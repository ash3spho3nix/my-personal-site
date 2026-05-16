---
title: "Work"
description: "15 years building simulation infrastructure — battery electrochemistry, EV systems, AI tooling, and on-premise LLM deployment."
draft: false
build:
  list: never
  render: always
---

15 years across automotive R&D. The consistent thread: build the infrastructure that makes the problem tractable — not just solve the immediate instance of it.

**2 patents · 3 simulation teams built from scratch · 10+ engineers led · 60% model dev time reduction (MBRD)**

📄 **[Full Experience & CV →](/work/experience/)**

---

## 🏆 Patents & Publications

Surfaced here because they represent the clearest external signal of original work.

- **Patent:** Cooling system for fuel cell vehicle/EV — *Inventor's Award, Mercedes-Benz, 2016*
- **Patent:** Efficient power recapturing from vehicle suspension — *Mercedes-Benz, 2017*
- **Publication:** [Estimating wood material properties for CFD fire modelling](http://vuir.vu.edu.au/id/eprint/10198) — *Victoria University, Melbourne, 2010*

---

## 🔋 Battery & Electrochemistry

The core domain — electrochemical modelling, thermal simulation, ageing, and system-level battery behaviour. Work spans cell characterisation through pack-level simulation across five companies.

- [Battery Modeling: When Your Elegant Equation Meets Reality](/work/projects/battery-modeling/)
  *Cross-company · 2015–present · analysis*
  ECM vs DFN vs data-driven — what each gets wrong, and why hybrids are the real answer.

- [Thermal Management System Modeling](/work/projects/thermal-management/)
  *Mercedes-Benz R&D · 2015–2021 · tool*
  Building the full EV TMS from scratch — battery, inverter, DC-DC, coolant loop, HVAC — integrated into the in-house vehicle simulation framework.

- [Battery Thermal Model Configurator](/work/projects/battery-thermal-configurator/)
  *Mercedes-Benz R&D · 2019–2021 · tool*
  Couples CFD cooling channel results to a reduced-order thermal ROM — generates a fully-parameterised Simulink thermal model. **60% reduction in model development time.**

- [DC Box Thermal Modelling](/work/projects/dc-box-thermal/)
  *Mercedes-Benz R&D · 2016–2018 · analysis*
  The component nobody thinks about until it fails. 96% experimental accuracy; design margin identified before hardware.

- [Charging Time: Why 80% Is Not Half the Problem](/work/projects/charging-time/)
  *Mercedes-Benz R&D · 2017–2018 · analysis*
  CC-CV physics, C-rate tradeoffs, and why fast charging is a thermal problem as much as an electrochemical one.

- [Battery Simulation Framework](/work/projects/battery-simulation/)
  *Volvo Trucks R&D · 2022 · tool*
  Standalone simulation environment with BMS-as-first-class-citizen, plus a PINN degradation model built for mobile inference.

- [Virtual Cell Scaling](/work/projects/battery-scaling/)
  *A123 Systems · 2022–present · tool*
  Physics-based scaling across capacity, form factor, and chemistry — for when you don't have the cell you need.

- [OpenFOAM Battery Simulator](https://github.com/ash3spho3nix/Battery_OpenFoam_Simulator)
  *Self-initiated · open source · tool*
  Python interface layer turning OpenFOAM CFD into a callable function — enabling parameter sweeps, optimisation, and AI integration. [Full writeup →](/work/projects/openfoam-battery/)

---

## 🛠️ Engineering Tools Built

Tools that exist, are used, and reduce the cost of doing the next project. Mix of OEM-commissioned and self-initiated.

- [Battery Thermal Model Configurator](/work/projects/battery-thermal-configurator/)
  *Mercedes-Benz R&D · 2019–2021 · tool*
  **60% reduction in thermal model development time.** Generates parameterised CFD-thermal ROM for HV battery systems.

- [Model Validation Framework]
  *Mercedes-Benz R&D · 2018–2020 · tool*
  Automated pipeline: fetch test data + battery model → run simulations → validate → upload report.

- [Current Limits Generator](/work/projects/current-limits-generator/)
  *A123 Systems · 2023 · tool*
  Physics-based current envelope covering lithium plating onset, side reactions, thermal limits, and thermal runaway margin — aging-aware, OEM-deliverable.

- [Pack Cost Estimator]
  *A123 Systems · 2023 · tool*
  RFQ/pre-RFQ phase commercial tool — cell selection through pack concept cost in a single run.

- [Front Fender Drag Optimization](/work/projects/front-fender-design/)
  *Hero MotoCorp · 2014 · method + tool*
  ANN surrogate + Firefly algorithm. 12% drag reduction, 10× speedup versus CFD-in-loop. The method generalises.

---

## ⚙️ Mechanics, CFD & Dynamics

The foundation — structural analysis, contact mechanics, vibration, and fluid dynamics from the first decade of the career. The physics intuition from this work keeps appearing in battery and AI contexts.

- [Tire Modelling: What a Spinning Ring Taught Me About Everything](/work/projects/tire-modelling/)
  *IIT Kanpur M.Tech · 2010–2011 · analysis*
  Standing waves, critical velocity, contact mechanics. The thesis that established the pattern: rotate a structure and everything changes.

- [Piston Rings: Friction, Sealing, and the Physics of Things That Touch](/work/projects/piston-rings/)
  *TVS Motor Company · 2011–2013 · analysis*
  Three simultaneous contact regimes, elastohydrodynamic lubrication, ring flutter. Where the interesting failure always lives at the boundary.

- [Magnesium Alloy Wheel Design](/work/projects/magnesium-wheel/)
  *TVS Motor Company · 2012–2013 · method + analysis*
  Topology optimisation, fatigue under realistic load spectra, thermal analysis. Material substitution is a system problem, not a materials problem.

- [Engine Mounts: Designing Something to Fail Softly](/work/projects/engine-mounts/)
  *Hero MotoCorp · 2013–2015 · method*
  NVH optimisation through stiffness design. Hybrid GA + Nelder-Mead, 15–20% cabin vibration reduction, verified on dynamometer.

- [Radar Modeling for Autonomous Driving](/work/projects/radar-autonomous-driving/)
  *Mercedes-Benz R&D · 2016–2017 · analysis*
  What sensors actually see — beam patterns, clutter, Kalman filter state estimation, and why edge cases aren't edge cases.

- [CFD Fire Modelling: The Inverse Problem Nobody Wants to Solve](/work/projects/cfd-fire-optimization/)
  *Victoria University, Melbourne · 2009 · method*
  Material property estimation by running the physics model backwards. GA + Nelder-Mead, cross-validated, published.

---

## 🤖 AI & Code Intelligence

Self-initiated — built outside the day job to solve problems the existing toolchain couldn't. **Runs on local LLMs (LM Studio) for GDPR-compliant on-premise deployment** — relevant for the German automotive context where sending engineering data to external APIs is not an option.

- [AI Systems: Building Tools That Understand Code, Not Just Generate It](/work/projects/ai-systems/)
  *Self-initiated · 2022–present · overview*
  The design philosophy connecting these tools: structure before generation, understanding before output.

- [Codebase Indexer](/work/projects/codebase-indexer/)
  *Self-initiated · 2023–present · tool*
  FAISS-based pre-filter navigation layer for local LLMs. Dependency graph, importance scoring, structural query layer. The difference between an agent that codes and one that understands.

- [Hybrid Code Analyzer](/work/projects/hybrid-code-analyser/)
  *Self-initiated · 2024 · tool*
  Static + dynamic analysis pipeline. Finds what neither alone can — runtime failures invisible to AST analysis, structural issues invisible to execution tracing.

- [Alchemist](https://github.com/ash3spho3nix/Alchemist) - on-going
  *Self-initiated · 2023 · tool*
  Indexes past repositories, extracts architectural patterns, suggests new combinations. Synthesis over generation.

- [Simple RAG Chatbot](https://github.com/ash3spho3nix/RAG-chatbot)
  *Self-initiated · 2022 · tool*
  First local RAG experiment — document retrieval, context injection, local LLM inference. The seed of the current toolchain.
