---
title: "Experience"
description: "Full technical experience — roles, responsibilities, and projects with links."
draft: false
build:
  list: never
  render: always
---

📄 **[Download CV (PDF)](/CV_Vishal_Sharma.pdf)**

---

**Systems Modelling & Simulation Expert | 15 years**
Stuttgart, Germany · EU Blue Card · Open to relocation

Work spanning Tier 1 cell manufacturer and premium OEM R&Ds: A123 Systems, Mercedes-Benz, Volvo Trucks, Caterpillar, Hero MotoCorp, TVS.
Specialising in battery simulation infrastructure, electrochemical modelling, full-vehicle frameworks, and on-premise AI tooling.

---

## Core Competencies

**Simulation & Modelling:** Component & system-level modelling, reduced order modelling, coupled modelling, physics-based modelling, MBSE, simulation framework & toolchain development, optimisation methods — MATLAB/Simulink, Simscape/Stateflow, Python, GT-Suite, Modelica/OpenModelica, PINN/ML

**Battery Systems:** Pack development, cell-to-pack scaling, thermal & ageing modelling (calendric + cyclic), cell characterisation & parametrisation, BMS, LV & HV battery, ISO 26262

**Electrochemical Methods:** P2D/SPM/DFN modelling, Butler-Volmer kinetics, EKF/UKF state estimation, SoC/SoH estimation, PyBaMM, ECM/EEM

**FEM:** ANSYS, ABAQUS, HYPERMESH, FEMFAT, ParaView — thermal, structural, multiphysics

**Leadership & Delivery:** 8 years leadership, 3 simulation teams built, cross-timezone EMEA coordination (DE/US/CN), requirements engineering, RFI/RFQ technical strategy, IBM DOORS

---

## Work Experience

### A123 Systems GmbH, Germany
**Simulation Lead, EMEA** · *Nov 2022 – Present*

Final validation authority for all EMEA simulation deliverables — thermal, ageing, electrochemical. Translate OEM RFI/RFQ specifications into simulation scope, cascade to global teams (DE/IN/CN), and drive resolution across time zones.

- **Technical Governance:** Owned full simulation scope across 6 major RFQs and 15+ RFIs — from requirement extraction to final deliverable sign-off. Responsible for making sure A123 simulation outputs were technically defensible and OEM-accepted.
- **RFI/RFQ cycle time reduced ~30%** — identified that most delay came from ambiguous requirements and cross-team misalignment. Fixed both: defined a simulation requirements template, established a shared tracking structure with China HQ and US teams, reduced back-and-forth loops significantly.
- **Won 2 major OEM 48V contracts** (high volume, multi-million euro) — simulation-driven feasibility studies that translated test data (electrical, thermal, ageing) into a clear technical argument for why A123's cell met the OEM's pack-level requirements.
- **Motorsport — Porsche racing programme:** Led battery pack simulation under motorsport duty cycles — high C-rate pulses, aggressive thermal gradients. Physics-based electro-thermal modelling used to assess pack performance margins and identify thermal bottlenecks before hardware build.
- **Cell concept development:** Ran simulation-driven feasibility analysis for next-gen cell formats — comparing chemistry variants and form factors against performance, cycle-life, and manufacturing cost targets. Simulation as input to cell roadmap decisions.

**Tools built (self-initiated, in production use):**
- [Current Limits Generator](/work/projects/current-limits-generator/) — replaces empirical lookup tables with physics-based current envelopes: Li-plating onset (Butler-Volmer), SEI and electrolyte oxidation side reactions, lumped thermal model, thermal runaway margin
- [Virtual Cell Scaling](/work/projects/battery-scaling/) — scales validated electrochemical models across capacity, form factor, and chemistry variants; used when the target cell doesn't yet exist as hardware
- Pseudo-3D Electro-Thermal Pack Model — rapid concept evaluation tool: coupled RC + lumped thermal with cooling plate; ~70% reduction in concept assessment cycle time
- Pack Cost Estimator — commercial tool for RFQ phase; takes cell selection inputs and outputs pack-level cost breakdown
- All tools run on local LLM infrastructure (LM Studio / Ollama) for GDPR-compliant on-premise deployment — no engineering data sent to external APIs. → [How this infrastructure was built](/thinking/local-llm/)

---

### Volvo Trucks R&D, India
**Lead – Simulation & Analysis (Senior Manager)** · *Mar 2022 – Sep 2022*

Technical lead for 10-person multidisciplinary team covering thermal, charging, SIL/HIL, and full-vehicle simulation workstreams — including VECTO compliance — with shared responsibility alongside Swedish counterparts.

- **PINN-based battery degradation + charging model** for Volvo fleet mobile app — the constraint was hard: inference had to run in seconds on mobile hardware. Standard physics models are too slow; pure data-driven models aren't trustworthy outside training data. Physics-Informed Neural Network resolved both: physics constraints prevent unrealistic predictions, fast inference makes fleet-scale use practical. ~90% accuracy validated against Audi e-tron public data and internal test data.
- **Standalone [battery simulation framework](/work/projects/battery-simulation-Volvo/)** — Volvo's existing simulation was embedded inside a full-vehicle framework, which was slow and over-scoped for battery-focused studies. Built a decoupled environment with BMS as a first-class citizen — faster run times, easier parametric sweeps, cleaner separation of battery physics from vehicle integration logic.
- Led VECTO compliance simulation workstream — coordinated with Swedish counterparts on methodology, ensured India-side outputs met EU regulatory requirements.

---

### Caterpillar R&D, India
**Performance Engineer** · *Sep 2021 – Feb 2022*

New EV division, no existing battery simulation capability. Task was to build one.

- **Built battery modelling & simulation team from scratch** — defined the team structure, toolchain selection, development process, and the first set of simulation deliverables. Chose tools based on what could be sustained by a small team with varying backgrounds, not what looked most sophisticated on paper.
- **Cell Testing Facility established end-to-end** — from cell procurement and vendor selection through test procedure definition, equipment specification, and cross-site coordination with US. The facility needed to support model parameterisation, so test design was driven by what the models needed, not generic cycling protocols.
- Developed empirical degradation models for NMC and LFP chemistries — parameter estimation from experimental cycling data, thermal analysis to understand temperature-dependent degradation rates. Used as baseline before physics-based models were warranted by programme maturity.

---

### Mercedes-Benz R&D India Ltd.
**Technology Lead (Domain Expert)** · *Jun 2018 – Sep 2021*

Battery and simulation SME. Dual role: individual contributor on specialised battery modelling work, and technical lead for team growth and cross-site collaboration.

- **5× Business Growth** — portfolio grew from 1 to 7 parallel projects over three years. Growth came from building genuine technical credibility with Daimler counterparts in Stuttgart through regular visits, understanding their actual problems, and demonstrating that India-side work was audit-ready. Team expanded from 1 to 4 through direct hiring.
- **Battery modelling toolchain** — led end-to-end development: strategy, architecture, development standards, technical review, release management. The goal was not to produce models, but to produce a reproducible process for generating and validating models — one that could survive team turnover and pass external audit.
- **[Battery Thermal Model Configurator](/work/projects/battery-thermal-configurator/)** — built to reduce the recurring cost of thermal model development. Standardised ROM generation by combining CFD cooling channel results with 3D thermal analysis outputs into a parameterised Simulink thermal model. Adopted across Mercedes HV battery development; ~60% reduction in model development time per programme.
- Cross-functional collaboration with Stuttgart counterparts on BMS, thermal management, and charging simulation — served as the technical interface between India-side implementation and German programme requirements.

**Senior Engineer (Top Expert)** · *Jun 2015 – Jun 2018*

Joined during EV programme ramp-up. Primary task: extend the in-house full-vehicle simulation framework (originally ICE-based, derived from CarSim) to cover EV, HEV, and PHEV architectures.

- **[Full-vehicle simulation framework — EV/HEV/PHEV extension](/work/projects/full-vehicle-simulation/)** — built the architecture layer that allows the framework to switch between powertrains without model surgery. Developed and integrated: EV charging system, BMS logic and battery interface, Thermal Management System coupling vehicle cooling to battery thermal state, ADAS module (Lidar, radar), and a SiL branch for BMS software validation. Simulation hierarchy: Experiment → Configuration → Architecture → Vehicle (component libraries). Variants: AMG, EQC, E-Class, S-Class, SUV.
- **[Thermal Management System module](/work/projects/thermal-management/)** — the most coupled subsystem in the framework. Connects vehicle-level cooling circuits (coolant loops, heat exchangers, HVAC) to battery thermal state. Getting the coupling between battery thermal dynamics and HVAC dynamics numerically stable was non-trivial. *Filed a patent on the cooling system architecture.*
- **[DC-DC converter thermal model](/work/projects/dc-box-thermal/)** — built to diagnose field overheating. Developed high-fidelity thermal model, validated at 96% accuracy against test data, identified the design margin issue that hardware teams could then address.
- **[Radar modelling for autonomous driving](/work/projects/radar-autonomous-driving/)** — ADAS branch work: beam patterns, clutter, Kalman filter state estimation. Part of the ADAS algorithm validation capability built into the framework.
- Full-vehicle and component-level performance simulations for architectural decisions across pre-concept, concept, and post-production stages on E-Class, S-Class, AMG, EQC programmes.

---

### Hero MotoCorp Ltd., India
**Deputy Manager, R&D — Engine Design Group** · *Nov 2013 – May 2015*

- 1D/3D IC engine modelling — non-linear structural, thermal-structural, and fatigue analyses on pistons, crankshafts, engine casings; working through the full engine vibration stack from source to rider
- **[Front fender aerodynamic optimisation](/work/projects/front-fender-design/)** — problem was that CFD-in-loop optimisation was too slow for design iteration. Solution: trained an ANN surrogate model on CFD data, then optimised over the surrogate. 12% drag reduction, 10× speedup vs direct CFD. The surrogate approach was novel for the team at the time.
- **[Engine mount NVH optimisation](/work/projects/engine-mounts/)** — collaborative project with Altair to establish a simulation methodology for engine mount placement and material selection. The problem was multi-objective: isolate vibration, maintain positional stability, survive fatigue loading. Hybrid GA + Nelder-Mead; 15–20% cabin vibration reduction, verified on dynamometer.

---

### TVS Motor Company, India
**Member, R&D — Design & Analysis Group** · *Nov 2011 – Oct 2013*

- Linear and non-linear structural analyses of chassis components; topology optimisation for weight reduction under realistic load spectra
- **[Piston ring analysis](/work/projects/piston-rings/)** — three simultaneous contact regimes (hydrodynamic, mixed, boundary), elastohydrodynamic lubrication, ring flutter under combustion pressure; understanding where standard assumptions break down and what a more accurate model actually changes
- **[Magnesium alloy wheel design](/work/projects/magnesium-wheel/)** — material substitution project: Mg instead of Al. Not just strength check — topology optimisation, fatigue under realistic load spectra, thermal analysis to understand Mg-specific failure modes. Material substitution is a system problem.
- **ANSYS APDL macros** — automated pre-processing and analysis setup; ~50% reduction in time per analysis. First serious automation work — the same instinct that later produced the Battery Thermal Model Configurator and the current AI tooling.

---

### Victoria University, Melbourne — Research Intern · *Jun 2009 – Aug 2009*

**[CFD fire modelling](/work/projects/cfd-fire-optimization/)** — the problem: material thermal properties for fire simulation are difficult to measure directly. Solution: run the simulation backwards — use a genetic algorithm to find the property values that make the simulation match experimental measurements. GA + Nelder-Mead, cross-validated, published. First serious exposure to inverse problems and optimisation as a modelling strategy.

---

## Education

**M.Tech — Mechanical Engineering** | IIT Kanpur | 2010–2011
Thesis: *[Critical Velocity and Standing Waves in High-Speed Tires](/work/projects/tire-modelling/)* — contact mechanics, wave propagation in pressurised rotating rings, critical velocity analysis

**B.Tech — Mechanical Engineering** | IIT Kanpur | 2006–2010

---

## Patents & Publications

- *Patent:* Cooling system for fuel cell vehicle/EV to improve fuel efficiency — Inventor's Award, Mercedes-Benz · 2016
- *Patent:* Efficient power recapturing from vehicle suspension — energy harvesting for range extension · 2017
- *Publication:* [Estimating wood material properties using optimisation techniques for CFD fire modelling](http://vuir.vu.edu.au/id/eprint/10198) · Victoria University, 2010

---

**→ [Work & Projects](/work/)** · **→ [Career summary](/career/)**
