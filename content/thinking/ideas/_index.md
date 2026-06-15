---
title: "Ideas & Open Questions"
description: "Half-formed hypotheses, active explorations, and questions that keep coming back."
draft: false
---

These are the things that haven't resolved yet.

Not finished projects - those live in [Work](/work/). Not settled positions - those are in [Research Interests](/thinking/research/). This is the frontier: directions being actively explored, hypotheses not yet tested, questions that keep surfacing from different angles.

---

## 🤖 AI-Assisted Simulation Debugging

Current simulation workflows fail silently or produce results that look plausible but are physically wrong. The debugging process is manual, slow, and heavily dependent on domain expertise that isn't transferable.

The open question: can an AI system reason about *why* a simulation is failing - not just flag that it diverged, but identify which physical assumption broke down, at what point, under what conditions?

This requires the system to understand the governing equations, the numerical scheme, and the coupling between subsystems. Not just pattern matching on error messages.

**Status:** Actively exploring. [Codebase Indexer](https://github.com/ash3spho3nix/Codebase_Indexer) and [Hybrid Code Analyzer](https://github.com/ash3spho3nix/hybrid_code_analyser) are partial steps in this direction - but for code, not simulation models. Early concept documented in [AI-Assisted Simulation Debugger](/work/projects/ai-simulation-debugger/).

---

## 🔬 Symbolic Physics + AI Reasoning

Can a system discover governing equations from data - not just fit a curve to observations, but recover the actual differential equation structure?

Symbolic regression (e.g., PySR, DSO) makes partial progress here. Physics-informed neural networks enforce known equations but don't discover new ones. The gap: systems that can propose physically plausible structures, test them against data, and refine.

The deeper question is whether human-imposed structure is always necessary, or whether the right inductive biases can make equation discovery tractable.

**Status:** Reading. No implementation yet. Early framing in progress.

---

## ⚡ Multi-Timescale Battery Aging

Battery aging operates across at least three coupled timescales: SEI growth (hours to days), thermal cycling effects (seconds to minutes), and calendar degradation (months to years). Most models handle one timescale well and approximate the others.

The open question: is there a formulation that handles all three without either becoming computationally intractable or losing physical fidelity at the fast timescales?

Possible directions: hierarchical models with timescale-separated solvers, reduced-order models trained on high-fidelity data at each timescale, or a Hamiltonian formulation that makes the conserved quantities at each scale explicit.

**Status:** This is a live problem in the day job. No clean solution yet.

---

## 🧠 Code Understanding as Engineering Reasoning

Most AI coding tools treat code as text. The more interesting framing: treat a codebase as a dynamical system - with state (data structures), transitions (function calls), invariants (type constraints, physical units), and failure modes (edge cases, dependency breaks).

Engineering reasoning about code would look like: identify the timescales, find the coupling, understand what drives instability. The same instinct as physical modeling.

**Status:** The [Codebase Indexer](https://github.com/ash3spho3nix/Codebase_Indexer) explores part of this - dependency graph analysis, dead code detection, impact propagation. Early stage.

---

[← Research Interests](/thinking/research/) | [How I Think](/thinking/how-i-think/)
