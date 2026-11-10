---
name: credit-risk-regulatory-context
description: Explain expected credit loss, provisioning, IFRS 9, CMN Resolution 4.966 and PD/LGD/EAD while preventing overclaiming from proxy datasets.
---

# Credit Risk and Regulatory Context

## When to use
When writing background, interpreting relevance of macrofinancial indicators, or explaining credit-risk/provisioning models.

## Source hierarchy
Use current official IFRS Foundation material for IFRS 9 and Banco Central do Brasil's consolidated normative text for CMN 4.966. Record access date and exact article/paragraph when citing. Avoid secondary commentary when primary text is available.

## Explain accurately
- IFRS 9: expected credit loss model, probability-weighted outcomes, time value of money and reasonable/supportable past, current and forward-looking information.
- General staging: Stage 1 12-month ECL; Stage 2 lifetime ECL after significant increase in credit risk; Stage 3 lifetime ECL for credit-impaired assets.
- 12-month ECL is the lifetime shortfall resulting from default events possible within the next 12 months, not simply cash shortfalls occurring only during that 12-month period.
- CMN 4.966 is Brazilian regulation for institutions in its scope; do not equate it legally with IFRS 9, although it is aligned with the expected-loss framework.
- PD, LGD and EAD are common risk-model components; `EL ≈ PD × LGD × EAD` is a simplified decomposition, not the entirety of regulatory ECL requirements.
- Regulations establish accounting/risk principles and requirements, not a mandatory neural-network architecture.

## Model examples (illustrative, not mandated)
PD: logistic regression, tree ensembles, gradient boosting, neural classification, survival/time-to-default models. LGD: recovery/workout models, regression/Beta-type approaches, survival models for recovery timing, tree ensembles or neural regression. EAD: exposure/credit-conversion models and regression/sequence approaches. Macroeconomic scenarios: econometric models, time-series methods and neural networks. Explain validation, governance, explainability, calibration and data suitability as essential issues.

## Strict project limitation
The NFCI `Credit` subindex describes aggregate US credit-market conditions. It is not borrower default, delinquency, PD, LGD, EAD, portfolio loss or a Brazilian-bank provision. This study predicts an indicator and may discuss potential contextual relevance only. Never claim direct IFRS 9/CMN 4.966 compliance or LGD estimation.
