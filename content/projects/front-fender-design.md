---
title: "Front Fender Design for Minimal Drag"
description: "ANN and firefly algorithm applied to aerodynamic shape optimization."
date: 2024-01-15
draft: false
---

## Overview

Aerodynamic drag is a primary energy loss in vehicles. This project used **meta-modeling** (neural networks + evolutionary algorithms) to optimize fender geometry for minimal drag without CFD re-runs on every iteration.

## Methodology

1. **Surrogate Model** — Train an ANN on CFD data (drag coefficient vs. geometry parameters)
2. **Optimization Loop** — Firefly algorithm explores the design space using the fast surrogate
3. **Validation** — Top designs re-evaluated with full CFD

## Key Innovation

Decoupling the **expensive simulation** (CFD) from the **optimization loop** (evolutionary algorithm). This enables rapid exploration of high-dimensional design spaces.

## Results

- Achieved 12% drag reduction
- 10× faster than traditional CFD-based optimization
- Robust to manufacturing tolerances

## Broader Lesson

**Meta-modeling** is a powerful paradigm:
- Physics simulations are expensive → build fast surrogates
- Evolutionary algorithms are data-hungry → train on simulation data
- Validation closes the loop → refine as needed
