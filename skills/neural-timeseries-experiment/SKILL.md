---
name: neural-timeseries-experiment
description: Execute, audit and interpret the univariate and multivariate neural time-series experiments in the NFCI academic project.
---

# Skill: neural time-series experiment

## When to use
Use when implementing, running, reviewing or interpreting MLP, CNN, LSTM, CNN-LSTM or ConvLSTM experiments in `victor_silva_trabalho1.ipynb`.

## Required context
Read `AGENTS.md`, `contexto_ia/decisoes.md`, `contexto_ia/metodologia_provisoria.md`, `arquivos_de_contexto/enunciado_e_requisitos.md` and the corresponding notebook section.

## Non-negotiable protocol
1. Target is `Credit[t+1]`; do not rename it to LGD, PD, EAD, default or provision.
2. Keep chronological 70/20/10 splits; do not shuffle raw time-series rows.
3. Build windows so each input uses only observations before its target.
4. Fit feature and target scalers on train only.
5. Keep `WINDOW_SIZE=52` common across architectures unless a separately justified validation-only sensitivity study is requested.
6. Use MSE loss and MAE metric for continuous regression; never use classification accuracy as the loss metric.
7. Compare against persistence (`y_hat[t+1]=y[t]`) on the exact same target indices.
8. Train diagnostics without automatic early stopping and inspect train/validation MSE and MAE. Record the selected epoch and written rationale for each architecture in `resultados_execucao/selecao_epocas_retreinamento.csv`; never infer convergence when the best epoch is at the diagnostic cap.
9. Retain the test set for final reporting only.
10. Reuse saved diagnostic histories only when their configuration matches the current data/features/lookback/hyperparameters. The notebook then loads the reviewed epoch selections and retrains each model automatically. Export histories, curves, final metrics and predictions to `resultados_execucao/`.

## Architecture assumptions
- Multi-head branches are separated by input feature and concatenated before one regression output.
- ConvLSTM is a documented temporal-block adaptation (13 blocks × 4 weeks), not a spatial interpretation of NFCI.
- Keep all imports in the notebook's single `central-imports` cell.

## Interpretation standards
- Discuss validation performance first, then report test performance.
- Include MAE/RMSE, R², directional accuracy, train-validation gap and parameter count.
- A neural network is not automatically better than persistence.
- Distinguish observed results from hypotheses and limitations.


## Current diagnostic interpretation
- The supplied 100-epoch diagnostics favor univariate models; BiLSTM had the lowest validation MSE, followed by LSTM.
- The best multivariate candidate was LSTM, but none of the multivariate models beat persistence on validation in the supplied run.
- Several models reached the 99/100-epoch boundary. Treat their selected epoch as the best observed within the available budget, not proof of plateau.
- The ZIP has no final neural evaluation outputs yet. Do not invent final test performance or declare a final winner until `avaliacao_*` outputs exist.
- See `resultados_execucao/interpretacao_diagnosticos.md` and `selecao_epocas_retreinamento.csv`.
