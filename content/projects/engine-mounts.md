---
title: "Engine Mounts Vibration Optimization"
description: "Design of engine mounts to minimize structure-borne vibration and NVH."
date: 2024-01-15
draft: false
---

## Problem

Engine vibration → structure-borne noise → cabin discomfort. Mounting design must balance stiffness (load support) and damping (vibration isolation).

## Methodology

1. **FEA of powertrain-frame assembly** capturing key modes
2. **Mount stiffness & damping parameter optimization** using metaheuristics (GA, Nelder-Mead)
3. **Frequency response analysis** (FRF) to minimize vibration transmission in comfort-sensitive range (20–200 Hz)
4. **Validation** on dynamometer with accelerometer measurements

## Outcome

Achieved 15–20% reduction in cabin vibration levels while maintaining engine support margin.

## Key Insight

Non-linear mount behavior (stiffness variation with load/frequency) is critical—linear models overestimate isolation capability.
