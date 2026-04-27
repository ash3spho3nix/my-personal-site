---
title: "Research Interests"
description: "Mechanics, dynamics, optimization, simulation — and the question of why systems behave the way they do."
draft: false
---

Most of what I find genuinely interesting in engineering sits at the intersection of two things: the governing equations that describe a system, and the behavior that emerges when you push that system toward its limits.

The stable, well-behaved middle of the operating envelope is well understood and usually boring. The interesting physics — the instabilities, the mode transitions, the nonlinear couplings — lives at the boundaries. That's been a consistent thread across tires, piston rings, batteries, and AI systems. Different physics, same instinct.

---

## Dynamics — The Core

Mechanics and dynamics are the foundation. Not just in the "I studied this in university" sense, but in the sense that the dynamic perspective keeps producing useful insight in domains where people don't usually apply it.

A battery electrode is a porous medium with coupled diffusion and reaction — it has wave-like concentration dynamics. A software codebase has dependency propagation patterns that behave like coupled oscillators. The specific equations differ; the structure of the analysis — find the modes, identify the coupling, understand what drives instability — transfers.

Sub-areas of active interest:

- **[Contact Mechanics](/research/contact-mechanics/)** — Local interactions with global consequences
- **[Hamiltonian Dynamics](/research/hamiltonian-dynamics/)** — Energy-based formulation that reveals conserved quantities and stability structure
- Rigid body rotation and gyroscopic effects
- Rotational instabilities (nutation, rattleback, standing waves)

---

## Evolution — Adaptation and Optimization

The principle of least action says physical systems evolve along paths that minimize (or extremize) some quantity. This shows up everywhere: Fermat's principle in optics, Hamilton's principle in mechanics, the second law in thermodynamics. Optimization isn't something humans impose on systems — it's what systems do.

This perspective makes evolutionary algorithms interesting beyond their practical utility. Genetic algorithms don't just solve engineering optimization problems — they're a computational expression of the same selection pressure logic that shapes physical systems.

Areas of interest:

- [Biologically-inspired algorithms](/research/evolution/) — GA, PSO, differential evolution
- Multi-objective optimization and Pareto frontiers
- Evolutionary computation for inverse problems
- Degradation as a form of system evolution — how does a battery electrode "age" and what determines the trajectory?

---

## Simulation and Mathematical Modeling

A simulation is a hypothesis in executable form. The discipline is building hypotheses that are precise enough to be wrong.

Vague models can't be falsified — they have too many degrees of freedom to ever definitively fail. A good simulation model has specific, checkable predictions. It tells you not just what will happen, but why, and therefore what would have to be different for a different outcome.

The domains I work in:
- Electrochemical systems — where continuum equations meet discrete reaction sites
- Thermal dynamics — coupling between energy storage, transport, and generation
- Fluid-structure interaction — especially rotating and deformable structures
- Multi-body dynamics — mechanical systems with multiple coupled degrees of freedom

---

## Physics + Machine Learning

The synthesis I keep coming back to: physics-based models are interpretable but expensive and parameter-hungry. Data-driven models are fast and flexible but opaque and fragile outside their training distribution.

The interesting approaches aren't choosing one over the other. They're about using physics to structure the machine learning problem:

- Physics-informed neural networks (PINNs) — enforce governing equations in the loss function
- Reduced-order modeling via dimensionality reduction — build fast surrogates that respect physical constraints
- Parameter estimation as inverse problem — use ML to invert from observations to physical parameters
- Learned surrogates for expensive simulations — generate physics-consistent training data, then approximate with a fast model

The goal isn't to replace physical understanding with data. It's to use data to fill the gaps where direct measurement or exact computation isn't feasible.

---

## Patterns I Keep Seeing

**Instability reveals structure.** Stable equilibria are degenerate — they look the same until you disturb them. Instabilities are specific: each one has a mechanism, a threshold condition, a characteristic signature. Understanding why a system goes unstable tells you more about the underlying physics than studying its nominal behavior.

**Timescale separation is an engineering tool.** Fast dynamics (RC in ECM, contact patch evolution in tires) can often be treated as quasi-static from the slow dynamics perspective. This is why lumped models work — they exploit the separation of timescales to reduce the model order. Knowing which timescales are coupled and which aren't is the key modeling decision.

**The math often transfers.** Diffusion equations, wave equations, stability analysis — the same mathematical structures appear in acoustics, electrochemistry, heat transfer, and mechanics. This isn't a coincidence; it reflects shared underlying physics. Recognizing the isomorphism between a new problem and a solved one is a significant part of engineering intuition.

---

## Things I'm Still Trying to Understand

- Whether the analogy between battery electrode diffusion dynamics and acoustic wave propagation is just a mathematical coincidence or points to something deeper
- How to properly handle the multi-timescale problem in battery aging — SEI growth (hours-days) coupled to thermal cycling (seconds-minutes) coupled to calendar degradation (months-years)
- Whether symbolic regression and physics-informed ML can actually discover governing equations from data, or whether human-imposed structure is always necessary
