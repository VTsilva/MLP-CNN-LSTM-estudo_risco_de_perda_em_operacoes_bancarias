# Interpretação dos diagnósticos e resultados finais

Data da revisão: 09/11/2026. Fonte dos resultados: CSVs e previsões presentes no ZIP executado recebido.

## 1. Integridade e escopo

Foram conferidos os históricos de diagnóstico, as configurações e os arquivos finais de métricas e previsões. Existem oito arquiteturas por abordagem e três partições por modelo. Cada arquivo de métricas contém 24 registros (8 modelos × treino, validação e teste). Cada arquivo de previsões contém 22.888 registros (8 modelos × 2.861 alvos somados nas partições), sem chaves duplicadas ou valores ausentes nas métricas.

A previsão é de um passo semanal: `Credit[t+1]`. O experimento univariado utiliza somente o histórico de `Credit`; o multivariado utiliza `Credit`, `Risk`, `Leverage` e `Nonfinancial_Leverage`. O benchmark é persistência, isto é, prever `Credit[t+1] = Credit[t]`.

## 2. Diagnósticos e seleção de épocas

Cada arquitetura foi diagnosticada por até 100 épocas, acompanhando MSE (loss) e MAE em treino e validação. A época escolhida corresponde ao menor `val_loss` observado, com inspeção da curva e justificativa registrada em `selecao_epocas_retreinamento.csv`. O modelo foi reinicializado e retreinado do zero pelo número selecionado; as métricas finais foram calculadas na escala original.

| Abordagem | Modelo | Época escolhida | Leitura do diagnóstico |
|---|---|---:|---|
| Univariada | MLP 1 | 100 | Melhor ponto na borda; sem prova de convergência |
| Univariada | MLP 2 | 99 | Melhor ponto próximo ao limite; pequena reversão final |
| Univariada | CNN 1D | 99 | Melhor ponto próximo ao limite; desempenho final fraco |
| Univariada | LSTM | 100 | Validação ainda melhorava ao final do intervalo observado |
| Univariada | Stacked LSTM | 100 | Melhor ponto na borda; sem prova de convergência |
| Univariada | BiLSTM | 100 | Melhor ponto na borda; sem prova de convergência |
| Univariada | CNN-LSTM | 100 | Melhor ponto na borda; sem prova de convergência |
| Univariada | ConvLSTM2D adaptada | 92 | Mínimo antes do limite, seguido de deterioração |
| Multivariada | MLP 1 | 90 | Validação piora após o mínimo; sinal de overfitting |
| Multivariada | MLP 2 | 38 | Melhor ponto antes do limite; treino segue melhorando e validação degrada/oscila |
| Multivariada | MLP multi-cabeça | 100 | Melhor ponto na borda; sem prova de convergência |
| Multivariada | CNN 1D | 1 | Validação piora desde o início; generalização muito fraca |
| Multivariada | CNN multi-cabeça | 59 | Validação degrada depois do mínimo; sinal de overfitting |
| Multivariada | LSTM | 88 | Mínimo de validação antes do limite |
| Multivariada | Stacked LSTM | 99 | Mínimo próximo ao limite, com pequena reversão |
| Multivariada | BiLSTM | 100 | Melhor ponto na borda; sem prova de convergência |

Dez dos 16 modelos tiveram o melhor ponto nas épocas 99 ou 100. Nesses casos, a seleção é o melhor resultado observado no intervalo, e não evidência de que o modelo tenha atingido um ótimo de treinamento. Aumentar o limite de épocas poderia alterar a comparação; isso deve ser tratado como limitação, não como justificativa para escolher épocas com base no teste.

## 3. Benchmark de persistência

| Partição | MAE | RMSE | R² |
|---|---:|---:|---:|
| Treinamento | 0,02192 | 0,03498 | 0,9991 |
| Validação | 0,01108 | 0,01794 | 0,9908 |
| Teste | 0,00519 | 0,00653 | 0,9965 |

A persistência é forte porque a série `Credit` apresenta alta autocorrelação. Portanto, superá-la é um critério mais informativo do que apresentar R² elevado isoladamente.

## 4. Resultados finais — abordagem univariada

A seleção é feita pela MAE de validação. A coluna de teste é apresentada somente como avaliação fora da amostra e não participa da escolha.

| Modelo | Épocas | MAE validação | RMSE validação | R² validação | MAE teste | RMSE teste | R² teste |
|---|---:|---:|---:|---:|---:|---:|---:|
| MLP 1 | 100 | 0,017759 | 0,025301 | 0,981752 | 0,013771 | 0,016555 | 0,977816 |
| MLP 2 | 99 | 0,022881 | 0,031278 | 0,972112 | 0,011201 | 0,014273 | 0,983512 |
| CNN 1D | 99 | 0,080053 | 0,091030 | 0,763782 | 0,077095 | 0,081431 | 0,463282 |
| LSTM | 100 | 0,005459 | 0,008219 | 0,998074 | 0,003010 | 0,003695 | 0,998895 |
| Stacked LSTM | 100 | 0,006911 | 0,009939 | 0,997184 | 0,004411 | 0,005344 | 0,997688 |
| BiLSTM | 100 | **0,005171** | **0,007501** | **0,998396** | **0,002368** | **0,003123** | **0,999211** |
| CNN-LSTM | 100 | 0,006850 | 0,009627 | 0,997358 | 0,003849 | 0,004784 | 0,998147 |
| ConvLSTM2D adaptada | 92 | 0,009384 | 0,013286 | 0,994968 | 0,006492 | 0,007642 | 0,995273 |
| Persistência | — | 0,011082 | 0,017940 | 0,990825 | 0,005188 | 0,006529 | 0,996549 |

A BiLSTM apresenta a menor MAE de validação (0,005171) e mantém a menor MAE no teste (0,002368). Em relação à persistência, reduz a MAE em 53,34% na validação e 54,36% no teste. A LSTM convencional também supera a persistência nas duas partições. CNN-LSTM e Stacked LSTM apresentam desempenho competitivo. ConvLSTM supera persistência na validação, mas não no teste. As duas MLPs e a CNN 1D não superam o benchmark em MAE.

A conclusão mais forte é que o histórico univariado de `Credit` contém informação muito relevante para prever seu próximo valor. As arquiteturas recorrentes foram mais adequadas do que as MLPs e a CNN 1D nesta configuração específica.

## 5. Resultados finais — abordagem multivariada

| Modelo | Épocas | MAE validação | RMSE validação | R² validação | MAE teste | RMSE teste | R² teste |
|---|---:|---:|---:|---:|---:|---:|---:|
| MLP 1 | 90 | 0,073005 | 0,099926 | 0,715357 | 0,060608 | 0,074310 | 0,553057 |
| MLP 2 | 38 | 0,088845 | 0,112613 | 0,638489 | 0,079837 | 0,098913 | 0,208098 |
| MLP multi-cabeça | 100 | 0,041994 | 0,053968 | 0,916972 | 0,046724 | 0,057699 | 0,730535 |
| CNN 1D | 1 | 0,579581 | 0,644453 | -10,839359 | 0,608189 | 0,642907 | -32,454797 |
| CNN multi-cabeça | 59 | 0,208799 | 0,272386 | -1,115017 | 0,141071 | 0,178483 | -1,578422 |
| LSTM | 88 | **0,017032** | **0,022459** | **0,985621** | **0,012216** | **0,014274** | **0,983510** |
| Stacked LSTM | 99 | 0,026665 | 0,035972 | 0,963113 | 0,022087 | 0,026000 | 0,945283 |
| BiLSTM | 100 | 0,061488 | 0,079402 | 0,820277 | 0,079576 | 0,092230 | 0,311497 |
| Persistência | — | 0,011082 | 0,017940 | 0,990825 | 0,005188 | 0,006529 | 0,996549 |

A LSTM é a melhor arquitetura multivariada pela validação, mas sua MAE é 53,68% maior que a persistência na validação e 135,44% maior no teste. Nenhuma das oito arquiteturas multivariadas supera a persistência em MAE nas partições de validação ou teste. Assim, a inclusão de `Risk`, `Leverage` e `Nonfinancial_Leverage` não produziu ganho preditivo incremental neste experimento.

O resultado não demonstra que essas variáveis sejam inúteis em geral. Correlação contemporânea ou defasada não garante ganho após incluir o próprio histórico de `Credit`; além disso, os subíndices pertencem ao mesmo sistema de indicadores e podem conter informação sobreposta.

## 6. Comparação entre abordagens e interpretação das partições

Na validação, o melhor modelo multivariado (LSTM, MAE 0,017032) apresenta MAE 229,39% maior que a melhor arquitetura univariada (BiLSTM, MAE 0,005171). O teste preserva a mesma ordenação geral: a BiLSTM univariada tem MAE 0,002368, enquanto a melhor multivariada tem MAE 0,012216.

Os erros absolutos observados no teste são menores que os da validação para o benchmark e para os melhores modelos. Essa diferença precisa ser interpretada junto à dispersão do target: desvio-padrão aproximado de 0,1875 na validação e 0,1113 no teste. O período de teste apresenta menor variação de `Credit`; por isso, comparar MAE entre partições sem considerar a escala e o regime pode induzir a conclusões erradas. A comparação de cada modelo com a persistência dentro da mesma partição é mais informativa.

A métrica denominada `Acuracia_direcional` é complementar. Ela compara o sinal da variação prevista com o sinal da variação observada em relação ao último valor. A persistência prevê variação zero; portanto, sua taxa de acerto só é positiva quando o valor seguinte não se altera. Por essa razão, o baixo valor da persistência nessa métrica não deve ser interpretado como uma comparação convencional de direção ou como evidência isolada de superioridade das redes.

## 7. Decisões e limitações metodológicas

- O lookback de 52 semanas foi mantido como escolha operacional comum para comparar arquiteturas sob a mesma entrada. Não houve avaliação de desempenho com 13, 26 ou 104 semanas; 52 não é um ótimo demonstrado nem evidência de sazonalidade anual.
- Cada arquitetura teve uma única execução, com seed base 42 e seed derivada da posição do modelo. Não foram quantificadas variações entre seeds nem validação temporal de origem móvel.
- Dez diagnósticos tiveram melhor ponto em 99 ou 100 épocas. O limite de 100 não prova convergência ou plateau para esses modelos.
- A versão exata de TensorFlow/Keras e o dispositivo (CPU/GPU) da execução original não foram capturados. O metadado do kernel registra Python 3.14.4. O hash do CSV e a impressão digital do notebook recebido/revisado estão em `proveniencia_execucao.json`.
- O target é um índice macrofinanceiro agregado dos Estados Unidos, não uma variável de operação bancária. O trabalho não estima PD, LGD, EAD ou provisão IFRS 9/CMN 4.966.
- A ConvLSTM2D foi adaptada em blocos temporais artificiais; a série não contém dimensão espacial natural.

## 8. Conclusão da análise

Entre as alternativas e configurações testadas, a BiLSTM univariada foi a melhor arquitetura: selecionada pela MAE de validação e confirmada pelo menor erro no teste, superou o benchmark de persistência. A abordagem multivariada não trouxe benefício nesta especificação: sua melhor rede, a LSTM, ficou atrás da persistência. O resultado reforça que adicionar variáveis ou complexidade arquitetural não garante melhor previsão e que modelos de séries temporais devem ser comparados com baselines simples.

A interpretação permanece circunscrita ao NFCI Credit Subindex, ao horizonte de uma semana, ao lookback fixo de 52 semanas, às partições e às únicas execuções recebidas. Repetições com múltiplas seeds, validação de origem móvel e comparação controlada de lookbacks são extensões recomendadas, não análises realizadas neste trabalho.
