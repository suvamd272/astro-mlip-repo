import pandas as pd

from astro_mlip.features import build_features


def test_build_features_runs():
    df = pd.DataFrame(
        {
            "ads_x": [1.0],
            "ads_y": [2.0],
            "ads_z": [3.0],
            "site_x": [1.0],
            "site_y": [2.0],
            "site_z": [1.0],
            "n_si": [24],
            "n_o": [48],
            "n_mg": [2],
            "n_fe": [1],
            "roughness": [0.3],
            "water_coverage": [0.5],
            "target_energy": [-0.2],
        }
    )
    feat = build_features(df)
    assert "ads_site_distance" in feat.columns
    assert feat.shape[0] == 1
