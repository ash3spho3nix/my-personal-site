---
title: "About"
description: "15 years from IIT Kanpur to battery electrochemistry to on-premise AI tooling — the arc, the instincts, the work."
build:
  list: never
  render: always
---

## Career Snapshot

| Period | Role | Company |
| --- | --- | --- |
| 2022–Present | Simulation Lead, EMEA | A123 Systems GmbH, Germany |
| 2022 | Lead – Simulation & Analysis (Sr. Manager) | Volvo Trucks R&D, India |
| 2021–2022 | Performance Engineer | Caterpillar R&D, India |
| 2015–2021 | Technology Lead / Senior Engineer | Mercedes-Benz R&D, India |
| 2013–2015 | Deputy Manager, R&D | Hero MotoCorp, India |
| 2011–2013 | Member, R&D | TVS Motor Company, India |
| 2009 | Research Intern | Victoria University, Melbourne |

[Full experience and CV →](/work/experience/)

---

## Patents

- **Cooling system for fuel cell vehicle/EV** — Inventor's Award, Mercedes-Benz, 2016
- **Efficient power recapturing from vehicle suspension** — Mercedes-Benz, 2017

---

## The Short Version

Mechanical engineer by training (IIT Kanpur, M.Tech + B.Tech). 15 years across automotive R&D — ICE systems, EV modeling & simulation, battery electrochemistry, and now ML/AI tooling for engineering workflows.

The consistent thread: build the infrastructure that makes the problem tractable. Not just solve the current instance, but reduce the cost of solving the next one.

Currently: **Sr. Product Engineer(Simulation Lead, EMEA)** at A123 Systems (Germany). Translate OEM requirements into simulation scope across DE/IN/CN teams, deliver final validation authority for EMEA deliverables.

**2 patents · 3 simulation teams built · 10+ engineers led · 60% model dev time reduction at MBRDI**

---

## What I Actually Do

- Design **12 V/48 V battery systems** from OEM requirements- preconcept phase to sample phase until project finalization.
- Responsible for managing **simulation related requirements** across all 12 V/48 V battery projects.
- Build and validate **battery simulation models** — electrochemical (DFN, SPM), thermal, ageing, full-pack
- Design **simulation frameworks and toolchains** that reduce the cost of the *next* project, not just complete the current one
- Develop **AI-assisted engineering tools** — codebase reasoning, local RAG, simulation debugging infrastructure
- Bridge **OEM requirements and global simulation teams** across cultural and technical boundaries

---

## Education

**M.Tech & B.Tech — Mechanical Engineering, IIT Kanpur** (2006–2011)

M.Tech Thesis: *Critical Velocity and Standing Waves in High-Speed Rotating Tires*

The thesis established the instinct that's recurred ever since: the interesting physics lives at the boundary — at the critical velocity where wave propagation onset changes the contact mechanics, at the SoC where lithium plating onset shifts the safety limit, at the dependency that breaks the codebase when modified.

---

## Engineering Principles

Seven principles that have stayed consistent across 15 years and six
companies. Not aspirational statements — operational rules that have
shaped real technical decisions.

---

**Infrastructure before instances**
The right investment is the system that reduces the cost of all
future similar problems, not the perfect solution to the current one.
Every simulation framework built — [Battery Thermal Configurator](/work/projects/battery-thermal-configurator/),
[Battery Simulation Framework](/work/projects/battery-simulation/),
[Current Limits Generator](/work/projects/current-limits-generator/)
— was this principle applied. The 60% reduction in model development
time at MBRD came from building once correctly, not from solving
the same setup problem faster each time.

---

**Own the interface**
Failures don't live inside well-tested components. They live at
the coupling: the CFD-to-ROM boundary, the BMS-to-thermal handoff,
the static-to-dynamic analysis correlation. Technical leadership
means owning those boundaries — not delegating the integration while
keeping the interesting component work.
→ [Thermal Configurator: CFD-ROM interface](/work/projects/battery-thermal-configurator/)
→ [Hybrid Code Analyzer: static-dynamic correlation](/work/projects/hybrid-code-analyzer/)

---

**Physics sets the constraints — engineering works within them**
Before committing to any model, architecture, or approach: what does
the governing physics actually allow? This question eliminates more
bad decisions than any review process. A PINN degradation model
isn't just a clever ML approach — it's the only formulation that
satisfies both the accuracy requirement and the mobile deployment
constraint simultaneously, because the physics of battery aging makes
that constraint explicit.
→ [PINN Battery Degradation](/work/projects/pinn-battery/)
→ [Battery Modeling: where models break](/work/projects/battery-modeling/)

---

**Reuse is designed, not discovered**
Tools that get reused across programmes and teams are designed for
reuse from day one: parameterised inputs, documented assumptions,
clear scope boundaries. The [Current Limits Generator](/work/projects/current-limits-generator/)
and [Virtual Cell Scaling](/work/projects/battery-scaling/) tool
are parameterised — swap the cell's characterisation data and the
output regenerates. That property is not an accident.

---

**Validate at the boundary, not the centre**
Nominal operating conditions reveal little about system quality.
Edge cases, failure modes, and boundary transitions are where the
real test lives. The [DC box thermal model](/work/projects/dc-box-thermal/)
found the design margin problem at the joint near maximum current,
not at nominal load. The [tire standing wave analysis](/work/projects/tire-modelling/)
is entirely about what happens at the critical velocity — the nominal
operating region is uninteresting.

---

**Cross-domain fluency is a compound advantage**
The engineer who recognises that tire standing wave dynamics and
battery electrode diffusion share the same mathematical structure
has an analytical toolkit that specialists on either side don't.
The [ANN surrogate + Firefly optimisation](/work/projects/front-fender-design/)
built for aerodynamics in 2014 is structurally identical to the
battery parameter estimation approach in 2023. Same method, different
physics. The investment compounds.
→ [Thinking: Research Interests](/thinking/research/)

---

**AI augments reasoning; it does not replace domain knowledge**
The most useful AI systems give a domain expert better information
to reason from. A local LLM with a structural index of the codebase
is more useful than a cloud model with no context. A Physics-Informed
Neural Network that respects electrode kinetics is more reliable
than a neural network trained on the same data without constraints.
The pattern across every AI tool built here: structure before
generation.
→ [AI Systems overview](/work/projects/ai-systems/)
→ [How I Think: AI as Reasoning Infrastructure](/thinking/how-i-think/)

---

## The Arc

IIT Kanpur → TVS → Hero → Mercedes-Benz → Caterpillar → Volvo → A123. Not a straight line, but a consistent pattern: go deep into a domain, build the infrastructure, then move to a harder problem.

The AI tooling work isn't a career pivot — it's the same instinct applied to the analysis workflow itself. The ANSYS APDL macros that cut pre-processing time by 50% in 2012 and the FAISS-based codebase indexer in 2023 are the same kind of move: the workflow is an engineering problem, and it should be treated like one.

[Full background and story →](/about/background/)

---

## Outside Work

Engineering trains you to decompose problems. Painting trains you to *see* what's actually there, not what you think is there. These aren't the same skill, and the second one is harder.

Sketchbooks, observational drawing, occasional writing. The habits that slow down perception in a useful way — the same attention that catches a model that "should work" but doesn't.

Fountain pen user. Analog watch collector. Reader who can't accept black boxes.

> *"You can't draw what you don't see. You can't model what you don't understand."*
