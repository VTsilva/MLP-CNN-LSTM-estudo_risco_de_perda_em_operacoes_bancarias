---
name: time-series-data-audit
description: Audit temporal datasets, build chronological splits/windows, and detect data leakage before time-series model training.
---

# Time Series Data Audit

## When to use
When ingesting, cleaning, exploring, splitting or generating supervised windows from any temporal dataset.

## Procedure
1. Preserve immutable raw input; record file, source, extraction date and snapshot limitations.
2. Parse timestamps explicitly; sort chronologically; check duplicates, missing timestamps, missing values, frequency and interval gaps.
3. Confirm the target and feature semantics from authoritative documentation; do not infer units or meaning from column names alone.
4. Describe trend, local variability, distribution, outliers, ACF/PACF, spectral structure and stationarity only when they support a decision.
5. Separate contemporaneous association from lagged predictive association; neither establishes causality.
6. Split chronologically before fitting scalers or selecting preprocessing. Fit transformations on training only.
7. Create samples as past window -> future target; assert each input index precedes target.
8. For validation/test, allow earlier already-observed history as context if realistic, while keeping targets inside their designated partition and excluding them from fitting.
9. Compare model candidates against a simple baseline, such as persistence, using identical target timestamps.
10. Keep test untouched during feature, lookback, architecture and epoch selection.

## Lookback selection
- Explain lookback separately from rolling descriptive windows.
- Define a small candidate set, here 13/26/52/104 weekly observations.
- Compare candidates on validation using same split and target dates.
- Record sample counts, scaling, metrics and the decision rationale.
- Do not claim 52 weeks represents annual seasonality unless evidence independently supports it.

## Required reporting
For each analysis: question, rationale, method, observed result, limitation, and consequence for the next step. Any failed assertion or irregular interval must be resolved or explicitly justified before training.
