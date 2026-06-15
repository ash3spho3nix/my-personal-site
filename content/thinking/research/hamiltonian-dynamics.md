---
title: "Hamiltonian Dynamics: The Energy Perspective"
description: "Why the energy-based formulation of mechanics reveals structure that force-based analysis misses - and where this keeps showing up."
draft: false
---

Newtonian mechanics starts with forces. Write down all the forces acting on a system, apply F=ma, solve for trajectories. This works. It's also the hardest way to see the structure of a problem.

Hamiltonian mechanics starts with energy. Write the total energy as a function of positions and momenta. Everything else follows from that single function - equations of motion, conserved quantities, stability conditions, symmetries. The formulation is more abstract and considerably more powerful.

The shift isn't just mathematical elegance. It changes what you can see.

---

## What the Hamiltonian Reveals

**Conserved quantities come for free.** Noether's theorem connects symmetries of the Hamiltonian to conservation laws. If the Hamiltonian doesn't depend on time, energy is conserved. If it doesn't depend on a particular coordinate, the corresponding momentum is conserved. You don't derive these - they fall out of the structure.

In practical terms: identifying what's conserved tells you what the long-term behaviour of a system is constrained to. A rotating rigid body with a specific symmetry can only precess in certain ways. A Hamiltonian system can't spontaneously gain or lose energy (in the absence of dissipation). These constraints are the guardrails that make physical intuition reliable.

**Stability analysis becomes geometric.** In phase space - the space of positions and momenta - a Hamiltonian system traces curves of constant energy. Stable equilibria are energy minima; unstable equilibria are saddle points. The stability question becomes a geometric question about the shape of the energy landscape. This is much more tractable than linearising equations of motion and checking eigenvalue signs.

**Canonical transformations simplify problems.** You can change coordinates in Hamiltonian mechanics in a way that preserves the structure of the equations. The right coordinate change can make a complicated problem separable - and a separable problem is solved. This is how action-angle variables work, and it's why perturbation theory in classical mechanics is so powerful.

---

## Where This Has Appeared

**Tire dynamics and standing waves** - The rotating ring problem is naturally formulated in terms of strain energy and kinetic energy. The critical speed at which standing waves form is the condition where energy input from rotation exactly balances the wave's natural dissipation. The Hamiltonian framing makes this condition explicit. [Full writeup →](/work/projects/tire-modelling/)

**Satellite fuel slosh** - Liquid propellant in a satellite tank is a Hamiltonian system (at leading order). Slosh modes are energy modes of the coupled spacecraft-fluid system. Nutational instability occurs when energy can transfer from the spin axis to a transverse mode - a condition visible immediately in the energy formulation, less obvious from force equations.

**Battery electrode dynamics** - This is more speculative, but the coupled diffusion-reaction system in a porous electrode has a variational structure. Whether a full Hamiltonian formulation is tractable and useful for battery modelling is an open question - but the analogy between concentration waves in electrodes and mechanical waves in structures keeps suggesting there's something there.

---

## The Dissipation Problem

Hamiltonian mechanics is, strictly, for conservative systems - no friction, no resistance, no heat generation. Real engineering systems dissipate energy. Batteries have ohmic losses. Engine mounts have rubber hysteresis. Everything interesting involves dissipation.

The extension is Lagrangian mechanics with dissipation functions, or port-Hamiltonian systems for systems with explicit energy ports (inputs and outputs). Port-Hamiltonian formulations are particularly useful for modelling coupled multi-domain systems - thermal-mechanical, electro-chemical - because they make the energy exchange between domains explicit and auditable.

This is relevant for battery pack modelling: a coupled electro-thermal-ageing system is naturally a multi-domain system with energy flowing between electrical, thermal, and chemical subsystems. A port-Hamiltonian formulation would make those energy flows visible and conserved by construction. Most production battery models don't use this formulation - but the ones that will handle multi-physics interactions correctly probably should.

---

## What I'm Still Thinking About

Whether the Hamiltonian perspective on electrode dynamics is genuinely useful or just mathematically interesting. The diffusion equation has a variational formulation; the Butler-Volmer kinetics don't, at least not in the obvious way. Whether the full coupled system admits a clean energy formulation - and whether that formulation would help with parameter estimation, stability analysis, or surrogate construction - is an open question worth pursuing.

*← [Evolution & Optimisation](/thinking/research/evolution/) | → [Contact Mechanics](/thinking/research/contact-mechanics/)*
