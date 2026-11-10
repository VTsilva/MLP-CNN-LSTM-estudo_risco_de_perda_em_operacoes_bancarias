## 10.3 Discussão comparativa dos resultados

A comparação utiliza a **MAE de validação como critério primário de seleção**, mantendo o conjunto de teste reservado à avaliação fora da amostra. RMSE e R² complementam a leitura: o RMSE penaliza mais os erros de maior magnitude, enquanto o R² expressa a proporção de variabilidade explicada em cada partição. A acurácia direcional é apresentada somente como indicador complementar, pois não substitui uma métrica de erro para regressão.

### 10.3.1 Resultado univariado

| Modelo | Épocas | MAE validação | RMSE validação | R² validação | MAE teste | RMSE teste | R² teste |
|---|---:|---:|---:|---:|---:|---:|---:|
| MLP — 1 camada oculta | 100 | 0.017759 | 0.025301 | 0.981752 | 0.013771 | 0.016555 | 0.977816 |
| MLP — 2 camadas ocultas | 99 | 0.022881 | 0.031278 | 0.972112 | 0.011201 | 0.014273 | 0.983512 |
| CNN 1D | 99 | 0.080053 | 0.091030 | 0.763782 | 0.077095 | 0.081431 | 0.463282 |
| LSTM | 100 | 0.005459 | 0.008219 | 0.998074 | 0.003010 | 0.003695 | 0.998895 |
| Stacked LSTM | 100 | 0.006911 | 0.009939 | 0.997184 | 0.004411 | 0.005344 | 0.997688 |
| LSTM bidirecional (BiLSTM) | 100 | 0.005171 | 0.007501 | 0.998396 | 0.002368 | 0.003123 | 0.999211 |
| CNN-LSTM | 100 | 0.006850 | 0.009627 | 0.997358 | 0.003849 | 0.004784 | 0.998147 |
| ConvLSTM2D adaptada | 92 | 0.009384 | 0.013286 | 0.994968 | 0.006492 | 0.007642 | 0.995273 |
| Persistência | — | 0.011082 | 0.017940 | 0.990825 | 0.005188 | 0.006529 | 0.996549 |

A **BiLSTM** foi selecionada como melhor arquitetura univariada pela validação, com MAE de **0,005171** e RMSE de **0,007501**. A LSTM convencional ficou próxima (MAE 0,005459), seguida por CNN-LSTM e Stacked LSTM. No teste, a BiLSTM manteve a primeira posição entre os modelos avaliados, com MAE de **0,002368**, RMSE de **0,003123** e R² de **0,999211**.

Em relação ao benchmark de persistência, a BiLSTM reduziu a MAE em **53,34% na validação** (0,011082 para 0,005171) e **54,36% no teste** (0,005188 para 0,002368). A redução de RMSE foi de aproximadamente 58,19% na validação e 52,17% no teste. Portanto, neste recorte temporal, a BiLSTM não apenas ajustou a série: ela superou uma referência simples que já explora a elevada persistência de `Credit`.

A LSTM simples também superou a persistência nas duas partições, embora com erro um pouco maior que a BiLSTM. CNN-LSTM e Stacked LSTM apresentaram resultados competitivos. A ConvLSTM adaptada ficou abaixo dessas arquiteturas recorrentes e híbridas, mas ainda superou a persistência na validação; no teste, sua MAE foi ligeiramente maior que a do benchmark. As duas MLPs tiveram desempenho inferior à persistência na validação e no teste. A CNN 1D apresentou o maior erro entre os modelos univariados, sugerindo que a arquitetura convolucional utilizada, com essa configuração e esse conjunto de dados, não representou tão bem a dinâmica temporal quanto as redes recorrentes.

### 10.3.2 Resultado multivariado

| Modelo | Épocas | MAE validação | RMSE validação | R² validação | MAE teste | RMSE teste | R² teste |
|---|---:|---:|---:|---:|---:|---:|---:|
| MLP — 1 camada oculta | 90 | 0.073005 | 0.099926 | 0.715357 | 0.060608 | 0.074310 | 0.553057 |
| MLP — 2 camadas ocultas | 38 | 0.088845 | 0.112613 | 0.638489 | 0.079837 | 0.098913 | 0.208098 |
| MLP multi-cabeça | 100 | 0.041994 | 0.053968 | 0.916972 | 0.046724 | 0.057699 | 0.730535 |
| CNN 1D | 1 | 0.579581 | 0.644453 | -10.839359 | 0.608189 | 0.642907 | -32.454797 |
| CNN multi-cabeça | 59 | 0.208799 | 0.272386 | -1.115017 | 0.141071 | 0.178483 | -1.578422 |
| LSTM | 88 | 0.017032 | 0.022459 | 0.985621 | 0.012216 | 0.014274 | 0.983510 |
| Stacked LSTM | 99 | 0.026665 | 0.035972 | 0.963113 | 0.022087 | 0.026000 | 0.945283 |
| LSTM bidirecional (BiLSTM) | 100 | 0.061488 | 0.079402 | 0.820277 | 0.079576 | 0.092230 | 0.311497 |
| Persistência | — | 0.011082 | 0.017940 | 0.990825 | 0.005188 | 0.006529 | 0.996549 |

A **LSTM** foi a melhor arquitetura multivariada pela validação, com MAE de **0,017032** e RMSE de **0,022459**. Entretanto, esse resultado foi **53,68% pior em MAE** do que a persistência na validação. No teste, a MAE da LSTM foi **0,012216**, enquanto a persistência obteve **0,005188**: o erro da LSTM foi aproximadamente **135,44% maior**. Nenhuma das oito arquiteturas multivariadas superou a persistência em MAE na validação ou no teste.

A inclusão de `Risk`, `Leverage` e `Nonfinancial_Leverage`, portanto, **não trouxe ganho preditivo incremental neste desenho experimental**. Isso não demonstra que essas variáveis sejam irrelevantes em qualquer horizonte ou especificação. Significa apenas que, com as features, o lookback fixo, as arquiteturas, os hiperparâmetros e as partições utilizados, o histórico univariado de `Credit` forneceu informação mais útil para a previsão de um passo à frente. Correlação contemporânea entre subíndices não garante informação antecipatória adicional; além disso, os componentes pertencem ao mesmo sistema de indicadores e podem compartilhar conteúdo informacional.

### 10.3.3 Comparação entre as abordagens e leitura temporal

Na validação, a MAE do melhor modelo multivariado (LSTM, 0,017032) foi **229,39% maior** que a MAE do melhor modelo univariado (BiLSTM, 0,005171). A diferença também se manteve no teste. O resultado favorece a abordagem univariada para a tarefa específica investigada e não sustenta a hipótese de que acrescentar os três subíndices melhora automaticamente a previsão de `Credit`.

Os erros absolutos do teste foram menores que os da validação para o benchmark e para a maioria dos modelos. Isso deve ser interpretado à luz da distribuição observada: o desvio-padrão de `Credit` foi aproximadamente **0,1875 na validação** e **0,1113 no teste**. O período de teste apresentou menor dispersão, de modo que comparar diretamente MAEs entre partições sem considerar a variabilidade seria inadequado. A comparação mais informativa é modelo contra benchmark **dentro da mesma partição**.

A acurácia direcional da BiLSTM foi de **82,47% na validação** e **87,67% no teste**. A persistência apresentou 4,47% e 4,11%, respectivamente. Esse valor baixo da persistência tem uma explicação matemática: como sua previsão é exatamente o último valor observado, ela prevê variação zero; o indicador só considera acerto quando o valor seguinte realmente permanece inalterado. Por isso, a acurácia direcional deve ser lida com cautela e não usada isoladamente para declarar superioridade.

### 10.3.4 Seleção de épocas, janela e reprodutibilidade

As épocas foram selecionadas a partir da menor perda de validação observada, com inspeção das curvas. Alguns diagnósticos atingiram o limite de 100 épocas sem evidência de reversão clara; nesses casos, a época registrada é o melhor ponto **dentro do intervalo testado**, não uma prova de convergência. Outros apresentaram sinais de overfitting antes do limite, como a CNN multivariada (melhor ponto na primeira época), a MLP de duas camadas multivariada (38 épocas) e a CNN multi-cabeça (59 épocas). Essas diferenças reforçam que a duração adequada do treinamento depende da arquitetura.

O *lookback* de **52 semanas foi mantido como escolha operacional fixa** para padronizar a comparação das arquiteturas e oferecer aproximadamente um ano de contexto semanal. Não foi realizado um experimento de desempenho com 13, 26 e 104 semanas; portanto, 52 não deve ser chamado de ótimo, nem associado a sazonalidade anual comprovada. A lista alternativa apresentada anteriormente serve apenas para ilustrar o custo amostral de diferentes janelas.

Cada arquitetura foi executada uma única vez com seed base 42 e seed derivada da posição do modelo. Não foram realizadas repetições com múltiplas seeds nem validação temporal de origem móvel. Assim, os resultados são reproduzíveis quanto à configuração documentada, mas a variabilidade entre inicializações e diferentes origens temporais não foi quantificada. O notebook registra o Python 3.14.4 no metadado do kernel; a versão exata de TensorFlow/Keras e o dispositivo utilizado não foram capturados nos outputs originais. O hash SHA-256 do CSV e a impressão digital das fontes do notebook estão em `resultados_execucao/proveniencia_execucao.json`; a captura completa de ambiente ficará disponível nas próximas execuções pelo script `tools/capture_execution_provenance.py`.


## 10.4 Conclusão

Este trabalho comparou oito arquiteturas de redes neurais no cenário univariado e oito no cenário multivariado para prever, com horizonte de uma semana, o subíndice `Credit` do National Financial Conditions Index (NFCI). A análise foi realizada sobre 2.913 observações semanais entre 8 de janeiro de 1971 e 30 de outubro de 2026, com separação cronológica em treinamento, validação e teste, lookback operacional de 52 semanas e avaliação frente a um benchmark de persistência.

Os resultados indicam que a **abordagem univariada apresentou o melhor desempenho**. A LSTM bidirecional foi selecionada pela menor MAE de validação (0,005171) e confirmou o resultado no período de teste (MAE 0,002368). Em ambas as partições, superou o benchmark de persistência, reduzindo a MAE em 53,34% na validação e 54,36% no teste. A LSTM convencional também apresentou desempenho competitivo, enquanto CNN-LSTM e Stacked LSTM tiveram resultados próximos. Entre as arquiteturas avaliadas, a CNN 1D apresentou desempenho inferior.

No cenário multivariado, a LSTM foi a melhor das oito arquiteturas pela validação, mas não superou o benchmark de persistência. Nenhum dos modelos multivariados obteve MAE menor que a referência simples na validação ou no teste. Portanto, para esta base, este horizonte e esta configuração experimental, a inclusão de `Risk`, `Leverage` e `Nonfinancial_Leverage` não melhorou a previsão em relação ao uso exclusivo do histórico de `Credit`.

A evidência responde à questão experimental: **é possível prever o próximo valor de `Credit` com redes neurais, mas o ganho depende da arquitetura e da especificação das entradas**. Neste estudo, a BiLSTM univariada foi a alternativa mais eficaz. A comparação também mostra que maior quantidade de variáveis e maior complexidade arquitetural não garantem melhor generalização; um benchmark simples deve permanecer como referência obrigatória.

A relevância financeira do estudo é contextual. O subíndice `Credit` resume condições agregadas do mercado de crédito dos Estados Unidos e pode ajudar a discutir a dinâmica macrofinanceira que acompanha avaliações de risco e cenários econômicos. Entretanto, ele **não representa PD, LGD, EAD, default, inadimplência ou perda esperada de uma carteira**. Assim, o modelo desenvolvido não calcula provisão contábil, não estima diretamente perdas esperadas da IFRS 9 ou da Resolução CMN nº 4.966 e não deve ser interpretado como modelo regulatório. Sua contribuição é demonstrar, em ambiente acadêmico, como arquiteturas de redes neurais podem ser comparadas na previsão de um indicador macrofinanceiro relacionado às condições de crédito.

Os resultados devem ser considerados à luz de limitações: o lookback de 52 semanas foi fixado e não otimizado; cada arquitetura teve uma única execução; não foi realizada validação de origem móvel; parte das curvas atingiu o limite de 100 épocas; a ConvLSTM foi adaptada por blocos temporais artificiais, sem estrutura espacial natural; e a base é agregada e referente aos Estados Unidos. Estudos futuros poderiam avaliar múltiplas seeds, diferentes origens temporais, janelas alternativas e variáveis macroeconômicas externas, sempre selecionando configurações pela validação e mantendo um teste final intocado.

Conclui-se que a BiLSTM univariada foi a melhor arquitetura **entre as alternativas e condições testadas**, mas essa conclusão não implica superioridade universal da arquitetura nem aplicação direta ao cálculo de provisões bancárias. O experimento evidencia a importância de comparar redes neurais com baselines simples, separar seleção e avaliação final e interpretar os resultados dentro dos limites informacionais da série utilizada.
