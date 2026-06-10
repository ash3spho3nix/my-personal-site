# Designing a Battery Cell That Does Not Exist Yet

## The Problem With "We Need a Different Battery"

Here is a situation that happens more often than you would think. An electric vehicle company has a working battery cell from Supplier A. It is 18650 format, 2500 mAh capacity, tested and reliable. But for their new sedan, they need a larger cell. More range, different shape, different thermal behavior. They ask the supplier: "Can you make us a 21700 version with 4000 mAh?"

The supplier says yes, of course. And then they spend six months and hundreds of thousands of dollars building prototypes, testing them, failing, adjusting, and testing again.

Meanwhile, the engineers have no simulation model to work with. They cannot run thermal analyses. They cannot predict charging behavior. They cannot even start designing the battery pack layout because they do not know exactly how the new cell will behave under load. They are waiting on hardware.

The root problem is this: you cannot create an accurate simulation model for a battery cell without testing that actual cell. But testing requires a physical cell. And building a physical cell requires a design. And designing requires... you see the circle.

## What If You Could Scale a Known Cell Into an Unknown One?

Battery cells are not magic. A larger cell from the same manufacturer, using the same chemistry and similar construction methods, will behave predictably. Not perfectly predictably, but close enough for early-stage simulation.

The relationship between a cell's physical dimensions and its electrical characteristics follows physical laws. Double the electrode area, and capacity scales roughly linearly. Change the aspect ratio, and internal resistance shifts in predictable ways. The thermal behavior changes with surface area to volume ratios.

So here is the idea. You start with a cell you have tested thoroughly. You know its capacity, its internal resistance, its thermal response under different discharge rates. Then you ask: "What if this cell were 20 percent taller and 10 percent wider?" Using physics-based scaling, you can estimate the new cell's behavior without ever building it.

That is what this tool does.

## A Virtual Design Tool for Cells That Do Not Exist Yet

I built a **Virtual Cell Design Tool** that models and scales battery cells using physics-based methods. You feed it data from an existing cell – the kind you have already tested in a lab. Then you tell it what you want: a different capacity, a different form factor, different dimensions.

The tool handles three common battery formats:

- **Cylindrical cells** (like 18650, 21700, 4680). You provide radius and height. The tool calculates new capacity, resistance, and thermal properties based on volume scaling and surface area changes.
- **Prismatic cells** (rectangular, like phone batteries or some EV packs). You provide length, width, and height. The geometry is more complex, so scaling considers electrode stacking and current collector placement.
- **Pouch cells** (flat, flexible, common in consumer electronics). Same approach as prismatic but with different assumptions about packaging thickness and heat dissipation.

The physics behind this is not trivial. The tool accounts for things like:

- **Electrode area scaling** – capacity is roughly proportional to the product of electrode dimensions
- **Current collector resistance** – longer paths mean higher internal resistance
- **Thermal dissipation** – surface area to volume ratio changes with size, affecting cooling needs
- **Tab placement effects** – where the electrical connections attach changes internal current distribution

The output is a simulation-ready model. You can take this virtual cell and plug it into battery management system simulators, thermal models, or vehicle powertrain simulations. No physical prototypes required.

![A diagram showing three battery form factors: cylindrical with radius/height annotations, prismatic with length/width/height, and pouch with similar rectangular dimensions](https://i.imgur.com/battery-form-factors.png)

*The three main battery cell formats: cylindrical, prismatic, and pouch. Each requires different scaling physics.*

## How This Is Different From Existing Tools

If you search for battery modeling software today, you will find plenty of options. Companies like ANSYS, COMSOL, and CD-adapco offer powerful electrochemical simulation tools. But they all share the same requirement: you need detailed material properties, electrode geometries, and often measured data to calibrate the model.

Those tools are for simulating a cell you already have or have already designed in detail.

What does not exist – and this is the gap this project fills – is a tool that takes an existing, tested cell and scales it into a different physical format without requiring new test data. No one has built a simple, physics-based scaler that bridges the gap between "I have data for Cell A" and "I need a model for Cell B that is 30 percent larger."

There are academic papers on scaling laws. There are proprietary internal tools inside big battery manufacturers. There is no open, accessible tool that does this in a straightforward way. That is what I built.

## Future Scope

This tool works well for first-order scaling, but there is plenty of room to grow. Here is what comes next:

**Electrochemical model integration.** Current scaling uses lumped parameters – capacity, resistance, thermal mass. A more sophisticated version would scale the actual electrochemical parameters: diffusion coefficients, reaction rates, porosity. This would enable accurate simulation of things like lithium plating risk or fast-charging behavior.

**Material substitution.** Right now, the tool assumes you keep the same chemistry and construction. The next step is to allow swapping cathode materials (NMC to LFP, for example) while still scaling geometry. That requires capturing material properties separately from cell geometry.

**Calendar life and cycle life estimation.** Larger cells often have different aging characteristics. Thicker electrodes mean longer lithium diffusion paths, which can accelerate degradation at high charge rates. Scaling these aging effects is an open research question.

**Multi-cell pack scaling.** Instead of scaling one cell, imagine scaling an entire battery pack. Given a pack with 100 small cells, what would the equivalent large-format cell pack look like? This is useful for comparing different cell strategies without building either one.

**Validation framework.** The biggest missing piece is a public dataset for validation. If manufacturers published scaled test results (Cell A and Cell B where B is a scaled version of A), the tool's accuracy could be benchmarked properly. This would also help refine the scaling physics.

**Integration with existing simulation tools.** Right now, the output is a standalone model. The future version would export directly to formats used by popular BMS simulators, thermal analysis tools, and vehicle simulation platforms.

## The Takeaway (Or Rather, The Forward Look)

You do not always need to build a physical prototype to start engineering. For battery cells, physics-based scaling works well enough for early-stage design, thermal feasibility studies, and pack layout decisions. The fact that no accessible tool exists for this is surprising, given how common the use case is.

This project is a starting point. The physics are solid. The math works. The next step is making it accurate enough for production engineering decisions. That is the future scope – and it is wide open.