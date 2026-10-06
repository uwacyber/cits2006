# Lab 2: Privacy

## 2.1. Introduction

Removing names from a dataset does not make it anonymous. If some values are unique to a person (**quasi-identifiers**), anyone with a little outside knowledge can link the record back to them. This is a **linkage attack**, the same idea as the Netflix/IMDb example in the lecture.

In this lab you will:
1. re-identify a household in a "de-identified" water-usage release, using a leaked bill (Task 1);
2. measure how identifying a single value is (Task 2);
3. reduce the risk by aggregation (Task 3);
4. answer queries with differential privacy and watch a differencing attack fail (Task 4);
5. optionally, compute an average without seeing anyone's value, using homomorphic encryption (Task 5).

## 2.2. Setup

Use the Python environment from Lab 0 (`source ~/cits2006/.venv/bin/activate`, or the Windows equivalent). Download the files into one folder:

```
curl -LO https://github.com/uwacyber/cits2006/raw/live/cits2006-labs/files/water_release.csv
curl -LO https://github.com/uwacyber/cits2006/raw/live/cits2006-labs/files/leaked_bill.txt
curl -LO https://github.com/uwacyber/cits2006/raw/live/cits2006-labs/files/lab2_privacy.py
python lab2_privacy.py
```

The first run prints the size of the release, then "Task 1: not done yet", the Task 2 accuracy (that function is provided, so it works straight away) and "Task 3: not done yet". The script stops there: Task 4 only runs once `daily_usage()` works, and until `dp_sum()` is complete it shows the two no-noise attacks and then "Task 4: not done yet".

**The data.** A water utility released hourly smart-meter data for 14 households (March 2016 to February 2017). It replaced each customer's ID with a pseudonym (`H01`–`H14`). Columns:
- `household`: the pseudonym;
- `datetime`: when the reading was taken, to the second. Readings are roughly hourly but irregular: each household's meter reports at its own minute and second past the hour, and there are gaps where readings are missing;
- `meter.reading`: the cumulative meter value in litres, which only goes up, like an odometer;
- `diff`: litres used since the previous reading.

## 2.3. Task 1: Linkage attack

`leaked_bill.txt` is a water bill for "12 Example Street". It lists three dated meter readings. Complete `link_bill()` so it returns the pseudonym whose readings match the bill on those dates.

**Questions.**
- Start with only the first bill line. How many households match it? Why is a single cumulative meter reading enough to identify a household? Compare this with your Task 2 result.
- What other outside knowledge could an attacker use instead of a bill: a photo of the meter, a neighbour's observation, a plumber's invoice?

## 2.4. Task 2: How identifying is one value?

`reid_accuracy()` is provided. It trains a classifier to predict the household from the features you give it. The script runs it on `meter.reading` alone.

**Questions.**
- Compare the accuracy with chance (1 in 14, about 7%). Why is a cumulative counter so identifying?
- Name the quasi-identifiers in this release. Hint: look at the minutes and seconds of each household's readings, as well as the meter value.

## 2.5. Task 3: Mitigation by aggregation

Complete `daily_usage()` so it returns litres used per household per day (the sum of `diff`), dropping the cumulative counter. The script re-runs the classifier on the daily litres.

**Questions.**
- How much did re-identification drop? Is it zero?
- What analyses can no longer be done with daily totals (utility lost)?

## 2.6. Task 4: Differential privacy on queries

Instead of releasing records, the utility could answer **queries**, such as "total litres used by all households on 1 June". This is still unsafe: an attacker who also learns the total *without* one household subtracts the two answers. That is a **differencing attack**.

The Laplace mechanism defends against it by adding noise once to the query answer:
- The **sensitivity** is the most one household can change the answer. Clip each household's daily usage to `[0, 1000]` litres (about the 99th percentile), so the sensitivity is 1000.
- The noise is `Laplace(0, sensitivity / ε)`.

Complete `dp_sum()`. The script picks the household that used the most water on any one day (more than the 1000 L clip, so clipping matters) and runs the differencing attack on it:
- with no noise and no clipping, which recovers the household's usage exactly;
- with clipping but still no noise, where the attacker gets only 1000 L: the part above the clip stays hidden, but they learn the household used at least that much;
- with your `dp_sum()` at ε = 10, 1 and 0.1, printing the attacker's average error over 200 tries each, measured against that clipped 1000 L. With a correct `dp_sum()` expect about 150 L, 1,500 L and 15,000 L.

If `dp_sum()` does not clip each value and use noise scale `clip / ε`, the script stops with a message saying so.

**Questions.**
- How does the attacker's error change with ε? What does this cost an honest analyst?
- What does the attacker still learn at ε = 10, and what stays hidden even with no noise at all?
- The attacker asked two queries. If each one uses ε, what is the total privacy cost? (Look up *sequential composition*.)
- Why must values be clipped before adding noise? What if one household used 50,000 L in a day?

## 2.7. Task 5 (optional): Encrypted average

With the Paillier cryptosystem, anyone can add encrypted numbers, but only the key holder can decrypt the result. Install `phe` (`pip install phe` inside your venv) and:
1. generate a key pair;
2. encrypt each household's usage for one day;
3. add the ciphertexts;
4. decrypt only the total and divide by the number of households that day.

**Question.** Who learns what? What does this *not* protect against, for example once the total is published?

## 2.8. Summary

| Defence | Stops | Does not stop |
|---|---|---|
| Removing names (pseudonyms) | Casual browsing | Linkage on quasi-identifiers (Task 1) |
| Aggregation | Most record-level linkage | Unusual households; differencing on totals |
| Differential privacy | Differencing, with a quantified guarantee (ε) | Loss of accuracy; the budget runs out with many queries |
| Homomorphic encryption | The aggregator seeing individual values | Inference from the decrypted output |

The workshop CTF this week builds on these attacks and defences, using data generated just for you.
