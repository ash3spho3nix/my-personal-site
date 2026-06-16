---
title: "Work"
description: "Building simulation/modeling infrastructure - battery electrochemistry, EV systems, AI tooling, and on-premise LLM deployment."
draft: false
build:
  list: never
  render: always
---

{{% expand title="馃殌 Flagship Systems" %}}
Five projects that best represent the architectural approach: building
infrastructure that compounds, not tools that expire.

### [Battery Simulation Framework + PINN Degradation](/work/projects/battery-simulation/)
*Volvo Trucks R&D 路 2022* \
Problem: BMS teams needed fast iteration without dragging a full
vehicle model. System built: standalone simulation environment with
BMS as first-class citizen, plus a PINN degradation model running
at ~90% accuracy in seconds on mobile. The PINN was the only
formulation that satisfied both accuracy and mobile deployment
constraints simultaneously.

### [OpenFOAM Battery Simulator](/work/projects/openfoam-battery/)
*Self-initiated 路 Open source 路 2025* \
Problem: CFD-based battery simulation is powerful and routinely
impractical. System built: Python interface layer that converts
OpenFOAM from an expert-only C++ tool into a callable function -
enabling parameter sweeps, optimisation loops, and AI integration.
[GitHub 鈫抅(https://github.com/ash3spho3nix/Battery_OpenFoam_Simulator)

### [Current Limits Generator](/work/projects/current-limits-generator/)
*A123 Systems 路 2025* \
Problem: current limits were being computed manually, inconsistently,
and conservatively across OEM programmes. System built: physics-based
Python tool generating aging-aware current envelopes covering plating
onset, side reactions, thermal limits, and thermal runaway margin -
parameterised, OEM-deliverable, in production use.

### [Codebase Indexer](/work/projects/codebase-indexer/)
*Self-initiated 路 2025鈥損resent* \
Problem: AI coding agents generate code without understanding the
codebase they're editing. System built: structural repository
understanding layer - dependency graphs, importance scoring, semantic
retrieval - that gives a local LLM a map before it touches a line.
[GitHub 鈫抅(https://github.com/ash3spho3nix/Codebase_Indexer)

### [Hybrid Code Analyzer](/work/projects/hybrid-code-analyzer/)
*Self-initiated 路 2025* \
Problem: static analysis misses runtime failures; dynamic analysis
misses structural importance. System built: combined pipeline that
correlates runtime failures with structural centrality - finding
what neither approach alone can detect.
[GitHub 鈫抅(https://github.com/ash3spho3nix/hybrid_code_analyser)

{{% /expand %}}

---
{{% expand title="馃攱 Battery & Electrochemistry" %}}

The core domain - electrochemical modelling, thermal simulation, ageing, and system-level battery behaviour. Work spans cell characterisation through pack-level simulation across five companies.

- [Battery Modeling: When Your Elegant Equation Meets Reality](/work/projects/battery-modeling/) \
  *Cross-company 路 2015鈥損resent 路 analysis* \
  ECM vs DFN vs data-driven - what each gets wrong, and why hybrids are the real answer.

- [Thermal Management System Modeling](/work/projects/thermal-management/) \
  *Mercedes-Benz R&D 路 2015鈥?021 路 tool* \
  Building the full EV TMS from scratch - battery, inverter, DC-DC, coolant loop, HVAC - integrated into the in-house vehicle simulation framework.

- [Battery Thermal Model Configurator](/work/projects/battery-thermal-configurator/) \
  *Mercedes-Benz R&D 路 2019鈥?021 路 tool* \
  Couples CFD cooling channel results to a reduced-order thermal ROM - generates a fully-parameterised Simulink thermal model. **60% reduction in model development time.**

- [DC Box Thermal Modelling](/work/projects/dc-box-thermal/) \
  *Mercedes-Benz R&D 路 2016 路 analysis* \
  The component nobody thinks about until it fails. 96% experimental accuracy; design margin identified before hardware.

- [Charging Time: Why 80% Is Not Half the Problem](/work/projects/charging-time/) \
  *Mercedes-Benz R&D 路 2017鈥?018 路 analysis* \
  CC-CV physics, C-rate tradeoffs, and why fast charging is a thermal problem as much as an electrochemical one.

- [Battery Simulation Framework](/work/projects/battery-simulation/) \
  *Volvo Trucks R&D 路 2022 路 tool* \
  Standalone simulation environment with BMS-as-first-class-citizen, plus a PINN degradation model built for mobile inference.

- [Teaching a Neural Network the Laws of Battery Decay](/work/projects/pinn-battery/) \
  *Volvo Trucks R&D 路 2022 路 method* \
  Physics-Informed Neural Network for battery degradation - physics-constrained training that prevents physically impossible predictions. Built for real-time aging inference on mobile hardware.

- [Virtual Cell Scaling](/work/projects/battery-scaling/) \
  *A123 Systems 路 2025鈥損resent 路 tool*  \
  Physics-based scaling across capacity, form factor, and chemistry - for when you don't have the cell you need.

- [OpenFOAM Battery Simulator](https://github.com/ash3spho3nix/Battery_OpenFoam_Simulator) \
  *Self-initiated 路 2025 路 open source 路 tool* \
  Python interface layer turning OpenFOAM CFD into a callable function - enabling parameter sweeps, optimisation, and AI integration. [Full writeup 鈫抅(/work/projects/openfoam-battery/)

{{% /expand %}}

---
{{% expand title="馃洜锔?Engineering Tools Built" %}}

Tools that exist, are used, and reduce the cost of doing the next project. Mix of OEM-commissioned and self-initiated.

- [Battery Thermal Model Configurator](/work/projects/battery-thermal-configurator/) \
  *Mercedes-Benz R&D 路 2019鈥?020 路 tool* \
  **60% reduction in thermal model development time.** Generates parameterised CFD-thermal ROM for HV battery systems.

- Model Validation Framework \
  *Mercedes-Benz R&D 路 2018鈥?020 路 tool* \
  Automated pipeline: fetch test data + battery model 鈫?run simulations 鈫?validate 鈫?upload report.

- [Current Limits Generator](/work/projects/current-limits-generator/) \
  *A123 Systems 路 2025 路 tool* \
  Physics-based current envelope covering lithium plating onset, side reactions, thermal limits, and thermal runaway margin - aging-aware, OEM-deliverable.

- Pack Cost Estimator \
  *A123 Systems 路 2024 路 tool* \
  RFQ/pre-RFQ phase commercial tool - cell selection through pack concept cost in a single run.

- [Front Fender Drag Optimization](/work/projects/front-fender-design/) \
  *Hero MotoCorp 路 2014 路 method + tool* \
  ANN surrogate + Firefly algorithm. 12% drag reduction, 10脳 speedup versus CFD-in-loop. The method generalises.

{{% /expand %}}

---
{{% expand title="馃 AI & Code Intelligence" %}}

Self-initiated - built outside the day job to solve problems the existing toolchain couldn't. **Runs on local LLMs (LM Studio) for GDPR-compliant on-premise deployment** - relevant for the German automotive context where sending engineering data to external APIs is not an option.

- [Battery Expert AI: A Domain-Specific Assistant That Knows Its Physics](/work/projects/battery-ai-systems/) \
  *Self-initiated 路 2025鈥損resent 路 tool* \
  Local, on-premise AI assistant for battery engineering - LoRA fine-tuned on domain knowledge, RAG over electrochemistry papers and test data, with mathematical equation reasoning for PDEs and electrochemical models.

- [AI Systems: Building Tools That Understand Code, Not Just Generate It](/work/projects/ai-systems/) \
  *Self-initiated 路 2025鈥損resent 路 overview* \
  The design philosophy connecting these tools: structure before generation, understanding before output.

- [Codebase Indexer](/work/projects/codebase-indexer/) \
  *Self-initiated 路 2025鈥損resent 路 tool* \
  FAISS-based pre-filter navigation layer for local LLMs. Dependency graph, importance scoring, structural query layer. The difference between an agent that codes and one that understands.

- [Hybrid Code Analyzer](/work/projects/hybrid-code-analyzer/) \
  *Self-initiated 路 2025 路 tool*  \
  Static + dynamic analysis pipeline. Finds what neither alone can - runtime failures invisible to AST analysis, structural issues invisible to execution tracing.

- [AI-Assisted Simulation Debugger](/work/projects/ai-simulation-debugger/) \
  *Self-initiated 路 2026 路 concept* \
  Exploratory: treating simulation failures as propagating structural inconsistencies rather than isolated errors - AI-assisted root cause reasoning for engineering simulations.

- [Physics-Informed Neural Network - Battery Degradation](/work/projects/pinn-battery/) \
  *Volvo Trucks R&D 路 2022 路 method* *(cross-listed: Battery section)* \
  Where domain physics meets ML - PINN-constrained degradation model prevents physically impossible predictions while enabling real-time inference.

- [Alchemist](https://github.com/ash3spho3nix/Alchemist) \
  *Self-initiated 路 2025 路 tool* \
  Indexes past repositories, extracts architectural patterns, suggests new combinations. Synthesis over generation.

- [Simple RAG Chatbot](https://github.com/ash3spho3nix/RAG-chatbot) \
  *Self-initiated 路 2025 路 tool* \
  First local RAG experiment - document retrieval, context injection, local LLM inference. The seed of the current toolchain.
  {{% /expand %}}
  
---

{{% expand title="鈿欙笍 Mechanics, CFD & Dynamics" %}}

The foundation - structural analysis, contact mechanics, vibration, and fluid dynamics from the first decade of the career. The physics intuition from this work keeps appearing in battery and AI contexts.

- [Tire Modelling: What a Spinning Ring Taught Me About Everything](/work/projects/tire-modelling/) \
  *IIT Kanpur M.Tech 路 2010鈥?011 路 analysis* \
  Standing waves, critical velocity, contact mechanics. The thesis that established the pattern: rotate a structure and everything changes.

- [Piston Rings: Friction, Sealing, and the Physics of Things That Touch](/work/projects/piston-rings/) \
  *TVS Motor Company 路 2012鈥?013 路 analysis* \
  Three simultaneous contact regimes, elastohydrodynamic lubrication, ring flutter. Where the interesting failure always lives at the boundary.
 
- [Magnesium Alloy Wheel Design](/work/projects/magnesium-wheel/) \
  *TVS Motor Company 路 2011鈥?012 路 method + analysis*  \
  Topology optimisation, fatigue under realistic load spectra, thermal analysis. Material substitution is a system problem, not a materials problem.

- [Engine Mounts: Designing Something to Fail Softly](/work/projects/engine-mounts/) \
  *Hero MotoCorp 路 2013鈥?015 路 method* \
  NVH optimisation through stiffness design. Hybrid GA + Nelder-Mead, 15鈥?0% cabin vibration reduction, verified on dynamometer.

- [Radar Modeling for Autonomous Driving](/work/projects/radar-autonomous-driving/) \
  *Mercedes-Benz R&D 路 2016鈥?017 路 analysis* \
  What sensors actually see - beam patterns, clutter, Kalman filter state estimation, and why edge cases aren't edge cases.

- [CFD Fire Modelling: The Inverse Problem Nobody Wants to Solve](/work/projects/cfd-fire-optimization/) \
  *Victoria University, Melbourne 路 2009 路 method* \
  Material property estimation by running the physics model backwards. GA + Nelder-Mead, cross-validated, published.
{{% /expand %}}


---


馃搫 **[Career 鈥?timeline, education, patents 鈫抅(/career/)**

馃敩 **[Beyond the work 鈥?Research Interests 鈫抅(/thinking/research/)** 路 Dynamics, contact mechanics, PINNs, evolutionary algorithms, and the patterns that keep appearing across domains that look unrelated on the surface.

---