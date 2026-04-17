# Astro MLIP Starter: Grain-Surface Reaction Exploration on Silicate-Like Models

## Overview

Astrochemistry-inspired MLIP starter project for grain-surface reactions: toy silicate surfaces, synthetic reference labels, reaction exploration, and IR-like analysis.

This repository is a proof-of-work project designed to demonstrate an end-to-end workflow relevant to machine-learning interatomic potentials (MLIPs) for surface chemistry. It includes toy structure generation, synthetic energy labeling, descriptor-based regression, reaction-coordinate exploration, and simple spectral analysis.

---

## Motivation

Chemical reactions on interstellar dust grains play an important role in astrochemistry, but realistic grain surfaces are structurally complex and chemically diverse. Silicate grains may be amorphous, compositionally variable, and partially covered by adsorbates such as water ice.

These features make first-principles studies expensive and difficult to scale. This repository serves as a compact prototype mimicking an MLIP workflow:

* Structure generation
* Reference labeling
* Surrogate model training
* Reaction coordinate exploration
* Scientific analysis

The current implementation uses simplified models and synthetic labels but is structured for future extension toward real DFT datasets and modern equivariant ML models.

---

## Current Features

* Generates toy silicate-like surface structures
* Assigns synthetic reference energies for rapid prototyping
* Extracts simple descriptors for ML regression
* Trains baseline regression models
* Scans reaction-like coordinates
* Produces IR-like / spectral-style outputs
* Modular and extensible code structure

---

## Repository Structure

* `src/` – core implementation
* `configs/` – configuration files
* `scripts/` – workflow scripts
* `examples/` – usage examples
* `tests/` – basic tests
* `requirements.txt` – dependencies

---

## Limitations

This repository uses **synthetic energies** and **simple descriptors**, so it is a proof-of-work project rather than a scientific benchmark.

Its purpose is to demonstrate:

* clear scientific framing
* familiarity with MLIP workflows
* modular code organization
* readiness for scaling to real datasets

It should not be interpreted as a quantitatively accurate model of silicate grain chemistry.

---

## Why This Project Matters

Although simplified, this repository reflects key components of realistic atomistic ML workflows:

* dataset construction
* descriptor generation
* surrogate modeling
* reaction exploration
* scientific visualization

It is intended as a stepping stone toward real MLIP development using DFT reference data and modern architectures such as NequIP or MACE.

---

## Installation

```bash
git clone git@github.com:YOUR_USERNAME/astro-mlip-repo.git
cd astro-mlip-repo
pip install -r requirements.txt
```

---

## Example Usage

```bash
python scripts/run_example.py
```

---

## Tests

```bash
pytest -q
```

---

## Planned Upgrades

The following extensions will significantly improve realism and impact:

1. Replace synthetic labels with DFT-computed energies
2. Export structures to XYZ / extended XYZ for ASE workflows
3. Add uncertainty estimation (ensemble models)
4. Study transferability across surface environments
5. Add visualization notebooks (adsorption maps, energy scans)
6. Upgrade to equivariant ML models (NequIP / MACE)

---

## HPC Readiness

This project is designed to scale toward high-performance workflows:

* large-scale structure generation
* parallel DFT data generation
* dataset curation
* MLIP training on HPC systems

---

## Relevance to MLIP Development

This repository was developed as a compact demonstration of how atomistic machine-learning workflows can be structured for surface-reaction problems.

While simplified, the codebase is designed to be extended toward DFT-driven MLIPs and high-performance training workflows.

---

## Author

Suvam kumar Das
University of Zurich

