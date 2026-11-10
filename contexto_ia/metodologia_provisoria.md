# Metodologia experimental — implementação atual

## Problema
Regressão semanal de um passo à frente: estimar `Credit[t+1]` a partir de observações anteriores. O trabalho é motivado pelo contexto de risco de crédito/provisionamento, mas não estima PD, LGD, EAD ou provisão.

## Dados e partições
- Fonte: CSV semanal Chicago Fed NFCI em `data/raw/`.
- Target: `Credit`.
- Cortes cronológicos: 70% treino, 20% validação, 10% teste (sem embaralhar a série bruta).
- Lookback experimental comum: 52 semanas; `X[t-52:t] -> y[t]`.
- Scalers ajustados exclusivamente no treino; aplicados à validação/teste sem reajuste.
- As janelas de validação/teste usam somente o passado que já estaria observado até cada target.
- O `shuffle=True` do `model.fit` embaralha apenas a ordem de janelas completas no treino; a sequência interna não é alterada.

## Experimento univariado — 8 modelos
Entrada: somente `Credit` (um canal). Modelos: MLP 1 camada oculta; MLP 2 camadas ocultas; CNN 1D; LSTM; Stacked LSTM; LSTM bidirecional; CNN-LSTM; ConvLSTM2D adaptada.

## Experimento multivariado — 8 modelos
Entradas: `Credit`, `Risk`, `Leverage`, `Nonfinancial_Leverage` (4 canais). Target único: `Credit[t+1]`. Modelos: MLP 1 camada; MLP 2 camadas; MLP multi-cabeça de 1 camada por variável; CNN 1D; CNN multi-cabeça; LSTM; Stacked LSTM; LSTM bidirecional.

## Definições das arquiteturas
- MLP: achata a janela e aplica Dense(64) ou Dense(64, 32), ReLU.
- CNN: Conv1D causal, kernel 3, 32 filtros, pooling global e Dense.
- LSTM: 32 unidades; Stacked: LSTM(32, return_sequences=True) + LSTM(16); Bidirecional: Bidirectional(LSTM(32)).
- CNN-LSTM: Conv1D causal (32 filtros, kernel 3) seguida de LSTM(32).
- MLP multi-cabeça: cada variável é achatada e processada por Dense(16); concatenação e regressão.
- CNN multi-cabeça: Conv1D (16 filtros, kernel 3) e pooling por variável; concatenação e regressão.
- ConvLSTM: janela univariada 52 organizada em 13 blocos de 4 semanas (`13 × 4 × 1 × 1`); ConvLSTM2D(16, kernel 3×1), flatten e Dense. É uma adaptação artificial para uma sequência unidimensional, que deve ser discutida como limitação.

## Treinamento em duas fases
1. Diagnóstico: treinar cada arquitetura até `EPOCHS_DIAGNOSTICO=100`, sem EarlyStopping automático, registrando MSE/loss e MAE em treino/validação.
2. Seleção de épocas: inspecionar MSE/MAE em treino e validação; a decisão e a justificativa de cada arquitetura ficam registradas em `resultados_execucao/selecao_epocas_retreinamento.csv`. A seleção atual foi feita a partir dos históricos fornecidos e usa o menor `val_loss` como âncora, com interpretação da forma das curvas.
3. Retreinamento: reinicializar pesos e treinar somente no conjunto de treino pelo número de épocas registrado. O notebook carrega a seleção automaticamente; não é necessário preencher dicionários ou flags.
4. Avaliação: calcular MAE, MSE, RMSE, R² e acurácia direcional em treino, validação e teste, com previsões e targets revertidos à escala original.

## Métricas
MSE como função de custo; MAE como métrica de acompanhamento. MAE/RMSE são métricas principais interpretáveis na escala original; R² é complementar. Acurácia direcional mede se o modelo antecipa a direção da variação em relação ao último valor observado; não é accuracy de classificação convencional. Para o target contínuo, `accuracy` de classificação não é uma métrica apropriada sem uma regra explícita de discretização. MAPE não é adotado, pois Credit pode ser negativo ou próximo de zero. Caso o docente tenha definido uma métrica específica de acurácia para regressão no material IAD-012, essa definição deve ser conferida antes da entrega final.

## Benchmark e seleção
Benchmark persistente: `Credit[t+1] = Credit[t]`, nos mesmos alvos e partições. Seleção das arquiteturas pela validação, priorizando MAE e usando RMSE, R², acurácia direcional e complexidade como complementos. O teste é reservado ao relato final; nunca selecionar por teste.

## Registro e artefatos
Diagnósticos, curvas e sugestões são salvos em `resultados_execucao/diagnostico_{univariado,multivariado}/`. Métricas e previsões finais em `resultados_execucao/avaliacao_{univariado,multivariado}/`; tabelas/gráficos comparativos em `resultados_execucao/`.


## Histórico do diagnóstico e seleção de épocas
- Os diagnósticos originais foram realizados em 08/11/2026, com até 100 épocas por arquitetura, acompanhando loss/MSE e MAE em treino e validação.
- A seleção de época usou o menor `val_loss` observado como âncora, com inspeção das curvas. Dez das 16 arquiteturas atingiram seu melhor ponto nas épocas 99 ou 100; nesses casos, o limite de 100 épocas não prova convergência ou plateau.
- O retreinamento final foi executado em 09/11/2026 com inicialização nova e as épocas selecionadas. As métricas finais de treino, validação e teste estão registradas nos CSVs de `resultados_execucao/avaliacao_*`.
- A interpretação consolidada dos diagnósticos e dos retreinamentos, com tabelas quantitativas e limitações, está em `resultados_execucao/interpretacao_diagnosticos.md`.

## Protocolo final e resultados (09/11/2026)
- Lookback: 52 semanas fixas para todas as arquiteturas, por consistência de comparação; não houve otimização por validação em outros lookbacks.
- Seleção: menor MAE de validação para escolher a arquitetura; RMSE, R² e acurácia direcional entram como métricas auxiliares.
- Resultado univariado: BiLSTM é a melhor pela validação e mantém desempenho no teste; MAE 0,005171 na validação e 0,002368 no teste.
- Resultado multivariado: LSTM é a melhor entre as arquiteturas multivariadas, mas não supera a persistência; MAE 0,017032 na validação e 0,012216 no teste, contra 0,011082 e 0,005188 do benchmark.
- Conclusão acadêmica é Markdown estático; não é gerada por função do notebook.
- Limitações: uma seed por modelo; sem rolling-origin; dez diagnósticos atingiram 99/100 épocas; ambiente original registrou Python 3.14.4, mas não versão exata de TensorFlow/Keras ou dispositivo.
