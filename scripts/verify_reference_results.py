from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
boot = pd.read_csv(ROOT/"reference_results"/"xgb_4_vs_5_bootstrap.csv")
assert boot["ci_includes_zero"].all()
scores = pd.read_csv(ROOT/"reference_results"/"final_test_scores.csv")
ranking = scores.sort_values("test_log_score", ascending=False)["model"].tolist()
assert ranking == ["XGBoost","Poisson","ConvLSTM","LT"]
print("Reference-result files are internally consistent.")
