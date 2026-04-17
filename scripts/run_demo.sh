#!/usr/bin/env bash
set -euo pipefail

PYTHONPATH=src python -m astro_mlip.mock_dataset --out data.csv --n-samples 500
PYTHONPATH=src python -m astro_mlip.train_toy_mlip --data data.csv --model-out toy_model.joblib
PYTHONPATH=src python -m astro_mlip.reaction_scan --model toy_model.joblib --out reaction_scan.csv
PYTHONPATH=src python -m astro_mlip.ir_spectrum --out ir_spectrum.csv

echo "Demo finished. Generated: data.csv, toy_model.joblib, reaction_scan.csv, ir_spectrum.csv"
