---
title: "Teaching a Neural Network the Laws of Battery Decay"
description: "Why a Physics-Informed Neural Network is a better approach to battery degradation modelling than either pure physics or pure data-driven - and the landscape of PINN approaches for Li-ion aging."
date: 2022-06-01
tags: ["battery", "PINN", "machine-learning", "degradation", "physics-informed-ML", "Volvo"]
draft: false
showToc: true
---

## The Quiet Problem Inside Every Battery

If you own a smartphone or an electric vehicle, you have experienced battery degradation. That slow, frustrating decline where a full charge used to last all day and now barely makes it to dinner.

The science behind this is actually fascinating, even if the experience is annoying. Inside every lithium-ion battery, a protective layer called the Solid Electrolyte Interphase (SEI) forms during the first charge. This layer is essential - without it, the battery would destroy itself immediately. But here is the cruel part: the SEI never stops growing. It creeps thicker over time, consuming active lithium that could otherwise be used to power your device.

This leads to an inevitable, exponential decay in capacity. A battery with a Coulombic Efficiency of 99.9% - which sounds excellent - will lose 20% of its capacity in just 148 cycles. The math is unforgiving.

But here is the real problem: predicting exactly how a given battery will degrade is extraordinarily difficult. The process depends on temperature, charge rates, depth of discharge, and a dozen other factors. And the internal chemical reactions follow nonlinear partial differential equations that are expensive to solve.

![PINN battery degradation model overview](/images/batteries-pinn.png)

## The Three Ways People Model Degradation

Before getting into the new approach, it helps to understand what already exists.

**Full physics-based models** (like the Doyle-Fuller-Newman or Single Particle Model) are the gold standard for accuracy. They describe lithium-ion diffusion, electrochemical reactions, and thermal behavior using fundamental physics. The problem? They are computationally intensive. Solving these models in real-time is nearly impossible, and they require detailed material parameters that are often unknown or vary between individual cells.

**Empirical models** take the opposite approach. They ignore the physics entirely and just fit curves to data. This is fast and simple, but it breaks down outside the conditions you trained on. A model trained on data from 25°C will give nonsense predictions at 40°C.

**Pure machine learning models** sit somewhere in the middle. They can learn complex patterns from data without explicit physics. But they need enormous amounts of high-quality training data, and they can produce physically impossible predictions without any warning. A neural network might happily predict that a battery gains capacity after 500 cycles - something that never happens in reality.

Each approach has strengths. Each also has crippling weaknesses.

## What Is a Physics-Informed Neural Network?

A Physics-Informed Neural Network, or PINN, does something that sounds almost too clever to work. It takes a standard neural network and adds the governing physics equations directly into the training process as a penalty term.

Here is how it works. A normal neural network learns by minimizing a loss function that measures how wrong its predictions are compared to training data. A PINN does that too. But it also calculates a second loss term: how badly the prediction violates the underlying partial differential equations that describe battery physics.

The network has to satisfy both. It cannot just memorize the training data. It must produce predictions that are consistent with Fick's laws of diffusion, charge conservation, and the Arrhenius equation that governs temperature-dependent reaction rates.

This is powerful for two reasons. First, the physics acts as a regularizer - it prevents the network from learning nonsense patterns that fit the data by coincidence. Second, the network can make accurate predictions even with sparse training data because the physics fills in the gaps.

Think of it this way: a pure data-driven model is a student who memorizes exam answers. A PINN is a student who learns the underlying principles. When faced with a question they have never seen before, which one performs better?

## How PINNs Compare to Other Techniques

There is active research in related approaches, and it is worth understanding the landscape.

**PyGNN** - Graph Neural Networks for batteries - model the battery as a graph where electrodes, electrolyte, and particles are nodes connected by physical relationships. This is excellent for capturing spatial heterogeneity but less suited for temporal degradation prediction.

**Gaussian Process Regression with physics constraints** has been shown to reduce prediction error from an RMSE of 3.22 to just 0.46 when physics-informed. That is an enormous improvement. But GPs scale poorly with large datasets.

**Electrochemical model surrogate modeling** uses neural networks to approximate expensive physics solvers. This is fast but still requires running the full physics model at least once to generate training data.

PINNs stand apart because they do not need pre-computed simulation data. The physics is embedded directly, so the network learns while simultaneously respecting the laws of electrochemistry. This is sometimes called a "mesh-free" approach - unlike finite element methods that discretize space into thousands of small cells, a PINN can evaluate the solution at any point instantly.

![Battery Modeling](/images/battery/battery_modeling.png)

## What Problem Does This Actually Solve?

The practical problem is this: battery management systems need to predict state of health and remaining useful life in real-time, but the underlying physics is too slow to solve on embedded hardware, and pure data-driven models are not reliable enough.

A well-trained PINN offers the best of both worlds. Once trained, inference is just a fast neural network forward pass - milliseconds on a phone processor. But because the network was trained with physics constraints, its predictions respect thermodynamic limits and known degradation mechanisms.

Recent work like the PINEAPPLE framework has demonstrated that PINNs can infer internal electrochemical parameters - such as lithium-ion diffusion coefficients - directly from voltage-time discharge curves. This is remarkable because those parameters are normally impossible to measure without destroying the battery. And the inference happens in real-time, with accuracy errors below 0.1% and a tenfold speedup over conventional solvers.

Another study showed that integrating partial differential equations into a machine learning model reduced mean squared error from 10.36 to just 0.21 - an improvement of nearly 50 times. That is the difference between useless predictions and actionable insights.

![Battery aging parameters and degradation mechanisms](/images/battery/parameter-battery-ageing.png)

## Where This Is Headed

The field is still young. While PINNs show enormous promise for battery degradation modeling, achieving high accuracy for long-term predictions remains challenging. The nonlinear dynamics of late-stage aging - where lithium plating causes sudden capacity dives - are particularly difficult to capture.

But the direction is clear. Hybrid models that combine physics-based understanding with data-driven flexibility are the future of battery diagnostics. No single approach works perfectly alone. But together, physics and machine learning can achieve what neither can separately: fast, accurate, physically consistent predictions of how a battery will age.

For electric vehicle owners, that means better range estimates. For grid storage operators, that means longer system life through smarter usage. And for the rest of us, it means fewer mornings reaching for a charger and finding the battery unexpectedly empty.

The laws of physics have not changed. But our ability to work with them - rather than around them - just took a significant step forward.

---

## Outcomes

The PINN degradation model was deployed as part of the Volvo Trucks
fleet mobile application. Key results:

- **~90% prediction accuracy** on battery capacity fade across
	the test dataset
- **Inference in seconds** on mobile hardware - no GPU, no
	workstation required
- **Physically consistent predictions**: the physics constraints
	in the loss function prevent capacity recovery artefacts and
	ensure correct temperature sensitivity direction - failure modes
	that appear in pure data-driven models trained on the same data

The hard constraint that shaped the approach: a full electrochemical
ageing model runs in minutes on a workstation. A fleet app needs
a result in under a second on a device with no GPU. PINN was the
only formulation that satisfied both the accuracy requirement and
the deployment constraint simultaneously.

---

*[← Battery Simulation Framework](/work/projects/battery-simulation/) | [Current Limits Generator →](/work/projects/current-limits-generator/)*
