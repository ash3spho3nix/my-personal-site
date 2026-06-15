---
title: "Tools, Projects, Frameworks - and the Difference That Took Me Years to See"
description: "Why building a simulation framework is a fundamentally different job than building a tool or finishing a project - and how that realisation has repeated itself across battery and AI tooling."
draft: false
---

After I joined Mercedes-Benz R&D in 2015, I started to understand what a toolchain actually is, and how different it is from a tool, and how different a tool is from a project.

A project solves one problem, once. A tool automates a repeated task - automation on steroids. A framework is a different beast altogether. My first real assignment there wasn't a tool or a project. It was a simulation framework: multiple vehicle architecture configurations, a library of powertrain components, base models built individually for each component, and then variants assembled from those base models to cover the full product range - from concept to production.

Building a framework needs a vision before you write the first line of code, before you wire the first signal in a Simulink model. Reusability, modularity, scalability - words I had, until then, only seen in computer science articles, not in anything I'd worked on. It also needs a different kind of empathy: you have to imagine yourself as the user who will never read the tutorial, who gets irritated when the GUI freezes mid-run, who just wants to drop in a new vehicle variant and get a result without touching the internals.

That last part came from actually going and asking the R&D users what they struggled with - what they avoided, what they quietly worked around because raising it felt like more effort than the workaround. Each round of that fed back into the framework: a function added here, a friction point removed there, the whole thing becoming a little more invisible each time.

Somewhere in that process, my role changed without anyone announcing it. I was no longer an R&D engineer working on projects and new tech. I was the person who enabled other R&D engineers to do that more efficiently. The work moved from "solve this problem" to "make this class of problem easier to solve, for everyone, repeatedly."

That distinction has stuck with me, and I keep re-discovering it in new domains.

At Volvo, the [Battery Simulation Framework](/work/projects/battery-simulation/) was the same move applied to batteries: not another battery model, but an environment where the cell model, the pack topology, and the BMS logic could each be swapped independently - with the BMS treated as a first-class citizen instead of an afterthought bolted onto someone else's vehicle model.

At A123, the [Current Limits Generator](/work/projects/current-limits-generator/) and [Virtual Cell Scaling](/work/projects/battery-scaling/) tool follow the same logic. Both are parameterised - a new cell's characterisation data goes in, a new envelope or scaled model comes out, without anyone touching the underlying physics each time.

And the AI tooling I've been building on the side - the [Codebase Indexer](/work/projects/codebase-indexer/) and [Hybrid Code Analyzer](/work/projects/hybrid-code-analyzer/) - is the same instinct pointed at a new problem. Not "fix this bug" or "analyse this one repo," but build the structural layer that makes every future analysis of any repo faster.

The pattern hasn't changed since 2015. Find the thing that will need doing again and again, and build *that*, instead of the thing sitting directly in front of you. The hard part has never really been the engineering - it's noticing, early enough to matter, that you're looking at a framework problem dressed up as a project.

---

## Connects To

*Thinking: [Infrastructure Before Instances](/about/#engineering-principles)*
*Project: [Battery Simulation Framework](/work/projects/battery-simulation/)*
*Project: [Codebase Indexer](/work/projects/codebase-indexer/)*
