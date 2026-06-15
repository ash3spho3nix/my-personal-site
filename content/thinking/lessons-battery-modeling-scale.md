---
title: "The Battery Model That Kept Getting Bigger"
description: "From RC circuits to multi-physics: how a battery model grows from an equivalent circuit into a multi-scale, multi-timescale problem - and why the answer ends up hybrid."
draft: false
---

Like pretty much every battery modelling engineer, I started with RC models. An equivalent circuit, a couple of resistor-capacitor pairs fit to some HPPC data, and you have something that runs in real time and gets you most of the way to a usable SoC estimate. It feels complete, for a while.

Then I went deeper - DFN, SPM, into the actual electrochemistry. And the deeper I went, the more I ran into the practical constraints nobody mentions in the textbook chapter: computational time, cost, and deadlines. A full DFN model is wonderful right up until you need to run it a thousand times for a parameter sweep and don't have a week to do it.

The thing that took me longest to accept was this: most of the time, the failures aren't in the bulk behaviour - they're at the boundary conditions. The cell behaves exactly as the model predicts, right up until you hit the temperature extreme, the C-rate edge, the end-of-life condition - and that's exactly where the model breaks. The interesting physics, and the interesting bugs, both live at the boundary.

That's also where I had to swallow something uncomfortable: there is no single model that explains everything about a battery. I wanted there to be one - one elegant formulation covering SoC, thermal, and aging all at once. There isn't. Different regimes need different models, and pretending otherwise just hides the gaps. It took time to actually accept that, not just agree with it on paper.

As I went further - from performance evaluation, to chemistry, to coupled thermal effects, then thermal-mechanical, then thermal-mechanical-aging - I realised I wasn't looking at "a battery model" anymore. I was looking at a multi-scale, multi-timescale problem sitting across mechanical, electrical, thermal, and chemical engineering at the same time. SEI growth on the order of days, thermal cycling on the order of minutes, calendar aging on the order of months - all coupled, all feeding back into each other.

At that point, the only way forward that didn't collapse under its own complexity was hybrid: use the physics-based model where you understand the mechanism and need it to extrapolate safely, and use a fast surrogate - empirical at first, later a [PINN](/work/projects/pinn-battery/) - to cover the rest within a validated range, without paying the full computational cost every time.

And underneath all of it, the part that's unglamorous but was always there, even when I underrated it early on: data analysis. Every model, however physics-rich, is only as good as how carefully you've looked at the data it's being checked against. The [battery modeling](/work/projects/battery-modeling/) page goes into where each model class actually breaks and why. The [Battery Thermal Model Configurator](/work/projects/battery-thermal-configurator/) and [Virtual Cell Scaling](/work/projects/battery-scaling/) tool are both downstream of the same realisation - that the model you need depends on the question you're asking, and the job is knowing which model to reach for, not building one model to rule them all.

I started with RC because it was simple. I ended up with hybrid because the problem was never simple - it just looked that way from far enough away.

---

## Connects To

*Thinking: [Physics + Machine Learning](/thinking/research/#physics--machine-learning)*
*Project: [Battery Modeling](/work/projects/battery-modeling/)*
*Project: [PINN Battery Degradation](/work/projects/pinn-battery/)*
