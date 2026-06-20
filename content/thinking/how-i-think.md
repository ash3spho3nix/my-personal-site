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

![Multi-scale modeling comparison - across timescales and length scales](/images/others/multi-scale-modeling-comparison.jpg)

*→ In practice: [Thermal Management System](/work/projects/thermal-management/) · [Battery Simulation Framework](/work/projects/battery-simulation/) · [Battery Modeling](/work/projects/battery-modeling/)*

---

## AI as Reasoning Infrastructure

Machine learning is useful - but the framing matters. The interesting direction isn't AI replacing physical models; it's AI helping reason *about* physical models.

A system that can understand a codebase's dependency structure before modifying it. A surrogate model that respects physical constraints rather than just fitting training data. A debugging assistant that starts from failure modes, not token prediction.

Structure before generation. Understanding before output.

*→ In practice: [Codebase Indexer](/work/projects/codebase-indexer/) · [Hybrid Code Analyzer](/work/projects/hybrid-code-analyzer/) · [Battery Expert AI](/work/projects/battery-ai-systems/)*

---

## Engineering Principles

Seven principles that have stayed consistent across 15 years and six companies. Not aspirational statements — operational rules that have shaped real technical decisions.

{{% expand title="Expand all seven principles →" %}}

#### Infrastructure before instances

The right investment is the system that reduces the cost of all future similar problems, not the perfect solution to the current one. Every simulation framework built — [Battery Thermal Configurator](/work/projects/battery-thermal-configurator/), [Battery Simulation Framework](/work/projects/battery-simulation/), [Current Limits Generator](/work/projects/current-limits-generator/) — was this principle applied. The 60% reduction in model development time at MBRD came from building once correctly, not from solving the same setup problem faster each time.

#### Own the interface

Failures don't live inside well-tested components. They live at the coupling: the CFD-to-ROM boundary, the BMS-to-thermal handoff, the static-to-dynamic analysis correlation. Technical leadership means owning those boundaries - not delegating the integration while keeping the interesting component work.
→ [Thermal Configurator: CFD-ROM interface](/work/projects/battery-thermal-configurator/) · [Hybrid Code Analyzer: static-dynamic correlation](/work/projects/hybrid-code-analyzer/)

#### Physics sets the constraints — engineering works within them

Before committing to any model, architecture, or approach: what does the governing physics actually allow? This question eliminates more bad decisions than any review process. A PINN degradation model isn't just a clever ML approach - it's the only formulation that satisfies both the accuracy requirement and the mobile deployment constraint simultaneously, because the physics of battery aging makes that constraint explicit.
→ [PINN Battery Degradation](/work/projects/pinn-battery/) · [Battery Modeling: where models break](/work/projects/battery-modeling/)

#### Reuse is designed, not discovered

Tools that get reused across programmes and teams are designed for reuse from day one: parameterised inputs, documented assumptions, clear scope boundaries. The [Current Limits Generator](/work/projects/current-limits-generator/) and [Virtual Cell Scaling](/work/projects/battery-scaling/) tool are parameterised - swap the cell's characterisation data and the output regenerates. That property is not an accident.

#### Validate at the boundary, not the centre

Nominal operating conditions reveal little about system quality. Edge cases, failure modes, and boundary transitions are where the real test lives. The [DC box thermal model](/work/projects/dc-box-thermal/) found the design margin problem at the joint near maximum current, not at nominal load. The [tire standing wave analysis](/work/projects/tire-modelling/) is entirely about what happens at the critical velocity - the nominal operating region is uninteresting.

#### Cross-domain fluency is a compound advantage

The engineer who recognises that tire standing wave dynamics and battery electrode diffusion share the same mathematical structure has an analytical toolkit that specialists on either side don't. The [ANN surrogate + Firefly optimisation](/work/projects/front-fender-design/) built for aerodynamics in 2014 is structurally identical to the battery parameter estimation approach in 2023. Same method, different physics. The investment compounds.
→ [Research Interests](/thinking/research/)

#### AI augments reasoning; it does not replace domain knowledge

The most useful AI systems give a domain expert better information to reason from. A local LLM with a structural index of the codebase is more useful than a cloud model with no context. A Physics-Informed Neural Network that respects electrode kinetics is more reliable than a neural network trained on the same data without constraints. The pattern across every AI tool built here: structure before generation.
→ [AI Systems overview](/work/projects/ai-systems/)

{{% /expand %}}

---

## The Pattern

Physics → model → automate → scale.

This has been the repeating cycle across battery modelling, simulation toolchains, and AI systems. The domain changes; the cycle doesn't.

---

*→ Where this leads technically: [Research Interests](/thinking/research/)*
*→ What's still unresolved: [Ideas & Open Questions](/thinking/ideas/)*
