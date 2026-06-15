---
title: "How I Think"
description: "The operating principles - physics-first, failure-driven, structure before generation."
draft: false
---

## Physics First

Most problems I work on start with the governing equations, not the data. Before reaching for a model or a tool, I try to understand: what forces are acting, what constraints exist, where the system can fail, and how it behaves at its boundaries.

This isn't dogma - it's practical. A model built from physical understanding generalises better, degrades more predictably, and can tell you *why* it's wrong when it fails. A model built from curve-fitting can't.

*→ In practice: [Battery Modeling](/work/projects/battery-modeling/) · [PINN Battery Degradation](/work/projects/pinn-battery/) · [CFD Fire Optimization](/work/projects/cfd-fire-optimization/)*

---

## Failure Reveals Structure

Stable, well-behaved systems are degenerate - they all look similar at equilibrium. It's the instabilities, edge cases, and nonlinear transitions that reveal the actual structure underneath.

This shows up everywhere: a battery at the edge of lithium plating, a simulation that diverges at a specific timestep, a codebase that breaks when a specific dependency is modified. In each case, the failure tells you something about the system that nominal operation hides.

The instinct is to treat failures as the most informative data points, not as noise to be avoided.

*→ In practice: [Hybrid Code Analyzer](/work/projects/hybrid-code-analyzer/) · [DC Box Thermal](/work/projects/dc-box-thermal/) · [Battery Thermal Configurator](/work/projects/battery-thermal-configurator/)*

---

## Timescale Separation

Most complex systems operate across multiple timescales simultaneously. In battery modelling: charge transport (milliseconds), thermal response (seconds to minutes), ageing (hours to years). In software: function execution (microseconds), test cycles (minutes), architectural evolution (months).

Recognising which timescales are coupled and which can be treated independently is usually the key modelling decision. It's what determines whether a lumped approximation is valid, or whether you need a full coupled simulation.

*→ In practice: [Thermal Management System](/work/projects/thermal-management/) · [Battery Simulation Framework](/work/projects/battery-simulation/) · [Battery Modeling](/work/projects/battery-modeling/)*

---

## AI as Reasoning Infrastructure

Machine learning is useful - but the framing matters. The interesting direction isn't AI replacing physical models; it's AI helping reason *about* physical models.

A system that can understand a codebase's dependency structure before modifying it. A surrogate model that respects physical constraints rather than just fitting training data. A debugging assistant that starts from failure modes, not token prediction.

Structure before generation. Understanding before output.

*→ In practice: [Codebase Indexer](/work/projects/codebase-indexer/) · [Hybrid Code Analyzer](/work/projects/hybrid-code-analyzer/) · [Battery Expert AI](/work/projects/battery-ai-systems/)*

---

## The Pattern

Physics → model → automate → scale.

This has been the repeating cycle across battery modelling, simulation toolchains, and AI systems. The domain changes; the cycle doesn't.

*→ See also: [Engineering Principles →](/about/) · [Research Interests →](/thinking/research/)*

---

*→ Where this leads technically: [Research Interests](/thinking/research/)*
*→ What's still unresolved: [Ideas & Open Questions](/thinking/ideas/)*
