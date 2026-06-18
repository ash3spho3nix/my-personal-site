---
title: "Full-Vehicle Simulation Framework"
description: "Three years of expanding an in-house EV/HEV/PHEV simulation framework at Mercedes-Benz R&D — from ICE model libraries through BMS integration, thermal management, ADAS, and multi-architecture DOE capability."
date: 2018-01-01
tags: ["simulation", "battery", "EV", "Mercedes-Benz", "framework"]
draft: false
---

## What This Was

This wasn't a project with a start date and a delivery date. It was three to four years of incremental work on a living codebase that had to keep working while being extended.

Mercedes-Benz R&D, in collaboration with other European OEMs, built an in-house full-vehicle simulation framework on top of CarSim — initially scoped for IC engine vehicles. When I joined in 2015, the task was to extend that framework for EV, HEV, and PHEV architectures, improve the existing model libraries, and build the component models that didn't yet exist.

Nobody blogs about this kind of work. There are no dramatic results — no single number that summarises what was done. What there is: a framework that a team of engineers could trust to run simulations for architectural decisions on real programmes (E-Class, S-Class, AMG, EQC), and a platform that later became the base for SiL testing and ADAS algorithm validation.

---

## The Architecture

The simulation hierarchy had four levels:

- **Experiment** — top-level orchestration: defines the simulation campaign, loops, parameter variations, and output collection
- **Configuration** — selects the vehicle architecture (ICE / HEV / PHEV / BEV) and the component set
- **Architecture** — wires the subsystem models together: drivetrain, battery, thermal, BMS, ADAS as appropriate
- **Vehicle** — the component library instantiation: specific cell models, motor maps, cooling layouts, BMS parameterisation

Each level was parameterised independently, so you could swap a component model without touching the architecture layer, or run a DOE across configurations without rebuilding the vehicle model. This separation of concerns was deliberate and was what made the framework usable for multiple programmes simultaneously.

---

## What Was Built

**Vehicle Dynamics** — the starting point. The existing ICE vehicle dynamics models needed review before anything new was added on top. Tyre models, suspension kinematics, braking, load transfer. Got these to a state where EV-specific torque delivery behaviour could be properly captured.

**EV/HEV/PHEV Architecture** — the core extension. Built the architecture layer that allows the framework to switch between powertrains without model surgery. Charging system integration, motor/inverter models, recuperation logic, energy management strategy integration points.

**BMS and Battery Integration** — modelled the battery pack interaction with the vehicle: SoC tracking, current limits, thermal state feedback to the vehicle energy management. The BMS logic layer was designed to be swappable — either a behavioural model or, in the SiL branch, actual compiled BMS software code.

**Thermal Management System** — the most coupled subsystem. Connects vehicle-level cooling (coolant circuits, heat exchangers, radiator, HVAC) to battery thermal state. The challenge was that the battery thermal dynamics and the HVAC dynamics operate on different timescales — getting that coupling numerically stable without excessive stiffness required care. *Filed a patent on the cooling system architecture.*

**DC-DC Converter Thermal Model** — a targeted fix for a real field problem. Overheating was being observed in deployed vehicles. Built a high-fidelity thermal model of the DC-DC converter, validated against test data at 96% accuracy, identified the design margin issue before hardware changes were made.

**ADAS Branch** — a side branch of the framework developed for ADAS algorithm validation. Worked specifically on the Lidar integration: beam patterns, point cloud generation, sensor field of view modelling. Radar work followed — beam pattern simulation, clutter modelling, Kalman filter state estimation for target tracking.

**SiL Branch** — another side branch: the BMS software code compiled and integrated into the full-vehicle simulation loop. Allows the BMS team to validate software logic against realistic vehicle dynamics and thermal boundary conditions before hardware.

**Optimisation and DOE Layer** — added late in the project. Users could define parameter ranges, select component variants (e.g., different battery chemistries, cooling configurations, drivetrain topologies), and run design-of-experiments studies across the full vehicle model. Variants developed included AMG (high-performance thermal loads), EQC (BEV architecture), standard E-Class, S-Class, and SUV configurations.

---

## What Made It Hard

The framework had to remain functional for existing ICE programmes while EV extensions were being added. No freeze periods. Every new module had to be backward-compatible, every interface had to be documented well enough that another engineer could use it without asking.

The coupling between subsystems — particularly battery thermal state, BMS logic, and TMS — created numerical stiffness that required solver configuration tuning and, in some cases, model architecture changes to make simulation time acceptable.

The ADAS and SiL branches needed the core framework to be stable before they could be developed. The order of development mattered, and the sequencing decisions made in years one and two constrained what was possible in years three and four.

---

## Outcomes

- Unified platform covering ICE, HEV, PHEV, BEV — used across E-Class, S-Class, AMG, EQC programmes
- SiL capability for BMS software validation integrated into the same framework
- ADAS validation branch with Lidar and radar sensor modelling
- DOE and optimisation layer enabling systematic architectural trade studies
- Component library with parameterised variants across multiple vehicle platforms
- Two patents filed during this period

---

## Related Work

- [Thermal Management System](/work/projects/thermal-management/) — the TMS module developed as part of this framework
- [DC Box Thermal Modelling](/work/projects/dc-box-thermal/) — targeted component model developed in parallel
- [Radar Modelling for Autonomous Driving](/work/projects/radar-autonomous-driving/) — ADAS branch work
- [Battery Simulation Framework (Volvo)](/work/projects/battery-simulation-Volvo/) — same instinct, different context: Volvo standalone battery framework built on lessons from Mercedes
