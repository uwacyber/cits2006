"""CITS2006 Lab 2: Privacy. Complete the functions marked TODO, then run:  python lab2_privacy.py

Needs: pandas, numpy, scikit-learn (installed in Lab 0). Put water_release.csv and leaked_bill.txt
in the same folder as this file (it finds them there, whichever folder you run it from).
"""
import re
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

HERE = Path(__file__).resolve().parent
CLIP = 1000  # Task 4: about the 99th percentile of daily usage, so the sensitivity of a sum is 1000


def load_release(path=HERE / "water_release.csv"):
    return pd.read_csv(path, parse_dates=["datetime"])


def parse_bill(text):
    """Return [(date, reading)] from the leaked bill, with date as a datetime.date."""
    rows = re.findall(r"(\d{2}/\d{2}/\d{4})\s+(\d+)", text)
    return [(pd.to_datetime(d, format="%d/%m/%Y").date(), int(r)) for d, r in rows]


def link_bill(release, bill):
    """TODO Task 1: return the household (e.g. 'H07') whose readings match every line of the bill.
    Hint: release["datetime"].dt.date gives the date of each row."""
    raise NotImplementedError


def reid_accuracy(features, labels, seed=0):
    """Task 2 (provided): train a classifier to predict the household from `features`; return test accuracy."""
    X_train, X_test, y_train, y_test = train_test_split(
        features, labels, test_size=0.2, random_state=seed, stratify=labels)
    model = RandomForestClassifier(n_estimators=50, random_state=seed).fit(X_train, y_train)
    return model.score(X_test, y_test)


def daily_usage(release):
    """TODO Task 3: return one row per household per day with columns household, datetime, litres
    (litres = sum of that day's `diff`).
    Hint: set_index("datetime"), groupby("household"), resample("D"), then .reset_index(name="litres")."""
    raise NotImplementedError


def dp_sum(values, clip, epsilon, rng):
    """TODO Task 4: clip each value to [0, clip], sum, and add Laplace noise with scale clip / epsilon.
    Use rng.laplace(0.0, scale)."""
    raise NotImplementedError


def main():
    release = load_release()
    bill = parse_bill((HERE / "leaked_bill.txt").read_text())
    print(f"{len(release)} rows, {release['household'].nunique()} households; chance = {1 / 14:.1%}")
    try:
        print("Task 1: the bill belongs to", link_bill(release, bill))
    except NotImplementedError:
        print("Task 1: not done yet")
    print(f"Task 2: one hourly reading re-identifies {reid_accuracy(release[['meter.reading']], release['household']):.1%}")
    try:
        daily = daily_usage(release)
        print(f"Task 3: daily litres re-identify {reid_accuracy(daily[['litres']], daily['household']):.1%}")
    except NotImplementedError:
        print("Task 3: not done yet")
        return

    # Task 4: the attacker's target is the household-day with the most litres. That is over CLIP L,
    # so clipping matters: the most any clipped answer can reveal is CLIP L.
    heaviest = daily.loc[daily["litres"].idxmax()]
    who, when, target = heaviest["household"], heaviest["datetime"], heaviest["litres"]
    day = daily[daily["datetime"] == when]
    others = day.loc[day.index != heaviest.name, "litres"]
    exact = day["litres"].sum() - others.sum()
    seen = day["litres"].clip(0, CLIP).sum() - others.clip(0, CLIP).sum()  # what clipping leaves visible
    print(f"Task 4: {who} used {target:.0f} L on {when:%Y-%m-%d}. With no noise, "
          f"total minus total-without-{who} = {exact:.0f} L: exactly their usage")
    print(f"Task 4: Clipped to {CLIP} L, no noise: the attacker gets {seen:.0f} L. The {target - seen:.0f} L above "
          f"the clip is hidden, but they learn {who} used at least {seen:.0f} L")
    try:
        rng = np.random.default_rng(0)
        assert abs(dp_sum([5 * CLIP], CLIP, 1e9, rng) - CLIP) < 1, (
            f"dp_sum([{5 * CLIP}], {CLIP}, 1e9, rng) should be about {CLIP}: "
            "clip each value to [0, clip] and use noise scale clip / epsilon")
        for eps in (10.0, 1.0, 0.1):
            guesses = [dp_sum(day["litres"], CLIP, eps, rng) - dp_sum(others, CLIP, eps, rng) for _ in range(200)]
            print(f"Task 4: epsilon={eps:>4}: attacker's average error {np.mean(np.abs(np.array(guesses) - seen)):8.1f} L")
    except NotImplementedError:
        print("Task 4: not done yet")


if __name__ == "__main__":
    main()
