---
title: "Front Fender Drag Optimization: Why Running CFD in a Loop Is a Bad Idea"
description: "Surrogate-based aerodynamic optimization using ANN and firefly algorithm — decoupling the simulation from the search."
date: 2024-01-15
tags: ["optimization", "aerodynamics", "ANN", "meta-modeling", "CFD"]
draft: false
---

The naive approach to aerodynamic optimization is obvious: run CFD, check drag, adjust geometry, run CFD again. Repeat until satisfied.

This works if you have a few design variables and a lot of patience. It doesn't work if you have a high-dimensional design space, a CFD solver that takes hours per run, and an optimization algorithm that wants to query thousands of points.

The solution is to decouple the two problems.

---

## The Core Idea: Surrogate Modeling

Instead of asking the CFD solver at every optimization step, you build a fast approximation — a surrogate model — from a limited set of CFD runs. The optimizer then works against the surrogate, not the simulator.

This changes the problem structure completely:

- CFD runs: expensive, slow, done once (or a few times for refinement)
- Surrogate queries: essentially free, done thousands of times
- Final validation: back to CFD, for the top candidates only

The surrogate here was an Artificial Neural Network trained on a design-of-experiments (DoE) set of CFD runs spanning the fender geometry parameter space. The ANN learned the mapping from geometry parameters → drag coefficient.

---

## The Optimization Loop

With a fast surrogate, you can afford population-based search methods that would be completely impractical with real CFD.

The firefly algorithm was used: a swarm-based metaheuristic where "brighter" (lower drag) individuals attract others. The swarm converges toward low-drag regions of the design space through a combination of attraction and random perturbation.

Why firefly over GA or PSO? Honestly, the choice of evolutionary algorithm matters less than the quality of the surrogate. With a well-trained ANN, any reasonable population-based optimizer finds good solutions. The firefly algorithm worked well and has continuous parameter updates that suit continuous design spaces.

The loop:
1. DoE sampling of geometry space
2. CFD runs for each sample point
3. Train ANN on (geometry, drag) pairs
4. Firefly optimization on ANN
5. Re-evaluate top candidates with CFD
6. (Optional) augment training data, retrain, repeat

---

## Results

12% drag reduction on the front fender geometry. More importantly: **10× speedup** versus traditional CFD-in-loop optimization, because the expensive evaluations were replaced by fast surrogate queries.

The drag reduction is real but specific to this vehicle and this geometry. The method generalizes — which is the more important result.

---

## The Broader Lesson: Physics Simulations Are Datasets

Once you accept that a physics simulation is just a very expensive function evaluation, the whole landscape of machine learning techniques becomes applicable. You have input (design parameters), output (performance metric), and a (very slow) black-box function connecting them. Any supervised learning approach that can approximate that function enables you to explore the space cheaply.

The same logic applies to:
- Structural optimization (FEA → surrogate)
- Battery parameter estimation (electrochemical model → surrogate)
- Thermal design (CFD → surrogate for coolant routing)

The pattern is: **build physical understanding, generate simulation data, train a fast model, search aggressively, validate top results with physics.**

---

## Patterns I Keep Seeing

**Decoupling expensive evaluation from search is almost always worth it.** Any time you're running a slow simulation inside a loop, ask whether a surrogate could replace it. The upfront cost of training data is usually worth the speedup.

**The surrogate must know its limits.** An ANN trained on a bounded DoE space is unreliable outside that space. The optimizer will cheerfully exploit regions where the surrogate is wrong if you don't constrain it. This is why validation against true CFD at the end is not optional.
