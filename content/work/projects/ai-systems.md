---
title: "AI Systems: Building Tools That Understand Code, Not Just Generate It"
description: "A different class of AI system — focused on reasoning about structure and behavior, not producing tokens."
date: 2024-01-15
tags: ["AI", "systems", "codebase-analysis", "agents", "tools"]
draft: false
---

Most AI coding tools are generation engines. You describe what you want, they produce code. This works for isolated functions, boilerplate, and anything where the context fits in a prompt.

It breaks down when the problem is understanding an existing system — navigating a codebase you didn't write, debugging a failure with no obvious error message, figuring out why something that worked in isolation fails in the larger system. These are comprehension problems, not generation problems. And comprehension requires structure, not just pattern matching.

The projects here are attempts to build the infrastructure for that kind of AI-assisted reasoning.

---

## Codebase Indexer

**Problem:** Large codebases are opaque. You can read files sequentially, but you can't reason about dependency structure, identify which modules are most central, or understand what a change to one function propagates to — not without analysis tooling.

**What it does:** Static analysis of Python codebases — symbol extraction, dependency graph construction, importance scoring (which functions are most connected / most depended on), and a query layer for asking structural questions. The output isn't just a file listing; it's a map of the codebase that an agent can use to navigate and reason.

**Why it matters for agents:** An agent with access to a structural index can form a plan before touching code. It can identify the right entry point, understand the blast radius of a change, and avoid making edits that look locally correct but break something three layers up. This is the difference between an agent that codes and an agent that understands.

---

## Hybrid Code Analyzer

**The gap:** Static analysis tells you about structure. It doesn't tell you what happens when the code actually runs — which paths get executed, what types actually flow through, which imports fail in the current environment.

**What it does:** Combines static analysis (AST-level) with dynamic analysis (runtime instrumentation). Running both together reveals things neither can find alone: a function that statically looks correct but fails on specific input types, an import chain that works in the dev environment but not in production, a path that's never exercised by tests and contains a latent bug.

**The key design decision:** The Indexer and Analyzer are deliberately kept separate tools. They produce different information — structural vs. behavioral — and combining them into a single pass loses the ability to correlate them independently. Run both, compare outputs, find the discrepancies. That's where bugs live.

---

## Alchemist

**Premise:** Most useful new projects aren't built from scratch. They're combinations of existing systems with a structural twist. The knowledge is already there — in past projects, existing tools, documented patterns. The gap is synthesis.

**What it does:** Indexes past local repositories, extracts architectural patterns and component types, and suggests new project ideas by identifying potentially valuable combinations. Not "write code for me" — "here's what you've built before and here's what that suggests you could build next."

**Why this is different from an LLM chat:** It operates on your actual code history, not on general training data. The suggestions are grounded in what you've actually built and what the real structural relationships between those components are.

---

## Battery Current Limit Generator (NMC)

**Problem:** BMS protection limits — maximum charge and discharge current as a function of SoC, temperature, SoH, and time — are typically lookup tables populated by empirical testing. Testing is slow and expensive; the coverage of the operating envelope is always incomplete.

**What it does:** Physics-based offline engine that generates the full 5D operating envelope using Butler-Volmer kinetics for plating onset detection, coupled Arrhenius aging side reactions, and lumped thermal modeling. Produces a lookup table the BMS can use in real-time, generated from first principles rather than pure empiricism.

**Why it matters:** A physics-derived current limit knows *why* the limit is where it is. When the aging model updates the SoH estimate, the current limit surface updates accordingly. When you want to understand why the limit tightened, the model can tell you which mechanism is driving it. That traceability is what distinguishes a physics-based approach from a calibrated lookup.

---

## The Pattern Across These Projects

All of these systems share a design philosophy: **structure before generation**. Understanding before output. Whether it's a codebase, a battery operating envelope, or a project portfolio — the goal is to build representations that preserve the structural relationships, and then reason from those representations.

This is the direction AI-assisted engineering should go: not replacing the engineer's judgment, but giving it better information to work from.
