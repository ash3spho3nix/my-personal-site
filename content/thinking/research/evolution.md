---
title: "Evolutionary Algorithms: Optimisation as a Physical Principle"
description: "Why genetic algorithms and related methods are interesting beyond their practical utility - and where they've shown up across different domains."
draft: false
---

The principle of least action says physical systems evolve along paths that extremise a quantity - usually energy or action. Fermat's principle in optics, Hamilton's principle in mechanics, entropy maximisation in thermodynamics. Optimisation isn't something humans impose on physical systems. It's what physical systems do.

Evolutionary algorithms are a computational expression of the same logic. Selection pressure, variation, inheritance - applied to a population of candidate solutions rather than a population of organisms. The algorithm doesn't know the answer; it discovers it by the same mechanism nature uses.

This isn't just a philosophical observation. It has practical consequences for how you design and apply these methods.

---

## Where These Have Appeared

**CFD fire modelling** - Genetic algorithm for material property estimation. The inverse problem: find the parameter set that makes the forward model match experimental data. GA explored the space globally, Nelder-Mead refined locally. The combination worked where gradient-based methods failed because the objective function was non-convex and noisy. [Full writeup →](/work/projects/cfd-fire-optimization/)

**Aerodynamic optimisation** - Firefly algorithm over an ANN surrogate for fender drag minimisation. Population-based search over a continuous design space, with attraction toward better solutions. The surrogate decoupled the expensive CFD evaluation from the search. [Full writeup →](/work/projects/front-fender-design/)

**Engine mount optimisation** - Hybrid GA + Nelder-Mead for NVH reduction. Multi-objective: minimise cabin vibration across multiple frequency ranges simultaneously. The Pareto front gave engineering options rather than a single answer. [Full writeup →](/work/projects/engine-mounts/)

**Battery parameter estimation** - Differential evolution for ECM parameter identification from pulse characterisation data. The parameter space has correlations and local minima that trip gradient methods. Evolutionary search with bounded parameters found physically plausible solutions consistently.

---

## Why Population-Based Search Works Here

These problems share a structure: non-convex objective, multiple local optima, moderate dimensionality (5–30 parameters), expensive or noisy function evaluations.

Gradient-based methods fail or get stuck because they follow the local slope - which leads to the nearest minimum, not the best one. Population-based methods maintain diversity explicitly, which is what allows escape from local optima.

The cost is evaluations. A gradient method might converge in 50 function evaluations. A GA might need 5,000. This is only acceptable if each evaluation is cheap (surrogate model) or if the problem is important enough to justify the compute. In engineering design, it's often the latter.

---

## The Interesting Connection to Degradation

Battery degradation is, in a specific sense, an evolutionary process. The electrode microstructure changes over cycles - SEI grows, active material cracks, lithium inventory redistributes. Each cycle is a selection event: configurations that dissipate less energy, distribute stress more uniformly, resist side reactions better - survive longer.

This isn't just metaphor. The mathematical structure of degradation models (differential equations with state-dependent rates, irreversible transitions, path dependence) has direct analogues in population genetics. Whether that analogy produces useful modelling insights or just interesting observation is an open question.

---

## What I'm Still Thinking About

Multi-objective evolutionary optimisation produces Pareto fronts, not single answers. This is actually more honest than single-objective optimisation - most real engineering problems have genuine tradeoffs, and pretending there's one right answer obscures the decision that has to be made. The challenge is presenting a Pareto front to an engineer or a customer in a way that helps them make the decision rather than overwhelming them with options.

The other open question: can evolutionary search be made sample-efficient enough to work directly against expensive physics simulations, without the surrogate intermediary? Bayesian optimisation approaches this from a different angle - using a probabilistic surrogate that also quantifies uncertainty. The combination of Bayesian optimisation with physical constraints is an area worth watching.

*← [Research Interests](/thinking/research/) | → [Hamiltonian Dynamics](/thinking/research/hamiltonian-dynamics/)*
