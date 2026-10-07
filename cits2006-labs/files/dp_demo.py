"""Differencing attack on a sum query, with and without differential privacy.

Run: python dp_demo.py   (needs numpy and pandas; data.csv in the same folder)
The attacker knows the sum over everyone and the sum over everyone except the target (row 0),
so subtracting the two reveals the target's value. The Laplace mechanism adds noise ONCE to each
query answer, scaled to the sensitivity (the most one person can change the sum) divided by epsilon.
"""
import numpy as np
import pandas as pd

CLIP = 250.0  # clip every sales_amount to [0, CLIP] (max in data.csv is about 249.52), so sensitivity = CLIP
RUNS = 1000


def clipped_sum(values):
    return float(np.clip(values, 0, CLIP).sum())


def dp_sum(values, epsilon, rng):
    return clipped_sum(values) + rng.laplace(0.0, CLIP / epsilon)


def main():
    rng = np.random.default_rng()
    everyone = pd.read_csv("data.csv")["sales_amount"].to_numpy()
    without_target, target = everyone[1:], everyone[0]
    print(f"Target's real value: {target:.2f}")
    print(f"No DP: sum(all) - sum(all but target) = {clipped_sum(everyone) - clipped_sum(without_target):.2f}")
    # Each attack uses two queries, so its total privacy cost is 2 x epsilon (sequential composition).
    for eps in (100.0, 10.0, 1.0, 0.1):
        errors = [abs(dp_sum(everyone, eps, rng) - dp_sum(without_target, eps, rng) - target) for _ in range(RUNS)]
        print(f"epsilon={eps:>5}: attacker's average error = {np.mean(errors):.2f}")


if __name__ == "__main__":
    main()
