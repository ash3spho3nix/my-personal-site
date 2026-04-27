---
title: "CFD Fire Modeling: The Inverse Problem Nobody Wants to Solve"
description: "Estimating wood material properties for fire simulation by running the physics model backwards — what this teaches you about parameter estimation in general."
date: 2024-01-15
tags: ["CFD", "optimization", "inverse-problems", "fire-modeling", "parameter-estimation"]
draft: false
---

Fire safety simulation has a problem that's easier to describe than to solve: the CFD model needs material properties — thermal conductivity, specific heat, ignition temperature, char oxidation rates — but these properties aren't available in standard databases for most real materials, and direct measurement is expensive and often impractical.

The alternative is to go backwards. You have experimental fire test data. You have a CFD model. Find the material properties that make the model match the experiment.

This is an inverse problem, and inverse problems are reliably harder than forward problems.

---

## Why Inverse Problems Are Annoying

In a forward problem, you put parameters in and get a result out. In an inverse problem, you observe the result and want to recover the parameters. The difficulty is that many different parameter sets can produce similar-looking results — the problem is **ill-posed**.

For fire material properties specifically:
- Multiple parameter combinations may fit the same temperature-time curve equally well
- Small changes in some parameters have large effects on model output; others barely matter
- The forward model (CFD) is expensive — you can't just try thousands of random parameter combinations

The approach has to be structured.

---

## The Method

**Sensitivity analysis first.** Before optimizing, figure out which parameters actually matter. Perturb each parameter independently, run the forward CFD model, check how much the output changes. Parameters with low sensitivity can be held fixed at literature values; the optimization focuses on the ones that actually drive the result. This is not just computational efficiency — it's intellectual honesty. Fitting a parameter that the data has no information about is circular.

**Nonlinear optimization.** With the sensitive parameters identified, Nelder-Mead simplex optimization minimized the residual between model output (temperature field, flame front position at measurement points) and experimental data. Nelder-Mead was chosen for its robustness on noisy objective functions — CFD output has numerical noise at the level of measurement uncertainty.

**Cross-validation.** Parameters derived from one test condition were validated against independent tests at different ventilation conditions and sample geometries. This is the check that distinguishes parameter estimation from overfitting.

---

## What Came Out

Material properties for several wood species that produced quantitatively good agreement with fire tests, including temperature evolution and flame spread rate. The results were published and have been used in building fire safety analysis.

More useful than the specific numbers: the methodology is general. Any system where direct parameter measurement is impractical but experimental observables are available is a candidate for this approach. Battery parameter estimation is the same problem with different physics. So is soil constitutive modeling, biological tissue characterization, and polymer creep prediction.

---

## Patterns I Keep Seeing

**The forward model has to be right before inverse methods work.** If the CFD fire model has structural errors — wrong turbulence model, wrong reaction mechanism — fitting parameters to compensate is just building a more elaborate wrong answer. Garbage in, confident garbage out.

**Sensitivity analysis always pays off.** The instinct is to optimize everything simultaneously. The result is always a poorly conditioned problem with non-unique solutions. Start by reducing the dimensionality — figure out what the data actually constrains, and fix everything else. This applies in battery model calibration, thermal model fitting, and structural parameter estimation.

**Publication means the method is verifiable.** The wood property paper matters not because fire safety is my primary domain, but because having a peer-reviewed inverse estimation methodology on record establishes the approach. The physics changes; the estimation logic doesn't.
