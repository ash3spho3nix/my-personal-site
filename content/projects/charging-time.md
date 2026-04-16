---
title: "Charging Time Calculation"
description: "Analytical and simulation-based approach to estimating EV battery charging time under various conditions."
date: 2018-01-01
tags: ["battery", "EV", "charging", "simulation"]
draft: false
---

## Overview

Charging time estimation is a non-trivial problem in EV systems. It's not just "capacity / current" — the actual charging time depends on the interplay between electrochemical limits, thermal constraints, and the CC-CV charging profile.

---

## Approach

The methodology combines:

- **CC-CV charging profile** — Constant current phase until voltage limit, then constant voltage phase until current drops below threshold
- **Thermal model** — Temperature rise during fast charging narrows the allowable current window
- **SOC estimation** — Open circuit voltage vs SOC lookup, coupled with coulomb counting

---

## Key Parameters

| Parameter | Description |
|-----------|-------------|
| C-rate | Charge rate relative to nominal capacity |
| Vmax | Upper voltage cut-off |
| T_cell | Cell temperature during charging |
| η_coulombic | Coulombic efficiency |

---

## Results

For a nominal NMC cell at 1C:
- CC phase dominates until ~80% SOC
- CV phase accounts for the remaining ~20% but takes disproportionately longer
- Temperature rise during fast charging (2C+) can trigger current derating, extending total time significantly

---

## Notes

This work was part of broader battery modeling efforts at Mercedes-Benz R&D, contributing to understanding fast-charge feasibility under real operating conditions.
