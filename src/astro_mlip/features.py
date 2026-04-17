from __future__ import annotations

import numpy as np
import pandas as pd

SURFACE_SPECIES = {"Si", "O", "Mg", "Fe"}


def _pairwise_distances(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    diff = a[:, None, :] - b[None, :, :]
    return np.linalg.norm(diff, axis=-1)


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build simple geometry/composition features from a flattened configuration table.

    Expected columns:
        ads_x, ads_y, ads_z,
        n_si, n_o, n_mg, n_fe,
        site_x, site_y, site_z,
        roughness, water_coverage, target_energy
    """
    feat = pd.DataFrame(index=df.index)

    ads = df[["ads_x", "ads_y", "ads_z"]].to_numpy(dtype=float)
    site = df[["site_x", "site_y", "site_z"]].to_numpy(dtype=float)

    d = np.linalg.norm(ads - site, axis=1)
    feat["ads_site_distance"] = d
    feat["inv_ads_site_distance"] = 1.0 / np.clip(d, 1e-6, None)
    feat["exp_ads_site_distance"] = np.exp(-d)

    for c in ["n_si", "n_o", "n_mg", "n_fe", "roughness", "water_coverage"]:
        feat[c] = df[c].astype(float)

    feat["metal_fraction"] = (feat["n_mg"] + feat["n_fe"]) / np.clip(
        feat["n_si"] + feat["n_o"] + feat["n_mg"] + feat["n_fe"], 1e-6, None
    )
    feat["fe_to_mg_ratio"] = feat["n_fe"] / np.clip(feat["n_mg"], 1.0, None)
    feat["surface_heterogeneity"] = feat["roughness"] * (1.0 + feat["metal_fraction"])
    feat["water_distance_coupling"] = feat["water_coverage"] * feat["ads_site_distance"]

    return feat
