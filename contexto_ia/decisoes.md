# Registro de decisões

Este documento distingue decisões confirmadas pelo responsável pelo projeto de propostas ainda pendentes de validação.

| ID | Tema | Decisão/entendimento | Status | Observação |
|---|---|---|---|---|
| D-001 | Tema | Trabalhar com previsão de condições de crédito no contexto financeiro/bancário. | Confirmado | Motivação inicial relacionada à LGD. |
| D-002 | Base | Utilizar o conjunto de indicadores do NFCI, obtido no CSV `nfci-data-series-csv.csv`. | Confirmado | Fonte institucional: Federal Reserve Bank of Chicago. |
| D-003 | Variável-alvo | Prever `Credit` (Credit Subindex). | Confirmado | Decisão expressa pelo responsável pelo projeto. |
| D-004 | Título | Adotar provisoriamente o título “Comparação de arquiteturas MLP, CNN e LSTM na previsão de condições de crédito: uma abordagem de séries temporais aplicada ao estudo do risco de perda em operações bancárias.” | Provisório | Pode ser refinado para espelhar os modelos e escopo finais. |
| D-005 | Frequência | Manter a frequência semanal original, sem subamostragem inicialmente. | Provisório | Confirmar após EDA e avaliação das exigências do notebook. |
| D-006 | Experimento multivariado | Avaliar `Risk`, `Leverage` e `Nonfinancial_Leverage` como variáveis explicativas, além do histórico de `Credit`. | Provisório | Confirmar após análise da base e da estrutura dos modelos. |
| D-007 | Índices agregados | Não incluir `NFCI` e `ANFCI` no primeiro desenho multivariado. | Provisório | São índices agregados/ajustados com sobreposição conceitual e matemática aos subíndices; avaliar risco de redundância/vazamento. |
| D-008 | Horizonte | Previsão de um único passo à frente (semana seguinte). | Confirmado pelo roteiro acadêmico | Aplicar à série de saída `Credit`. |
| D-009 | Partição | Divisão cronológica 70% treino, 20% validação e 10% teste. | Confirmado pelo roteiro acadêmico | Não embaralhar a sequência antes da divisão. |
| D-010 | Arquitetura do projeto | Organizar dados em `raw`, `bronze`, `silver` e `gold`, além dos diretórios de contexto, planos, skills, imagens e fontes. | Confirmado | Conforme estrutura adotada pelo responsável pelo projeto. |

## Decisões pendentes

- Tamanho da janela (*lookback/window size*).
- Estratégia de normalização/padronização e tratamento de eventuais outliers.
- Métricas finais de regressão e como responder ao termo “acurácia” usado no roteiro do professor.
- Critério operacional para selecionar o número de épocas pela curva de treino/validação.
- Hiperparâmetros e critérios de comparação dos modelos.
- Se haverá experimento adicional usando NFCI/ANFCI como comparação de features.
- Organização exata dos arquivos intermediários e finais de cada etapa.

## Como registrar novas decisões

Adicionar uma linha com identificador sequencial, tema, decisão, status e justificativa. Quando uma decisão antiga mudar, não apagar silenciosamente: atualizar o status e registrar a razão da alteração e a data.
