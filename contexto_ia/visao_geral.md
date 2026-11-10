# Visão geral do projeto

## Identidade
- Repositório: `MLP-CNN-LSTM-estudo_risco_de_perda_em_operacoes_bancarias`
- GitHub: https://github.com/VTsilva/MLP-CNN-LSTM-estudo_risco_de_perda_em_operacoes_bancarias
- Título: “Comparação de arquiteturas MLP, CNN e LSTM na previsão de condições de crédito: uma abordagem de séries temporais aplicada ao estudo do risco de perda em operações bancárias.”
- Disciplina: IAD-012 — Redes neurais recorrentes.
- Notebook principal: `victor_silva_trabalho1.ipynb` na raiz.
- Entrega da disciplina: somente o notebook `.ipynb` final, conforme o enunciado.

## Objetivo
Comparar arquiteturas neurais na previsão semanal de um passo à frente da variável `Credit` do dataset NFCI, em experimentos univariados e multivariados.

## Motivação e delimitação
O contexto é provisionamento bancário e perdas de crédito esperadas (IFRS 9 e Resolução CMN 4.966). O dataset, contudo, é um indicador agregado dos Estados Unidos e não contém PD, LGD, EAD, operações, default ou recuperações. O estudo prevê condições de crédito, não estima LGD nem provisões.

## Dados
- Raw: `data/raw/nfci-data-series-csv.csv`.
- 2.913 registros semanais, 08/01/1971–30/10/2026, seis variáveis numéricas e uma data.
- Target: `Credit`.
- Features multivariadas candidatas: `Credit`, `Risk`, `Leverage`, `Nonfinancial_Leverage`.
- `NFCI` e `ANFCI` fora do primeiro desenho, dada a sobreposição com componentes.

## Experimentos exigidos
O roteiro contém 8 modelos univariados e 8 multivariados; ver `contexto_ia/metodologia_provisoria.md` e notebook do professor em `arquivos_de_contexto/`.

## Princípio de narrativa
Toda análise deverá responder: (1) por que foi feita; (2) o que o código calcula; (3) o que os resultados mostram; (4) que decisão ou próximo passo é afetado. Eliminar análises decorativas ou que não contribuam para a pergunta experimental.
