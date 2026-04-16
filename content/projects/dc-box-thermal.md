---
title: "DC Box Thermal Modelling"
description: "Thermal modeling of the DC junction box for EV high-voltage systems."
date: 2019-01-01
tags: ["thermal", "EV", "DC", "simulation", "Mercedes-Benz"]
draft: false
---

## Overview

The DC box (junction box) is a critical component in EV high-voltage architecture. It houses fuses, contactors, and busbars that carry high current — and gets hot. Thermal runaway in this component can cascade to the pack.

---

## Scope

Thermal modeling of:
- Busbar heating under peak current load
- Contactor thermal limits
- Steady-state and transient temperature distribution
- Cooling pathway assessment

---

## Method

- **Lumped thermal network** — Each component modeled as a thermal resistance-capacitance node
- **Power loss calculation** — I²R losses for busbars, switching losses for contactors
- **Boundary conditions** — Ambient temperature, forced convection from pack cooling circuit proximity

---

## Outcome

The model was used to validate component selection against OEM thermal specifications and to identify hot-spot risks under worst-case (peak power + high ambient) scenarios.

---

## Context

Part of the broader vehicle-level battery and thermal system modeling work at Mercedes-Benz R&D India.
