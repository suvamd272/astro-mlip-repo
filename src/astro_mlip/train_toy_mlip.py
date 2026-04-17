from __future__ import annotations

import argparse
import json
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

from .features import build_features


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, required=True)
    parser.add_argument("--model-out", type=str, default="toy_model.joblib")
    parser.add_argument("--metrics-out", type=str, default="metrics.json")
    args = parser.parse_args()

    df = pd.read_csv(args.data)
    X = build_features(df)
    y = df["target_energy"].to_numpy(dtype=float)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=300, random_state=42)
    model.fit(X_train, y_train)

    pred_train = model.predict(X_train)
    pred_test = model.predict(X_test)

    metrics = {
        "train_rmse": float(np.sqrt(mean_squared_error(y_train, pred_train))),
        "test_rmse": float(np.sqrt(mean_squared_error(y_test, pred_test))),
        "train_r2": float(r2_score(y_train, pred_train)),
        "test_r2": float(r2_score(y_test, pred_test)),
        "n_train": int(len(X_train)),
        "n_test": int(len(X_test)),
        "feature_names": list(X.columns),
    }

    artifact = {"model": model, "feature_names": list(X.columns)}
    joblib.dump(artifact, args.model_out)
    Path(args.metrics_out).write_text(json.dumps(metrics, indent=2))

    print(json.dumps(metrics, indent=2))
    print(f"Saved model to {args.model_out}")
    print(f"Saved metrics to {args.metrics_out}")


if __name__ == "__main__":
    main()
