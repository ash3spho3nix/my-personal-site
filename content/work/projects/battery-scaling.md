---
title: "Virtual Cell Scaling: When You Don't Have the Cell You Need"
description: "Scaling electrochemical models across capacity, form factor, and chemistry — without starting from scratch every time."
date: 2024-01-15
tags: ["battery", "electrochemistry", "simulation", "A123", "tool"]
draft: false
---

In battery development, the cell you're simulating is rarely the cell you have test data for.

A customer RFI comes in specifying a 60 Ah prismatic. Your characterisation data is for a 40 Ah cylindrical from the same chemistry family. The programme timeline doesn't allow for a full test campaign on the new cell before the simulation deliverable is due. This is the normal situation — not the edge case.

Virtual cell scaling is the tooling built to handle it.

---

## The Problem With Naive Scaling

The instinct is to scale linearly: double the capacity, double the current. This works for some things and breaks badly for others.

What scales linearly with capacity (for the same chemistry and electrode design):
- Total charge storage (by definition)
- Heat generation at the same C-rate
- OCV curve shape (same chemistry, same voltage window)

What doesn't scale linearly:
- **Internal resistance** — depends on electrode thickness, active material loading, and current collector geometry. A larger cell isn't just a smaller cell with more material; the current distribution changes.
- **Thermal response** — larger cells have worse surface-to-volume ratio. Heat generated in the core has further to travel. Thermal gradients emerge that don't exist in smaller cells.
- **Diffusion timescales** — thicker electrodes mean longer solid-phase diffusion paths. The same C-rate on a larger cell with thicker electrodes produces higher local concentration gradients, shifting plating onset and power limits.
- **Ageing mechanisms** — current distribution non-uniformity in larger cells means different local utilisation rates, which means non-uniform aging. The cell doesn't die uniformly.

Miss these and your scaled model is wrong in ways that aren't obvious from nominal discharge curves but matter enormously for safety boundaries and lifetime prediction.

---

## What the Tool Does

The scaling tool takes a validated electrochemical model for a reference cell and applies physics-based transformations to produce a model for a target cell specification.

**Capacity scaling:** Adjusts electrode active material loading and geometric area. Internal resistance is recalculated from the new current density distribution, not assumed proportional.

**Form factor transformation:** Cylindrical → prismatic → pouch involves changes in thermal boundary conditions, current collector geometry, and the mechanical constraints on electrode stack expansion. Each transform has a specific set of adjustments.

**Thickness scaling:** Thicker electrodes are parameterised by adjusting solid-phase diffusion length and tortuosity. The diffusion timescale shifts accordingly — which directly affects the C-rate capability and the onset conditions for lithium plating.

**Thermal recalculation:** Surface area, core-to-surface thermal resistance, and heat capacity are recalculated from the new geometry. The thermal model is not inherited from the reference cell — it's rebuilt for the target geometry.

---

## Where It Sits in the Workflow

The tool feeds the pre-concept simulation phase — before a new cell has been sampled or tested. Given a target specification (chemistry, capacity, form factor), it produces a simulation-ready model that can be used for:

- Pack-level feasibility checks (thermal, electrical)
- Power map generation for the new cell
- Current limit envelope estimation
- Initial ageing projections

It's not a replacement for characterisation data when that data becomes available. It's the bridge that makes simulation possible before characterisation is complete — which, in a fast-moving RFI/RFQ cycle, is most of the time.

---

## The Broader Principle

Physics-based scaling is more reliable than empirical scaling because it separates what changes (geometry, material loading) from what doesn't (fundamental electrochemistry of the active materials). Two cells of the same chemistry but different form factor share their OCV curve, their diffusion coefficient temperature dependence, their reaction rate constants — but not their resistance, thermal response, or rate capability. The tool encodes exactly that separation.

The result is a scaled model that's wrong in quantifiable ways — with known error bounds — rather than wrong in ways you don't know about until the hardware arrives.
