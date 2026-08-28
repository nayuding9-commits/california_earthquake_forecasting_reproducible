import sys
print("Python:", sys.version)
if sys.version_info < (3, 12):
    raise SystemExit("ERROR: Python >=3.12 required.")
import xgboost as xgb
import torch
print("XGBoost:", xgb.__version__)
print("PyTorch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
if xgb.__version__ != "3.4.1":
    raise SystemExit(f"ERROR: expected xgboost==3.4.1, found {xgb.__version__}")
print("Critical environment checks passed.")
