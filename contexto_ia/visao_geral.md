# Visão geral do projeto

## Identificação

- **Projeto:** Trabalho 1 — Redes recorrentes.
- **Disciplina/tema:** previsão de séries temporais com redes neurais.
- **Data de consolidação deste documento:** 07/11/2026.
- **Base escolhida:** indicadores do National Financial Conditions Index (NFCI), do Federal Reserve Bank of Chicago.
- **Variável-alvo escolhida:** `Credit`, correspondente ao Credit Subindex.

## Título provisório

**Comparação de arquiteturas MLP, CNN e LSTM na previsão de condições de crédito: uma abordagem de séries temporais aplicada ao estudo do risco de perda em operações bancárias.**

## Motivação

O projeto busca estudar condições de crédito em contexto financeiro/bancário, conectando a previsão de séries temporais à discussão sobre risco de crédito e perdas em operações bancárias. O interesse inicial surgiu da LGD (*Loss Given Default*), mas a base pública escolhida contém indicadores de condições financeiras, e não observações diretas de LGD.

Assim, o trabalho atual tem como alvo estatístico a previsão do subíndice `Credit`. A relação com LGD será apresentada como motivação e contexto econômico: condições financeiras e de crédito podem ser relevantes para compreender o ambiente em que perdas e recuperações de crédito ocorrem. Não se deve afirmar que o modelo estima LGD ou que a previsão de `Credit` é equivalente à previsão de LGD.

## Objetivo acadêmico

Familiarizar o aluno com o uso de diferentes arquiteturas baseadas em redes neurais para previsão de séries temporais, comparando experimentos univariados e multivariados de previsão de um único passo à frente.

## Pergunta de pesquisa provisória

Como diferentes arquiteturas de redes neurais se comparam na previsão de um passo à frente do subíndice de condições de crédito (`Credit`), utilizando somente seu histórico (abordagem univariada) ou incorporando outros subíndices do NFCI (abordagem multivariada)?

## Escopo inicial

1. Descrever a fonte, a frequência, o histórico e as variáveis do conjunto.
2. Validar e explorar a série temporal.
3. Preparar os dados para previsão de um passo à frente.
4. Executar os modelos univariados previstos no notebook do professor.
5. Executar os modelos multivariados previstos no notebook do professor.
6. Comparar desempenho, curvas de treinamento/validação e resultados no conjunto de teste.
7. Discutir as diferenças entre previsão univariada e multivariada.

## O que não faz parte do escopo confirmado

- Construir um modelo de LGD individual.
- Prever diretamente perdas realizadas ou taxas de recuperação.
- Estabelecer relações causais entre NFCI e LGD.
- Interpretar o experimento como uma aplicação de produção ou política real de crédito.

Esses temas podem aparecer na contextualização, mas não são resultados que a base selecionada permita afirmar diretamente.
