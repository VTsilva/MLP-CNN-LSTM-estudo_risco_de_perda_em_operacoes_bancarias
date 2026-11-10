---
name: academic-notebook-storytelling
description: Build a professional academic notebook in which every analysis has a purpose, every result is interpreted, and every decision follows from evidence.
---

# Academic Notebook Storytelling

## Core rule
No code cell, table or graph exists only for decoration. Every analytical block must form an evidence chain.

## Required structure around an analytical block
**Before the code (Markdown):**
1. Business/scientific question being answered.
2. Why the question matters to the research objective.
3. What the code calculates and key methodological assumptions.
4. What outcome would change the next step.

**After the code (Markdown):**
1. State only observations supported by the displayed output.
2. Explain the interpretation in domain terms.
3. Explain limitations (association is not causation; descriptive is not predictive; in-sample is not out-of-sample).
4. Explicitly state the decision or next analysis affected by the result.

## Storyline for this project
Banking credit risk and expected credit loss -> IFRS 9 / Brazilian CMN 4.966 context -> PD/LGD/EAD/staging and macroeconomic scenarios -> role and limitations of NFCI -> temporal EDA -> split/lookback -> persistence baseline -> MLP/CNN/LSTM experiments -> comparative evidence -> cautious conclusion.

## Visual standards
- A graph must answer a named question and be referenced in the interpretation.
- Label axes, units/frequency, period and target; use consistent colors for partitions/models.
- Avoid unneeded 3D charts, decorative charts and redundant tables.
- Show uncertainty, different regimes or errors where relevant.
- Do not use the held-out test to choose models or hyperparameters.

## Project-specific guardrails
- `Credit` is a financial-conditions subindex, not PD, LGD, EAD or default.
- Do not claim causal impact from Pearson or lagged correlation.
- Do not claim 52-week seasonality from a 52-week rolling statistic.
- Report benchmark persistence before presenting deep learning as useful.
- Keep all Python imports in the single designated notebook cell.
- The final academic deliverable is the notebook itself.


## Regra de conclusão acadêmica
- A discussão e a conclusão do relatório devem ser redigidas como células Markdown estáticas, após análise dos arquivos reais de métricas e previsões.
- Não criar funções Python que montem automaticamente parágrafos de conclusão, nem salvar `conclusao_automatica.md`.
- Métricas computadas podem alimentar tabelas e gráficos; interpretação, limitações e conclusão devem ser texto autoral fundamentado, revisável e coerente com o experimento.
- Separar seleção pela validação e avaliação final pelo teste. Nunca selecionar o modelo com base no teste.
