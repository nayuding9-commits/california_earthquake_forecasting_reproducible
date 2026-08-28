# Seven-Day Grid-Based Earthquake Forecasting in California

Reproducibility repository for the MSc Statistics project:

**A Comparative Study of Statistical and Machine-Learning Models for Seven-Day Earthquake Forecasting in California**

Models compared: long-term spatial rate (LT), Poisson regression, XGBoost and ConvLSTM.

## Recommended exact-reproduction route

Place the archived processed files in `data/`:

- `california_grid_centre_mask.csv`
- `earthquake_california_grid_2010_2025_Mw25_centre_mask.csv`

Then run notebooks `02`–`05` in order.

This is the recommended route for reproducing the submitted analysis because
ANSS ComCat is a live catalogue and historical event metadata may be revised
after the original analysis. The archived Mw*≥2.5 catalogue contains the
30,347 events used in the dissertation and is treated as the frozen modelling
input.

## Full preprocessing rebuild

Run notebooks `00` and `01`.

- `00` downloads/caches the 2024 Census TIGER/Line state boundary and rebuilds
  the 1,080-cell centre-based California mask.
- `01` downloads/caches ANSS ComCat data for 2010–2025 at reported M≥2.0,
  applies the magnitude-harmonisation procedure, and rebuilds an Mw*≥2.5
  catalogue from the currently available source data.

A newly rebuilt catalogue is saved separately for audit and does **not**
overwrite the archived dissertation input in `data/`.

Because ComCat is a live catalogue, a fresh download is not guaranteed to be
identical to the archived project catalogue.

## Notebook order

| Notebook | Purpose |
|---|---|
| `00_build_california_grid_mask.ipynb` | Boundary, 53×55 grid and 1,080-cell centre-based mask |
| `01_harmonise_catalogue.ipynb` | ComCat download, QC and magnitude harmonisation |
| `02_final_eda.ipynb` | Final report EDA |
| `03_lt_poisson_xgboost_model_selection.ipynb` | LT, Poisson and XGBoost validation-stage selection, including tuned 4-vs-5-window bootstrap comparison |
| `04_convlstm_model.ipynb` | ConvLSTM selection, checkpoint and test predictions |
| `05_final_test_evaluation.ipynb` | Frozen held-out 2023–2025 model comparison |

## Critical environment

The reported XGBoost model-selection results require:

- Python 3.12
- **xgboost==3.4.1**

The same reconstruction with xgboost 2.1.4 does not reproduce the reported
Poisson-objective validation scores. The XGBoost notebook therefore checks the
version explicitly.

The ConvLSTM development run used **PyTorch 2.8.0** and a single NVIDIA RTX
3060 Laptop GPU. ConvLSTM model selection was deliberately targeted rather
than exhaustive because repeated training on full 53×55 spatial sequences is
computationally expensive. GPU execution is strongly recommended for
retraining.

Create the environment:

```bash
conda env create -f environment.yml
conda activate earthquake-forecasting
jupyter lab
