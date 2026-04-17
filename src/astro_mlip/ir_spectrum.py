from __future__ import annotations

import argparse
import numpy as np
import pandas as pd


def autocorrelation(x: np.ndarray) -> np.ndarray:
    x = x - np.mean(x)
    corr = np.correlate(x, x, mode="full")
    corr = corr[corr.size // 2 :]
    return corr / np.max(np.abs(corr))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=str, default="ir_spectrum.csv")
    parser.add_argument("--n-steps", type=int, default=4096)
    parser.add_argument("--dt-fs", type=float, default=0.5)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    t = np.arange(args.n_steps) * args.dt_fs

    signal = (
        0.9 * np.sin(2 * np.pi * t / 24.0)
        + 0.5 * np.sin(2 * np.pi * t / 47.0)
        + 0.2 * np.sin(2 * np.pi * t / 90.0)
        + rng.normal(0.0, 0.15, size=args.n_steps)
    )

    acf = autocorrelation(signal)
    spectrum = np.abs(np.fft.rfft(acf))
    freqs = np.fft.rfftfreq(len(acf), d=args.dt_fs)

    out = pd.DataFrame({"frequency_arb": freqs, "intensity_arb": spectrum})
    out.to_csv(args.out, index=False)
    print(f"Saved toy IR spectrum to {args.out}")


if __name__ == "__main__":
    main()
