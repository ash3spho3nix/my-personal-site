---
title: "Background"
description: "Where the thinking came from - IIT Kanpur, early career, and how 15 years of domain work connects."
draft: false
---

## IIT Kanpur

Mechanical Engineering, B.Tech and M.Tech - 2006 to 2011.

IIT Kanpur's mechanical programme at that time was genuinely heavy on fundamentals. Thermodynamics, fluid mechanics, solid mechanics, vibrations, control theory - taught from first principles, not from software tutorials. The assumption was that if you understood the physics, you could figure out the tools. That assumption has turned out to be correct.

The M.Tech thesis was on *standing waves in high-speed rotating tires* - contact mechanics, wave propagation in pressurised rotating rings, critical velocity analysis. It was the first time a modelling problem had enough depth that the interesting difficulty was in the physics, not just the implementation. That experience set a pattern.

The projects like *Nutational damping of asteroids in free space* and *remaining fuel estimation in spacecraft* which had core mechanics/dynamics physics and modeling/simulation essence for results and visualization, generated a genuine interest in modeling world.

The other formative thing at IIT Kanpur: the culture of building things from scratch before reaching for existing tools. Not as dogma, but as a way of understanding what the tools actually do. Most of the simulation work that came later - and the AI tooling work more recently - runs on that instinct.

---

## Early Career: Foundation in Mechanics

**TVS Motor Company (2011–2013)** was where simulation met production constraints. Structural analysis of chassis components - topology optimisation, fatigue, NVH. The environment was fast and resource-constrained: limited software licenses, tight timelines, engineering decisions made on incomplete information. It built a useful tolerance for working with imperfect models and an instinct for what actually needs to be modelled precisely versus what can be approximated.
The work on chassis components, particularly wheels, helped in understanding how full development cycles works, and how safety factor comes into picture in *real life*.
During my short time spent with TVS Racing team, I was asked to disassemble the full dirt racing bike and then reassemble it and then ride it. *An everlasting impact*.

The ANSYS APDL macros developed there - reducing pre-processing time by ~50% - were the first serious automation work. The insight that *the analysis workflow itself is an engineering problem* has recurred continuously since.

**Hero MotoCorp (2013–2015)** extended this into thermal analysis, contact analysis, NVH and structural dynamics of engine components(Core component of 2 wheeler automotive). Piston, crankshafts, engine case, each of these components are a topic in itself. From working on engine vibrations, considering crankshaft balancing, piston slap motion, to how it affects rider experience, system level thinking developed. Engine mount optimisation was a collaborative effort with team of *Altair* to set-up a simulation technique to estabilish engine mount locations and engine mount material for reduction in vibration transfer to vehicle frame. Vibration analysis, introducing SOPs that reduced review cycles. The first experience of building something repeatable and transferable - not just solving a problem once, but setting up the system so the next engineer could solve it faster.\
The next memorble project was **surrogate modeling for front fendor optimization**, *when Neural networks were not talk of the town, particularly in engineering*.

---

## The Pivot to EV: Mercedes-Benz R&D (2015–2021)

Joining MBRD in 2015 was a pivot from ICE mechanics into EV systems - specifically battery simulation, at a time when the toolchain for battery development in automotive was being enhanced in collaboration wtih German counterparts.

Six years, two roles. The first three years (Senior Engineer) were about enhancing the simulation framework. Starting from vehilce dynamics module, ADAS systems, Lidar systems, and later full vehicle simulation was extended for EV/PHEV/HEV. Each integral component/subsystem was built, validated and integrated, *Charging systems*, *Thermal management system*, *BMS logic*, etc. This was the time, when built competence: electrochemical modelling, thermal simulation, systems modeling(MBSE). Understanding how a Li-ion cell actually works, not just how to use a BMS library.

The second three years (Technology Lead) were about parralel roles- one of technical leadership of building capability at the team level: toolchain architecture, development standards, cross-site collaboration with Daimler in Stuttgart, team growth from 2 to 6 engineers, 5× business growth in the portfolio, and second as an individual contributor, worked on specialized battery modeling toolchain, utilizing and enhancing battery domain knowhow.

The Battery Thermal Model Configurator - 60% reduction in model development time - came out of this period. It was the first project where the goal was explicitly to reduce the cost of doing the *next* project, not just complete the current one. That's a different kind of engineering problem, and a more interesting one.

---
*Covid times*

## Building Teams: Caterpillar and Volvo (2021–2022)

Two back-to-back assignments where the task was establishing battery simulation capability where none existed.

**Caterpillar R&D** - new EV division for heavy construction vehicles. Battery simulation team from scratch: structure, toolchain, development process. Cell testing facility established end-to-end. The domain was different (construction vehicle duty cycles, different thermal and mechanical constraints than passenger cars) but the process of building a team's capability from first principles was familiar.

**Volvo Trucks R&D** - Product Owner for battery, thermal, and SIL/HIL simulation workstreams. Led a 10-person team. The PINN-based degradation model for the fleet mobile app came from here - the first project with a hard real-time inference constraint, which forced a genuinely different modelling approach.

---

## A123 Systems and the Current Work (2022–Present)

Simulation Lead for EMEA at a cell manufacturer - which is a different vantage point from OEM work. The customer is the OEM; the deliverable is simulation supporting cell and pack development for their specific application.

The work is more technically specific (electrochemical focus, cell-to-pack scaling, ageing characterisation) and more commercially embedded (RFI/RFQ cycles, feasibility studies, cost estimation). The self-initiated tools - *Current Limits Generator*, *Virtual Cell Scaling*, *Pack Cost Estimator* - came from gaps in the existing toolchain that were slowing down the commercial process.

---

## The AI Work: Parallel Track

The AI and software tooling work has been running in parallel to the day job since around 2016 - initially PowerShell automation, gradually expanding into Python, machine learning, and more recently local LLM systems.

It's not a career pivot. It's a natural extension of the same instinct that produced the ANSYS macros in 2012: the analysis workflow is an engineering problem, and if you can build better infrastructure for it, you should.

The local LLM focus - running models on-premises, building RAG systems, developing code analysis tools - is deliberate. In the German automotive context, GDPR-driven interest in on-premise AI is real and growing. The capability to deploy AI tooling that doesn't send data to external servers is worth having, both practically and professionally.

[← About](/about/) | [Work & Projects →](/work/)
