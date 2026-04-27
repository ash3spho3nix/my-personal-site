---
title: "Radar Modeling for Autonomous Driving: What Sensors Actually See"
description: "Building a radar sensor model that's honest about what radar can and can't do — and why the interesting problems are in the edge cases."
date: 2024-01-15
tags: ["autonomous-driving", "radar", "sensor-modeling", "perception"]
draft: false
---

Radar is the sensor that autonomous driving can't work without, doesn't fully understand, and frequently underestimates.

Camera gives you texture and color. LiDAR gives you precise geometry. Radar gives you something both of them don't: direct velocity measurement, all-weather reliability, and the ability to see through the annoyances — rain, fog, dust — that blind the other sensors at exactly the moments when you most need to see.

The limitation is angular resolution. A camera pixel corresponds to a very small angle. A radar beam is much wider. Multiple targets at similar range but different angles blur together. This isn't a failure of implementation — it's physics.

---

## What a Radar Model Has to Get Right

Sensor models for simulation exist on a spectrum from "completely fake" (spherical targets with perfect detection) to "physically accurate" (full electromagnetic wave propagation). Production sensor models for autonomous driving sit somewhere in between, aiming to reproduce the behavioral characteristics without the computational cost of first-principles EM simulation.

The key behaviors to capture:

**Beam pattern and angular resolution.** The antenna gain pattern determines which targets are detected at what signal strength depending on their azimuth and elevation. Targets off-beam-center see reduced signal — this has to be in the model, because it's why a pedestrian stepping from behind a car might initially appear dim before becoming a clear detection.

**Clutter.** Rain, road surface, and multipath reflections all generate radar returns that aren't real targets. A model that ignores clutter produces unrealistically clean detection data that trains and tests perception algorithms against a problem that doesn't exist in the field. The interesting edge cases — rain at 60 kph, standing water on motorways — are exactly the conditions where the vehicle needs to be most robust.

**Range-Doppler measurement.** Radar gives you range and radial velocity directly (from the Doppler shift). What it doesn't give you directly is cross-range position. A target at 50m, 30m to the side and a target at 50m, 5m to the side both appear at similar range — and may be in the same beam. The model has to represent this accurately, not pretend the radar has LiDAR-like spatial resolution.

---

## Kalman Filter and the State Estimation Problem

Raw radar detections are noisy. Position estimate uncertainty increases with range; velocity estimates have their own noise floor. The tracking layer — a Kalman filter — takes the sequence of noisy measurements and produces a smoothed state estimate: position, velocity, and their uncertainties.

The interesting part of Kalman filter design for radar is the process model. You're estimating the motion of other vehicles in traffic. Constant-velocity model works for motorway cruise. It fails for intersection scenarios where the target is decelerating, turning, and potentially occluded mid-maneuver. The filter has to handle that gracefully — not collapse into divergence when the measurement update contradicts the prediction.

---

## Where Models Meet Reality

The model was validated against real sensor data from vehicle tests across scenario types: motorway overtake, urban intersection, parking maneuver. The key metric isn't just detection rate — it's the **failure mode distribution**. What does the sensor miss, and why? At what conditions does the tracker lose a target?

That failure characterization matters more than the mean case, because autonomous driving algorithms are only as good as their understanding of sensor failure modes.

---

## Patterns I Keep Seeing

**The edge cases aren't edge cases.** Rain, sensor occlusion, and multi-target scenarios are described as "edge cases" in system specs and tested last. In field operation, they're routine. A sensor model that only handles nominal conditions isn't testing the system that will be deployed.

**Uncertainty propagation matters.** The Kalman filter doesn't just estimate state — it estimates state *and uncertainty*. An algorithm that ignores the uncertainty estimates and just uses the point estimate is throwing away the most operationally relevant information: how much should I trust this detection?
