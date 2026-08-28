# Reproducibility checklist

## Core expected data checks

- Final Mw*≥2.5 catalogue: 30,347 events
- Retained grid cells: 1,080
- Complete calendar days: 5,844
- Training origins: 3,616
- Validation origins: 1,089
- Test origins: 1,089
- LT smoothing epsilon: 0.10
- LT statewide expected 7-day count: 8.75

## Tuned XGBoost 4-vs-5 audit

Expected:
- 4-window score: -0.03614813162214664; iteration 167
- 5-window score: -0.03614997127781987; iteration 190
- bootstrap CIs for block lengths 7, 14, 30 all include zero

## Final test ranking

1. XGBoost
2. Poisson
3. ConvLSTM
4. LT

Use `reference_results/` for exact comparison values.
