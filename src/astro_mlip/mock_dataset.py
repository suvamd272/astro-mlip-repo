from __future__ import annotations

import argparse
import numpy as np
import pandas as pd


def synthetic_energy(
    distance: float,
    n_mg: int,
    n_fe: int,
    roughness: float,
    water_coverage: float,
    rng: np.random.Generator,
) -> float:
    """Toy energy model for adsorption/reaction configurations."""
    repulsion = 2.5 * np.exp(-2.0 * distance)
    attraction = -1.8 * np.exp(-0.8 * (distance - 1.8) ** 2)
    mg_stabilization = -0.08 * n_mg
    fe_stabilization = -0.15 * n_fe
    roughness_term = -0.3 * roughness
    water_term = -0.25 * water_coverage * np.exp(-0.5 * (distance - 2.2) ** 2)
    noise = rng.normal(0.0, 0.03)
    return repulsion + attraction + mg_stabilization + fe_stabilization + roughness_term + water_term + noise


def build_dataset(n_samples: int, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rows = []
    for _ in range(n_samples):
        n_si = 24
        n_o = 48
        n_mg = int(rng.integers(0, 6))
        n_fe = int(rng.integers(0, 4))
        roughness = float(rng.uniform(0.0, 1.0))
        water_coverage = float(rng.uniform(0.0, 1.0))

        site = rng.uniform([0, 0, 0], [8, 8, 1.5])
        lateral_offset = rng.normal(0.0, 0.8, size=2)
        z_height = rng.uniform(1.1, 4.5)
        ads = np.array([site[0] + lateral_offset[0], site[1] + lateral_offset[1], site[2] + z_height])

        energy = synthetic_energy(
            distance=float(np.linalg.norm(ads - site)),
            n_mg=n_mg,
            n_fe=n_fe,
            roughness=roughness,
            water_coverage=water_coverage,
            rng=rng,
        )

        rows.append(
            {
                "ads_x": ads[0],
                "ads_y": ads[1],
                "ads_z": ads[2],
                "site_x": site[0],
                "site_y": site[1],
                "site_z": site[2],
                "n_si": n_si,
                "n_o": n_o,
                "n_mg": n_mg,
                "n_fe": n_fe,
                "roughness": roughness,
                "water_coverage": water_coverage,
                "target_energy": energy,
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=str, default="data.csv")
    parser.add_argument("--n-samples", type=int, default=500)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    df = build_dataset(n_samples=args.n_samples, seed=args.seed)
    df.to_csv(args.out, index=False)
    print(f"Saved {len(df)} samples to {args.out}")


if __name__ == "__main__":
    main()
