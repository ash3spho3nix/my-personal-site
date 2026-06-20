---

title: "Battery Simulation Framework — Why I Built a Framework Instead of Buying a Tool"
description: "Building battery models is difficult. Building battery simulation infrastructure is a completely different problem."
tags: ["battery", "battery modeling", "Pack" , "Modules", "Vehicle", "electrochemistry", "simulation", "BMS", "DFN", "ECM", "aging"]
draft: false
showToc: true
math: true
------------

![](/images/battery/battery-framework-hero.svg)

After spending years working in battery simulation across Mercedes-Benz, Caterpillar, Volvo Trucks and later A123 Systems, I slowly realised something that was not obvious to me in the beginning.

Most battery engineers think they are building battery models. In reality, they are usually building battery infrastructure. **The distinction sounds subtle.**

It isn't. A battery model answers a question. A battery simulation framework enables an organisation to ask thousands of questions. *Those are completely different engineering problems.*

When people hear "battery simulation", they often imagine electrochemistry equations, thermal models, SOC estimation algorithms or ageing models. All of those are important, but they represent only a small part of the overall challenge.

The real challenge begins when those models need to interact with vehicle simulations, BMS software, test data pipelines, manufacturing data, calibration workflows and engineering processes spread across multiple teams.

That is where individual tools start breaking down. That is where frameworks become necessary.

## The Day I Stopped Thinking About Cells

Early in my battery career I was fascinated by cell physics.

* Diffusion.
* Lithium transport.
* Reaction kinetics.

The famous DFN model. The equations themselves are beautiful.

Lithium concentration inside active particles follows:

$$
\frac{\partial c_s}{\partial t}
=

\frac{D_s}{r^2}
\frac{\partial}{\partial r}
\left(
r^2
\frac{\partial c_s}{\partial r}
\right)
$$


Electrolyte transport introduces another set of coupled PDEs. Potential distributions add another layer.

Then thermal behaviour joins the party. Then degradation. Then side reactions. Then manufacturing variations.

A battery cell quickly becomes one of the most complicated components inside a vehicle.

The natural instinct is to keep adding physics. The deeper I went, however, the more I realised something interesting.

*Vehicle engineers rarely ask:*

*"What is the lithium concentration distribution at 60% depth inside the negative electrode?"*

They ask:

*"Can this vehicle finish the drive cycle?"*

*"Will fast charging damage the battery?"*

*"What happens after eight years?"*

*"Will cooling be sufficient during towing?"*

*"How much performance will be available at -20°C?"*

These are system questions, not cell questions. That shift fundamentally changed how I viewed battery simulation.

## Accuracy Is Not The Goal

This statement usually makes battery modellers uncomfortable. Accuracy matters, but accuracy alone is not the goal. **Usability matters, Computational speed matters, Scalability matters, Automation matters, Integration matters.**

Consider a DFN model. It captures electrochemical behaviour with remarkable fidelity. For cell development work, it is invaluable.

For running a complete vehicle simulation containing climate systems, motor models, drivetrain models, control systems and multiple drive cycles, it quickly becomes impractical. A single simulation taking several hours might be acceptable in research. It becomes useless inside an optimisation loop requiring 50,000 evaluations.

This creates a constant engineering tension:

**How much physics can we afford?**

*Not financially. Computationally.*

Most of battery simulation is really a resource allocation problem disguised as a modelling problem. At one end sits the full electrochemical model. At the other end sits an equivalent circuit model:

$$
V_t = OCV(SOC) - I R_0 - V_{RC}
$$

The ECM ignores enormous amounts of physics. Yet automotive companies continue using it.

#### Why?

Because sometimes an answer in 10 milliseconds is more valuable than a slightly better answer in 10 minutes. The best model depends on the question being asked. That is a systems engineering decision, not a modelling decision.

## The Battery Is Not A Cell

![Battery Pack Modeling](/images/battery/cell_to_pack.png)

Another realisation arrived much later. Most battery models focus on individual cells, most real-world problems do not. A vehicle does not operate a cell, it operates a pack; the pack contains modules, modules contain cells, the pack includes cooling systems.

* Contactors.
* Sensors.
* Fuses.
* Wiring.
* Controllers.
* Safety systems.
* BMS logic.
* Diagnostic algorithms.
* Manufacturing variations.
* Thermal gradients.
* Ageing differences.

The battery is not one system. It is a collection of interacting systems. This creates an interesting challenge.

The electrochemist wants cell accuracy.

The controls engineer wants execution speed.

The thermal engineer wants temperature prediction.

The BMS engineer wants real-time deployability.

The validation engineer wants correlation against test data.

Everyone is correct. Everyone wants something different.

A framework exists to reconcile those competing requirements.

## Electro-Thermal-Ageing Coupling Changes Everything

One of the biggest mistakes I see in battery discussions is treating electrical, thermal and ageing behaviour as independent domains. They are not, they continuously influence each other.

Current generates heat. Heat changes electrochemical behaviour. Electrochemical behaviour influences degradation. Degradation increases resistance. Resistance generates more heat. The system becomes strongly coupled.

A simplified thermal balance appears innocent:

$$
mC_p\frac{dT}{dt}
=================

## Q_{gen}

Q_{loss}
$$

But hidden inside that equation are effects that influence battery lifetime, charging speed, power capability and safety margins. The challenge is not writing the equation. The challenge is connecting that equation to every other model surrounding it.

*This is why I eventually became more interested in architecture than modelling.*

The coupling became more important than the individual models.

## Safety Changes The Entire Design Philosophy

A battery is not just an energy storage device. It is a safety-critical system, that single fact changes everything. A thermal model is no longer simply predicting temperature. It is protecting hardware. An SOC estimator is not merely estimating charge. It is influencing power limits. An SOH estimator is not merely tracking degradation. It is influencing warranty decisions worth millions. Errors propagate. Bad assumptions propagate. Incorrect calibration propagates. The consequences are real. This forces battery simulation to operate differently from many other engineering domains. 

**The framework must support traceability, Validation, Versioning, Data lineage, Correlation workflows, Reproducibility.**

Suddenly software architecture becomes as important as electrochemistry.


![Value chain of lithium-ion batteries for vehicles](/images/battery/Value-chain-of-lithium-ion-batteries-for-vehicles.png)

## Building A Tool Versus Building A Framework

This was probably the biggest lesson I learned. A tool solves a task. A framework supports a process.

Suppose an engineer manually imports test data, cleans it, identifies parameters, updates a model and generates a report. You can automate that task. Many organisations stop there.

The deeper question is:

What created that task in the first place?

Can the entire workflow become connected?

Can test data automatically feed analytics pipelines?

Can analytics automatically generate model parameters?

Can parameters automatically update simulations?

Can simulations automatically generate validation reports?

Can those reports automatically support calibration decisions?

At that point you are no longer automating tasks.

You are automating engineering processes.

That is an entirely different level of thinking.

The battery framework eventually became less about models and more about information flow. Test data became inputs. Models became transformations. Analytics became feedback loops. The architecture became the product.

## What The Framework Eventually Became

Over time the framework started absorbing everything around it.

* Battery test analytics.
* Cell characterisation.
* SOC estimation.
* SOH estimation.
* Thermal simulation.
* Ageing prediction.
* Drive cycles.
* Climate scenarios.
* Pack scaling.
* BMS logic.
* Vehicle integration.
* Manufacturing variability.
* Validation workflows.

What emerged was not a battery model. **It was a battery operating system.**

A common environment where multiple engineering disciplines could work using the same underlying infrastructure.

Ironically, the individual models changed repeatedly. New chemistries appeared. New ageing mechanisms appeared. New vehicle requirements appeared. The architecture remained. That was the real asset.

## Looking Back

When I started, I thought battery simulation was about solving equations. Years later, I think it is mostly about managing complexity. The equations matter. The physics matters. The chemistry matters. But those are only components inside a much larger system. The real challenge is creating an environment where electrochemistry, thermal behaviour, ageing, controls, manufacturing, testing and vehicle integration can coexist without becoming an unmanageable mess. That is why I eventually stopped thinking in terms of battery models. 

I started thinking in terms of battery infrastructure.

A model answers a question. A framework enables an organisation to keep answering new questions long after the original model becomes obsolete. The models evolved. The requirements evolved. The vehicles evolved. The framework survived.

And that, more than any individual equation, is what made it valuable.