---
title: "Debugging a Black Box vs Debugging Physics"
description: "The real argument for physics-based models isn't accuracy - it's that they carry the signature of the physics inside them, which is what makes them debuggable."
draft: false
---

Every few years, someone makes the case that black-box models - neural networks, mostly - are good enough now that physics-based models are a relic. I've heard versions of this argument since the early ECM-vs-data-driven debates, and I've never found it convincing, for a reason that has nothing to do with accuracy: debuggability.

A physics-based model carries the signature of the physics inside it. When it goes wrong - predicts the wrong voltage sag, the wrong temperature rise, the wrong plating onset - you can trace that error back to a term in an equation. Is the diffusion coefficient wrong? Is a heat generation contribution missing? Is a boundary condition mis-specified? The error has an address, and you can go look at what's there.

A black-box model that goes wrong gives you a number and nothing else. The "address" of the error is somewhere across a few million weights, and there's no equation to point at. You can retrain, add data, try a different architecture - but you're debugging by guessing, not by reasoning.

![It doesn't work, why? It works, why?](/images/memes/it-doesnt-work-why-it-works-why.png)

This isn't an argument that black-box models are useless - they're clearly not, and the [PINN](/work/projects/pinn-battery/) work I've done makes the opposite point: the combination is often better than either alone. The PINN's value comes precisely from keeping part of that physics signature. The loss function still has the governing equations in it, so when the model produces something physically impossible - a battery gaining capacity, say - that's a signal, not just noise. There's still something to point at.

That's the real distinction, and it isn't "physics vs ML." It's whether the model has a signature that lets you reason about *why* it's wrong. A pure empirical ECM, fit to data with no physical grounding in its parameters, has the same debugging problem as a neural network - even though it isn't "AI," it's just a curve fit wearing an equivalent-circuit costume. The [battery modeling](/work/projects/battery-modeling/) page gets into this directly: an ECM whose RC parameters are *derived* from electrochemical first principles extrapolates correctly, because the parameters mean something physically. An ECM whose parameters are just fit to characterisation data doesn't - for the same reason a neural network doesn't. No signature, nothing to check against.

So when I reach for a physics-based model first, it isn't nostalgia, and it isn't distrust of ML. It's that I want to be able to open the hood when something goes wrong - and a model grounded in the governing equations, even a reduced or hybrid one, is the only kind that lets you do that.

---

## Connects To

*Thinking: [Physics First](/thinking/how-i-think/#physics-first)*
*Project: [Battery Modeling](/work/projects/battery-modeling/)*
*Project: [PINN Battery Degradation](/work/projects/pinn-battery/)*
