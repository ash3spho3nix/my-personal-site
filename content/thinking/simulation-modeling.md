---
title: "Simulation and Modelling — Fifteen Years of Getting It Wrong and Sometimes Right"
description: "A personal walk through the evolution of my thinking on automotive, battery, thermal, and ageing modelling — the problems that broke my early approaches and the approaches that still surprise me."
draft: false
---

After I joined TVS Motor Company back in 2011, simulation felt straightforward. I would set up ANSYS APDL macros for chassis structural analysis, apply some loads, hit solve, and check if the stresses stayed below the limit. It worked well enough for the day. The models were linear, the questions were simple, and I slept reasonably well.

Then reality started showing its teeth. A minor change in mounting stiffness would invalidate half my assumptions. Physical tests on the prototype would reveal behaviours the model had never seen. I began to realise I wasn't really modelling the system — I was modelling an idealised version of it, and the gap mattered more than I wanted to admit.

By the time I reached Mercedes-Benz R&D India in 2015 the problems had scaled up. Full-vehicle simulation frameworks demanded coupling between structural dynamics, thermal systems, and early controls logic. I spent weeks stitching together tools for one vehicle programme only to watch the whole chain fall apart when the next variant arrived with different cooling architecture. The frustration was familiar: the physics was there, but making it useful across teams felt like fighting entropy with duct tape.

![Full vehicle thermal simulation mesh](/images/full-vehicle-thermal-simulation.jpg)

That experience pushed me deeper into battery work. At Caterpillar and later Volvo Trucks I started wrestling with true multi-physics problems. Automotive modelling had prepared me for large systems, but battery packs operate at a different level of tightness. Heat generation changes local electrochemistry, which changes resistance, which changes heat again — a feedback loop that laughs at loosely coupled solvers.

I remember one particular study on fast-charging behaviour. The initial physics-based model looked clean on paper. Run it for a few cycles and the predicted temperature gradients seemed manageable. Reality, informed by cell testing, showed something much uglier. Local hotspots were accelerating ageing in ways the base model simply couldn't capture. I had to go back and rebuild the thermal-electrochemical coupling from scratch.

That led me into ageing modelling properly. Early attempts used simple empirical fits. They were fast but terrifyingly brittle outside the training data. One temperature excursion and the prediction would drift into nonsense. So I started exploring physics-informed approaches.

At Volvo Trucks in 2022 we built a PINN-based degradation model on top of the existing framework. The results were startling — ~90% accuracy on capacity fade for NMC cells under mixed drive-cycle and charging conditions, running in seconds instead of hours. For the first time I could run hundreds of pack-level ageing scenarios as part of a vehicle trade-off study instead of waiting for HPC slots. It felt like a genuine leap.

![Battery aging degradation curves](/images/battery-aging-degradation-curves.jpg)

But of course the new technique brought its own headaches. The PINN was brilliant at interpolation and fast evaluation, yet it still struggled with strong extrapolation — new cell chemistries or abuse conditions required careful retraining and validation. Interpretability remained partial. Engineers reviewing the results wanted to understand *why* the model predicted a particular lithium plating onset, not just that it did. Pure data-driven methods hit the same wall even harder.

This pushed me toward hybrid physics-based modelling. I started combining pseudo-3D electro-thermal models with reduced-order ageing mechanisms. At A123 Systems the work on pseudo-3D pack models for Porsche motorsport applications and multiple RFQs showed the value. We could capture current distribution, tab heating, and cell-to-cell variation without going to full 3D CFD for every study. The models became tools for current limits generation and virtual cell scaling — practical, traceable outputs that design teams could actually use.

![Battery pack electro-thermal simulation](/images/battery-pack-electro-thermal.jpg)

Thermal modelling has been a constant companion through all this. Automotive thermal systems are large and somewhat forgiving — cabin comfort, under-hood temperatures, radiator sizing. Battery thermal management is the opposite: tight margins, strong two-way coupling, and safety implications that keep you honest. I have spent more nights than I care to count debugging why a seemingly minor change in cooling channel geometry produced runaway temperature predictions in one scenario but not another.

The manufacturing variation piece surprised me most. Early models treated every cell as identical. In practice, electrode coating thickness scatter, electrolyte distribution differences, and contact resistance all create ensembles of behaviour. Once I started incorporating stochastic elements into the framework the confidence in long-term pack predictions improved noticeably. It wasn't flashy, but it mattered when we had to stand behind the numbers for customer programmes.

Along the way I have explored quite a few side paths. OpenFOAM-based battery simulators for detailed CFD when the pseudo-3D layer isn't enough. Hybrid code analyzers to understand and modernise legacy simulation codebases. Even RAG systems to query years of past simulation reports and decisions. Each new technique solves one class of problems while exposing the next layer of complexity.

What keeps pulling me forward is the realisation that simulation modelling is never finished. Every new chemistry — LFP versus NMC, solid-state experiments, silicon anodes — rewrites parts of the rulebook. The questions from vehicle teams keep evolving too: not just "will it work?" but "how do we optimise this pack for both performance and circular economy requirements?"

I still catch myself falling into old traps — over-simplifying the coupling, trusting a model a little too far outside its validation envelope, or under-investing in the infrastructure that makes the models reusable. But the pattern is clearer now. The real leverage comes not from any single solver or algorithm, but from building systems where new physics can be plugged in, where results stay traceable, and where the accumulated knowledge compounds instead of evaporating between projects.

Fifteen years in, simulation modelling still feels like a conversation with the physical world. Sometimes the world answers clearly. More often it forces me to ask better questions and build better tools to hear the answer.

---

## Connects To

*Project: [Battery Simulation Framework](/work/projects/battery-simulation-framework/)*  
*Project: [PINN Degradation Modelling](/work/projects/pinn-degradation-modelling/)*  
*Thinking: [How I Think About Engineering Systems](/thinking/how-i-think/)*