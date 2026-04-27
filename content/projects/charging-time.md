---
title: "Charging Time: Why 80% Is Not Half the Problem"
description: "The CC-CV charging profile and why the last 20% of a charge takes disproportionately long — and why that matters for thermal management."
date: 2024-01-15
tags: ["battery", "charging", "thermal", "EV", "BMS"]
draft: false
---

The EV marketing spec says "0 to 80% in 22 minutes." It rarely says how long 80 to 100% takes. The omission is deliberate — and it reveals something fundamental about how lithium-ion cells actually work.

---

## The CC-CV Profile and Why the Transition Matters

Lithium-ion charging follows a two-phase profile, not because someone decided it was a good idea, but because cell physics demands it.

**Constant Current (CC) phase:** You push current in at a fixed rate. The cell voltage rises as SoC increases. This phase is efficient — you're putting energy into the cell at the maximum rate the chemistry allows without exceeding the voltage limit or driving electrochemical side reactions.

**Constant Voltage (CV) phase:** Once the voltage hits the upper cutoff, you hold it there and let current taper off. The cell is approaching full charge; the concentration gradients at the electrodes are large; the driving force for lithium intercalation is dropping. Current declines exponentially. You're waiting for the chemistry to catch up.

The transition from CC to CV happens around 80% SoC for a typical NMC cell under normal charging rates. The CV tail — that last 20% — takes roughly the same time as the CC phase got you to 80%, depending on cutoff criteria. That's why the marketing spec stops at 80%.

---

## C-Rate and Its Discontents

Higher C-rate means faster CC phase. Simple. Except:

- Higher current generates more heat (I²R losses increase quadratically with current)
- Higher current drives larger overpotential at the electrodes, approaching the conditions for lithium plating
- The CV tail doesn't get proportionally shorter — it stays approximately the same because the cutoff current is fixed, not relative to charge rate

So a 2C charge compared to 1C gets you to 80% roughly twice as fast, but produces 4× the heat, increases plating risk, and doesn't substantially accelerate the final 20%.

The practical result: fast charging protocols are thermal management problems as much as electrochemical ones. The cell doesn't care how fast you can push current in isolation — it cares what temperature it reaches, because temperature determines degradation rate, which determines lifetime.

---

## What the Model Captures

The charging time model integrates:

- OCV-SoC curve (determines when the voltage cutoff is reached)
- Internal resistance as a function of SoC and temperature (sets the voltage drop under load)
- Thermal model (predicts cell temperature evolution during charge)
- Current derating logic (reduces charge current if temperature or SoC-based overpotential limits are approached)

The thermal coupling is important. A cell that starts warm charges faster in CC (lower resistance) but reaches thermal limits sooner, triggering current derating that extends the tail. A cold cell has high resistance, takes longer to reach the CC-to-CV transition, but may never hit thermal limits. The total charge time is non-monotonic with temperature — there's an optimal starting temperature that minimizes total charge time.

---

## Patterns I Keep Seeing

**Non-linear systems have optimal operating points that aren't at the extremes.** Cold isn't better and hot isn't better — there's a temperature window that minimizes charge time while staying within degradation limits. This shows up in battery design constantly: the "push it harder" instinct hits diminishing returns or reversals.

**The constraint you're not thinking about is the one that bites.** Fast charging seems like a current problem. It's actually a thermal problem. The electrochemistry sets the current limit; the thermal system determines whether you can sustain it.
