---
title: "Virtual Cell Scaling: When You Don't Have the Cell You Need"
description: "Scaling electrochemical models across capacity, form factor, and chemistry — without starting from scratch every time."
date: 2024-01-15
tags: ["battery", "electrochemistry", "simulation", "A123", "tool"]
draft: false
showToc: true
---

## The Situation Nobody Talks About

Here is a situation that happens more often than you would think in battery development. An EV company has a working cell from Supplier A — tested, characterised, reliable. But for their next programme, they need a different cell: larger capacity, different form factor, different thermal profile. They ask the supplier: "Can you make us a 21700 version with 4000 mAh from the same chemistry?"

The supplier says yes. And then six months and significant prototype cost later, the engineers still have no simulation model to work with in the meantime. They cannot run thermal analyses. They cannot predict charging behaviour. They cannot start designing the pack layout because they don't know exactly how the new cell will behave under load.

The root problem: you cannot create an accurate simulation model for a battery cell without test data for that cell. But testing requires a physical cell. And building a physical cell requires a design. And designing requires a model. The circle.

In a fast-moving RFI/RFQ cycle — which is most of the time at a cell manufacturer — this is the normal situation, not the edge case. Virtual cell scaling is the tooling built to handle it.

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

![Cell-to-pack scaling — parameter transformation](/images/cell_to_pack-scaling.png)

---

## What the Tool Does

The scaling tool takes a validated electrochemical model for a reference cell and applies physics-based transformations to produce a model for a target cell specification.

**Capacity scaling:** Adjusts electrode active material loading and geometric area. Internal resistance is recalculated from the new current density distribution, not assumed proportional.

**Form factor transformation:** Cylindrical → prismatic → pouch involves changes in thermal boundary conditions, current collector geometry, and the mechanical constraints on electrode stack expansion. The tool handles all three common formats — 18650/21700/4680 cylindrical, prismatic, and pouch — with format-specific scaling physics for each.

**Thickness scaling:** Thicker electrodes are parameterised by adjusting solid-phase diffusion length and tortuosity. The diffusion timescale shifts accordingly — which directly affects C-rate capability and the onset conditions for lithium plating.

**Thermal recalculation:** Surface area, core-to-surface thermal resistance, and heat capacity are recalculated from the new geometry. The thermal model is not inherited from the reference cell — it's rebuilt for the target geometry.

---

## How This Is Different From Existing Tools

Battery simulation software exists. ANSYS, COMSOL, and CD-adapco all offer electrochemical simulation tools. But they all share the same requirement: you need detailed material properties, electrode geometries, and often measured data to calibrate the model. Those tools are for simulating a cell you already have or have already designed in detail.

What doesn't exist — and this is the gap the tool fills — is a scaler that takes an existing, tested cell and produces a model for a physically different cell without requiring new test data. There are academic papers on scaling laws. There are proprietary internal tools inside large battery manufacturers. There is no open, accessible tool that does this in a straightforward workflow.

The tool is parameterised: swap in a different cell's characterisation data and the scaled model regenerates for that cell. This is intentional — at a cell manufacturer working across multiple OEM customers and cell chemistries, that flexibility is not optional.

---

## Where It Sits in the Workflow

The tool feeds the pre-concept simulation phase — before a new cell has been sampled or tested. Given a target specification (chemistry, capacity, form factor), it produces a simulation-ready model that can be used for:

- Pack-level feasibility checks (thermal, electrical)
- Power map generation for the new cell
- Current limit envelope estimation
- Initial ageing projections

It's not a replacement for characterisation data when that data becomes available. It's the bridge that makes simulation possible before characterisation is complete — which, in a fast-moving RFI/RFQ cycle, is most of the time.

---

## Where This Has Been Used

The scaling methodology has been applied across multiple OEM
RFI/RFQ requirements at A123 Systems — covering capacity scaling,
form factor transformation, and chemistry-adjacent scaling where
full re-characterisation was not available within the commercial
timeline.

Two consistent results: the scaled model is significantly faster to
produce than a model built from scratch (no new characterisation
campaign required), and the physics-based parameter transformations
produce more accurate extrapolations than empirical scaling rules,
particularly at temperature extremes and high C-rates where the
naive approach breaks down most visibly.

---

## Future Scope

The tool works well for first-order scaling. Where it can grow:

**Electrochemical model integration.** Current scaling uses lumped parameters — capacity, resistance, thermal mass. A more sophisticated version would scale the actual electrochemical parameters: diffusion coefficients, reaction rates, porosity. This would enable accurate simulation of things like lithium plating risk and fast-charging limits on the scaled cell.

**Material substitution.** Right now, the tool assumes the same chemistry and construction. The next step is allowing cathode material swaps (NMC to LFP, for example) while still scaling geometry — capturing material properties separately from cell geometry.

**Calendar and cycle life estimation.** Larger cells often have different aging characteristics. Thicker electrodes mean longer lithium diffusion paths, which can accelerate degradation at high charge rates. Scaling these aging effects is an open research problem.

**Multi-cell pack scaling.** Instead of scaling one cell, scale an entire pack concept. Given a pack with 100 small cells, what would the equivalent large-format cell pack look like? Useful for comparing different cell strategies without building either one.

**Integration with simulation toolchain.** Export directly to formats used by BMS simulators, thermal analysis tools, and vehicle simulation platforms — rather than a standalone output.

---

## The Broader Principle

Physics-based scaling is more reliable than empirical scaling because it separates what changes (geometry, material loading) from what doesn't (fundamental electrochemistry of the active materials). Two cells of the same chemistry but different form factor share their OCV curve, their diffusion coefficient temperature dependence, their reaction rate constants — but not their resistance, thermal response, or rate capability. The tool encodes exactly that separation.

The result is a scaled model that's wrong in quantifiable ways — with known error bounds — rather than wrong in ways you don't know about until the hardware arrives.

[← Work](/work/) | [Current Limits Generator →](/work/projects/current-limits-generator/)
