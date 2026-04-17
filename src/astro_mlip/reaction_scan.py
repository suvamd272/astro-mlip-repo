from __future__ import annotations

import argparse
import joblib
import numpy as np
import pandas as pd

from .features import build_features


def build_scan_dataframe(n_points: int = 100) -> pd.DataFrame:
    distances = np.linspace(1.2, 4.5, n_points)
    rows = []
    for d in distances:
        rows.append(
            {
                "ads_x": 4.0,
                "ads_y": 4.0,
                "ads_z": d,
                "site_x": 4.0,
                "site_y": 4.0,
                "site_z": 0.0,
                "n_si": 24,
                "n_o": 48,
                "n_mg": 3,
                "n_fe": 1,
                "roughness": 0.4,
                "water_coverage": 0.5,
                "target_energy": 0.0,
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True)
    parser.add_argument("--out", type=str, default="reaction_scan.csv")
    args = parser.parse_args()

    artifact = joblib.load(args.model)
    model = artifact["model"]

    scan_df = build_scan_dataframe()
    X = build_features(scan_df)
    scan_df["predicted_energy"] = model.predict(X)
    scan_df.to_csv(args.out, index=False)

    min_idx = int(scan_df["predicted_energy"].idxmin())
    print(scan_df.loc[min_idx, ["ads_z", "predicted_energy"]])
    print(f"Saved scan to {args.out}")


if __name__ == "__main__":
    main()
