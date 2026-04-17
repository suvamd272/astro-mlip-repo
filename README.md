# Astro-MLIP Starter Repo

A compact starter repository for **astrochemistry-inspired machine learning interatomic potentials (MLIPs)**.

This project is designed as a **portfolio/demo repo** for PhD applications involving:
- grain-surface reactions in astrochemistry
- silicate or ice-covered surfaces
- machine learning interatomic potentials
- reaction exploration and spectroscopy

It does **not** claim to be a production-ready MLIP. Instead, it shows that you understand the full workflow:

**reference data -> descriptors -> model training -> structure scoring -> toy reaction scan -> IR-like analysis**

## Why this repo is relevant

The Aarhus project is about building GNN-based interatomic potentials trained on DFT data to study reactions on realistic silicate grain surfaces. This starter repo mirrors that logic at a toy level:

1. create surface + adsorbate configurations
2. generate mock reference energies and forces
3. train a baseline ML model
4. rank candidate structures / pathways
5. compute a toy IR spectrum from a dipole-like trajectory signal

You can later replace the toy model with:
- NequIP
- MACE
- Allegro
- SchNet

## Repo structure

```text
astro_mlip_repo/
├── README.md
├── requirements.txt
├── configs/
│   └── demo_config.yaml
├── examples/
│   └── application_blurb.md
├── scripts/
│   └── run_demo.sh
├── src/
│   └── astro_mlip/
│       ├── __init__.py
│       ├── mock_dataset.py
│       ├── features.py
│       ├── train_toy_mlip.py
│       ├── reaction_scan.py
│       └── ir_spectrum.py
└── tests/
    └── test_features.py
```

## What the demo does

### 1. Mock grain-surface dataset
`mock_dataset.py` builds small toy structures containing:
- a silicate-like slab made of Si/O atoms
- optional Mg/Fe substitutions
- a simple adsorbate (e.g. NH, HCN-like, or CH fragment)

The energies are synthetic but physically motivated:
- short-range repulsion
- attraction to undercoordinated surface regions
- composition-dependent stabilization from Mg/Fe sites

This is just a stand-in for real DFT labels.

### 2. Baseline descriptors
`features.py` computes simple geometry descriptors such as:
- pair-distance summaries
- minimum adsorbate-surface distance
- local counts within cutoffs
- composition counts

These are deliberately simple so the repo is lightweight and readable.

### 3. Toy MLIP training
`train_toy_mlip.py` trains a regression model on the synthetic data and reports:
- train/test RMSE
- feature importance proxy
- saved model artifact

### 4. Reaction exploration skeleton
`reaction_scan.py` scans a toy reaction coordinate such as bond approach distance and scores configurations using the trained model.

This mimics the idea of using a learned potential to explore reaction pathways more cheaply than DFT.

### 5. IR spectrum workflow
`ir_spectrum.py` generates a toy dipole autocorrelation function and converts it into a spectrum-like signal.

This connects to the project’s spectroscopy angle.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the full demo

```bash
bash scripts/run_demo.sh
```

Or step by step:

```bash
PYTHONPATH=src python -m astro_mlip.mock_dataset --out data.csv --n-samples 500
PYTHONPATH=src python -m astro_mlip.train_toy_mlip --data data.csv --model-out toy_model.joblib
PYTHONPATH=src python -m astro_mlip.reaction_scan --model toy_model.joblib --out reaction_scan.csv
PYTHONPATH=src python -m astro_mlip.ir_spectrum --out ir_spectrum.csv
```

## How to make this stronger for applications

Good upgrades for your GitHub:

1. Replace synthetic labels with a small DFT dataset.
2. Export structures to XYZ/extended XYZ for ASE workflows.
3. Add uncertainty estimation using ensembles.
4. Compare transferability across clean vs substituted vs ice-covered surfaces.
5. Add a notebook showing adsorption maps or reaction barrier sketches.
6. Swap the baseline regressor for a true equivariant model.

## Suggested GitHub description

> Astrochemistry-inspired MLIP starter project for grain-surface reactions: toy silicate surfaces, synthetic reference labels, reaction exploration, and IR-like analysis.

## Suggested lines for your CV or application

- Built a toy astrochemistry-inspired MLIP workflow for grain-surface reaction exploration on silicate-like surfaces.
- Demonstrated an end-to-end pipeline from reference data generation to regression, reaction-coordinate scanning, and IR-like spectral analysis.
- Designed the codebase to be easily extensible toward NequIP/MACE-based interatomic potentials on DFT datasets.

## Limitations

This repository uses **synthetic energies** and **simple descriptors**, so it is a proof-of-work repo, not a scientific benchmark. Its purpose is to show:
- clear scientific framing
- familiarity with MLIP workflows
- good code organization
- readiness to scale to real DFT-based datasets
