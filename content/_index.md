---
title: Home
---

I build the infrastructure that makes hard engineering problems tractable — not just solve the immediate instance.

15 years across automotive R&D: from tyre contact mechanics at IIT Kanpur through ICE simulation, into battery electrochemistry and EV systems, and now into AI tooling for engineering workflows. The domain keeps changing. The pattern — **physics first, then model, then automate, then scale** — hasn't.

Currently: Simulation Lead (EMEA) at A123 Systems. Electrochemical modelling, cell-to-pack scaling, OEM requirements translation across DE/IN/CN teams. Parallel track: local LLM tooling for GDPR-compliant on-premise AI — a genuine differentiator in the German automotive market.

Two patents. Three simulation teams built from scratch. One consistent instinct: **the interesting physics lives at the boundary, not the nominal operating point.**

---

## Selected Impact

| | |
|---|---|
| 🔋 | **60% reduction** in battery thermal model development time — CFD-to-ROM pipeline, Mercedes-Benz R&D |
| ⚙️ | **3 simulation teams built from scratch** across Mercedes-Benz, Volvo Trucks, and A123 Systems |
| 🧪 | **96% experimental accuracy** on DC-DC converter thermal model — design margin identified pre-hardware |
| 📐 | **12% drag reduction** on motorcycle fender — ANN surrogate + Firefly algorithm, 10× faster than CFD-in-loop |
| 🤖 | **On-premise AI toolchain** for GDPR-compliant engineering workflows — codebase reasoning, RAG, simulation debugging |
| 📄 | **2 patents** — EV cooling system (Inventor's Award, 2016) and energy recapture from suspension (2017) |
| 🏎️ | **15–20% cabin vibration reduction** — hybrid GA + Nelder-Mead mount optimisation, verified on dynamometer |

---

## AI + Physics Tooling

The German automotive context has a hard constraint: engineering IP and simulation data cannot leave the building. Cloud AI tools are not an option for the interesting work.

This pushed me to build a local AI stack — LM Studio + Ollama + FAISS — that runs entirely on-premise. The tools I've built on top of it:

- **[Codebase Indexer](/work/projects/codebase-indexer/)** — structural repository understanding (dependency graphs, importance scoring, semantic retrieval) for AI agents that need to *reason about* a codebase, not just generate code into it
- **[Hybrid Code Analyzer](/work/projects/hybrid-code-analyzer/)** — static + dynamic analysis pipeline; correlates runtime failures with structural importance to identify where failures actually propagate from
- **[Battery Expert AI](/work/projects/ai-systems/)** — domain-specific assistant for battery electrochemistry and simulation, running locally
- **[RAG Chatbot](https://github.com/ash3spho3nix/RAG-chatbot)** — document retrieval + local LLM inference over engineering notes and papers

The design philosophy across all of these: **structure before generation**. A reasoning system that understands what it's working with produces better outputs than one that generates fluently without comprehension.

[Full AI tooling overview →](/work/projects/ai-systems/)

---

## What I Work On

**Battery & Electrochemistry** — electrochemical modelling (DFN, SPM, ECM), thermal simulation, ageing models, cell-to-pack scaling, OEM deliverables. Five companies deep in this domain across 10 years.

**Simulation Infrastructure** — frameworks and toolchains that reduce the cost of the *next* project, not just complete the current one. ANSYS, OpenFOAM, MATLAB/Simulink, Python. The APDL macros from 2012 and the FAISS indexer from 2023 are the same kind of move.

**Vehicle Dynamics & NVH** — tyre contact mechanics, engine mounts, structural vibration. The physics intuition from the M.Tech thesis in rotating structures keeps appearing in new contexts.

**On-premise AI for Engineering** — codebase reasoning, simulation debugging infrastructure, domain-specific RAG. Built for environments where data sovereignty is a hard constraint.

---

**→ [Work & Projects](/work/)** — engineering projects, AI tools, patents

**→ [Thinking](/thinking/)** — how I approach problems, research interests, open questions

**→ [About](/about/)** — background, arc, what I'm working on

**→ [Notes](/notes/)** — shorter observations
