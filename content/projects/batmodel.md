---
title: Battery ECM Modeling (batModel)
---

## ⚡ Overview  

Equivalent Circuit Model (ECM) for battery behavior with parameter estimation pipeline.  

---

## 🔬 Key Work  

- Modeled OCV, resistance, and RC parameters  
- Parameters as function of:
  - SoC  
  - temperature  
  - C-rate  

---

## ⚙️ Method  

Two-stage optimization:
1. Genetic Algorithm → global search  
2. Local optimization → refinement  

---

## 🧠 Insight  

Early example of:
> physics structure + data-driven parameter fitting  

---

## 🚀 Extensions  

- Bayesian optimization  
- PINNs for parameter learning  