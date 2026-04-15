---
title: "CFD Fire Modeling Material Optimization"
description: "Estimating wood material properties for CFD-based fire simulation using optimization."
date: 2024-01-15
draft: false
---

## Overview

Fire safety in buildings requires predicting flame spread, heat release, and smoke propagation. Material properties (thermal conductivity, heat capacity, ignition temperature) are critical inputs to CFD models—yet often unavailable or poorly characterized.

## Inverse Problem

**Given:**
- Experimental fire test data (temperature, flame propagation)
- CFD fire model (simplified)

**Find:** Material properties that best match observed behavior

## Solution Approach

1. **Parameter Estimation** via nonlinear optimization (Nelder-Mead, genetic algorithm)
2. **Sensitivity Analysis** — Which parameters matter most?
3. **Validation** — Cross-check against independent test data

## Outcome

Derived accurate material properties for several wood species, enabling predictive fire safety analysis.

## Publication

Results published: *"Estimating wood material properties using optimization techniques for CFD based fire modeling"*

## Industrial Relevance

Applicable to:
- Building code compliance (fire rating prediction)
- Material development (optimizing fire resistance)
- Accident investigation (reconstructing fire behavior)
