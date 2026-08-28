# Seven-Day Grid-Based Earthquake Forecasting in California

Reproducibility repository for the MSc Statistics project:

**A Comparative Study of Statistical and Machine-Learning Models for Seven-Day Earthquake Forecasting in California**

Models compared: long-term spatial rate (LT), Poisson regression, XGBoost and ConvLSTM.

## Recommended exact-reproduction route

Put the archived processed files in `data/`:

- `california_grid_centre_mask.csv`
- `earthquake_california_grid_2010_2025_Mw25_centre_mask.csv`

Then run notebooks `02`–`06` in order.

This is recommended for examination because ANSS ComCat is a live catalogue and
historical event metadata can be revised after the submitted analysis.

## Full preprocessing rebuild

Run notebooks `00` and `01`.

- `00` downloads/caches the 2024 Census TIGER/Line state boundary and rebuilds
  the 1,080-cell centre-based California mask.
- `01` downloads/caches ANSS ComCat data for 2010–2025 at reported M≥2.0,
  harmonises supported magnitude types to Mw-equivalent values, and creates the
  final Mw*≥2.5 catalogue.

A fresh live ComCat download is not guaranteed to be byte-identical to the
archived project catalogue.

## Notebook order

| Notebook | Purpose |
|---|---|
| `00_build_california_grid_mask.ipynb` | Boundary, 53×55 grid, 1,080-cell mask |
| `01_harmonise_catalogue.ipynb` | ComCat download/QC/magnitude harmonisation |
| `02_final_eda.ipynb` | Final report EDA |
| `03_lt_poisson_xgboost_model_selection.ipynb` | LT, Poisson and XGBoost validation-stage selection |
| `04_xgboost_4_vs_5_tuned_bootstrap_check.ipynb` | Final tuned 4-vs-5 XGBoost audit |
| `05_convlstm_model.ipynb` | ConvLSTM selection, checkpoint, test predictions |
| `06_final_test_evaluation.ipynb` | Frozen held-out 2023–2025 comparison |

## Critical environment

The reported XGBoost model-selection results require:

- Python 3.12
- **xgboost==3.4.1**

The same reconstruction with xgboost 2.1.4 does not reproduce the reported
Poisson-objective validation scores. The XGBoost notebooks therefore check the
version explicitly.

The ConvLSTM development run used **PyTorch 2.8.0**. GPU execution is strongly
recommended for retraining.

Create the environment:

```bash
conda env create -f environment.yml
conda activate earthquake-forecasting
jupyter lab
```

or, with Python 3.12 already installed:

```bash
python -m venv .venv
# activate .venv
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

## Chronological split

- Training origins: 30 Jan 2010–24 Dec 2019 (3,616)
- Validation origins: 1 Jan 2020–24 Dec 2022 (1,089)
- Test origins: 1 Jan 2023–24 Dec 2025 (1,089)

Seven-day gaps prevent target windows from crossing subset boundaries.

## Outputs

Generated files are written to:

- `outputs/figures/`
- `outputs/tables/`
- `outputs/models/`
- `outputs/predictions/`
- `outputs/audit/`

Large binary model/prediction files can be distributed through a GitHub Release
or the separate project data archive.

## Reference results

`reference_results/` contains compact values against which an examiner can check
a rerun.

The final tuned XGBoost feature-set audit reproduces:

- `{1,7,21,30}`: `-0.03614813162214664`, iteration 167
- `{1,7,10,21,30}`: `-0.03614997127781987`, iteration 190

The 7-, 14- and 30-day moving-block bootstrap intervals for the 4-window minus
5-window mean score difference all include zero.

Final held-out test scores are in `reference_results/final_test_scores.csv`.

## Fast environment check

```bash
python scripts/check_environment.py
python scripts/verify_reference_results.py
```

## AI-use statement

The dissertation states that ChatGPT was used primarily for language polishing
and to assist with code drafting and debugging. All code, analyses and final
written content were reviewed and verified by the author.
