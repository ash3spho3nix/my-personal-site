---
title: "Battery Simulation Framework: Building the Infrastructure, Not Just the Model"
description: "A standalone simulation framework for battery and BMS development - and a PINN-based degradation model built to run on a mobile app."
date: 2024-01-15
tags: ["battery", "simulation", "PINN", "BMS", "Volvo", "tool"]
draft: false
---

Most battery simulation work happens inside large OEM simulation frameworks - tools with hundreds of subsystems, long setup times, and infrastructure built for full-vehicle analysis. Useful when you need the full vehicle. Counterproductive when you need to iterate quickly on battery-specific questions.

At Volvo Trucks, the problem was clear: the battery and BMS teams needed a simulation environment they could actually use - fast iteration, battery-focused, not dragging a full vehicle model along for every run.

---

## The Standalone Framework

The framework was designed around one principle: **the battery and BMS should be first-class citizens**, not subsystems of a larger model.

![BMS](/images/battery/BMS_functionalities.jpg)

**Architecture:**

- Cell model layer - ECM and simplified P2D, selectable per simulation objective
- Pack model layer - series/parallel topology, cell-to-cell variation, thermal network
- BMS logic layer - SoC/SoH estimation, protection logic, charging control, state machine
- Load profile interface - drive cycle, stationary charging, arbitrary current profiles
- Output layer - automated result extraction, parameterised report generation

The BMS layer was the novel part. Most battery simulation frameworks treat BMS as an afterthought - a simple lookup or a fixed control law. This one implemented the actual BMS logic as a Stateflow-equivalent state machine, so the simulation could reproduce exactly what the real BMS would do under a given load profile. This matters because BMS decisions - derating, balancing, charging cutoffs - are what actually determine real-world battery behaviour in a vehicle.

**What it enabled:**

- SIL testing of BMS software against simulated battery behaviour before hardware was available
- Charging strategy comparison under realistic thermal conditions
- Pack-level performance sensitivity to cell-to-cell variation

---

## The PINN Degradation Model

The second deliverable was harder: a battery degradation model fast enough to run on the Volvo fleet mobile app.

The constraint was severe. A full electrochemical ageing model - SEI growth kinetics, lithium inventory loss, active material degradation - runs in minutes per simulated cycle on a workstation. A mobile app needs a result in under a second, on a device with no GPU and limited memory.

Physics-Informed Neural Networks were the answer.

**The approach:**

A neural network was trained not just on degradation data, but with the governing differential equations for SEI growth and capacity fade embedded in the loss function. The network learns a compressed representation of the ageing dynamics that:

- Satisfies the physical constraints by construction (not just by fitting data that happens to satisfy them)
- Extrapolates more reliably than a pure data-driven model because the physics constrains the solution space
- Runs in milliseconds at inference time

**Training data:** Accelerated ageing test data across temperature, C-rate, and SoC window combinations, augmented with synthetic data generated from the full electrochemical model for operating conditions not covered by physical tests.

**Inputs:** Cumulative Ah throughput, temperature history (summarised as weighted average), average SoC, typical C-rate profile.

**Output:** Remaining capacity fraction, estimated remaining useful life.

**What made it work:** The PINN formulation prevented the network from learning physically impossible degradation trajectories - no capacity recovery, monotonic fade, correct temperature sensitivity direction. A pure neural network trained on the same data would have fit the training distribution but produced nonsensical extrapolations outside it. The physics constraints acted as regularisation with physical meaning.

---

## The Lesson About Infrastructure

The framework and the PINN model are different kinds of deliverables - one is a simulation environment, the other is a deployed model. What they share is that both required thinking about the *infrastructure* first, not just the immediate modelling problem.

A standalone framework that only answers one question isn't a framework - it's a script. A degradation model that only works on a workstation isn't deployable. The engineering decisions that make these useful - modular architecture, BMS-as-first-class-citizen, PINN formulation for mobile constraints - are upstream of the modelling itself.

That's the part that takes longer and gets less credit. It's also the part that determines whether the work is actually used.

---

## Connects To

*Thinking: [Timescale Separation](/thinking/how-i-think/#timescale-separation)*
*Project: [PINN Battery Degradation](/work/projects/pinn-battery/)*
*Project: [Battery Thermal Configurator](/work/projects/battery-thermal-configurator/)*
