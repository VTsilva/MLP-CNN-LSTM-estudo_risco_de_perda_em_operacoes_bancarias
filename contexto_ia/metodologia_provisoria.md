# Metodologia provisória e requisitos do trabalho

## Fonte prioritária

O roteiro acadêmico original está em:

`arquivos_de_contexto/trabalho 1 previsao univariada e multivariada passo unico.ipynb`

Este resumo facilita a navegação, mas não substitui o enunciado. Em caso de divergência, conferir o notebook original.

## Requisitos gerais identificados

- Escolher uma série temporal real com duas ou mais variáveis e pelo menos 1.000 pontos consecutivos.
- Descrever a fonte, aquisição/processamento, variáveis e relevância.
- Realizar análise estatística e visualização temporal; explorar tendências e ciclos.
- Dividir cronologicamente em 70% treino, 20% validação e 10% teste.
- Definir uma janela móvel (*lookback*).
- Fazer previsão de um único passo à frente.
- Acompanhar a função de custo e a métrica chamada de “acurácia” no roteiro, em treino e validação.
- Inspecionar graficamente o comportamento de treino e validação para identificar overfitting/plateau e escolher o número de épocas.
- Retreinar conforme o número de épocas definido e reportar resultados em treino, validação e teste.
- Comparar modelos com tabelas e gráficos e discutir as limitações.
- Discutir diferenças entre previsão univariada e multivariada.
- O notebook informa que a entrega acadêmica será um único arquivo `.ipynb`, nomeado `<nome_do_estudante>_trabalho1.ipynb`.

## Experimento univariado — Passo 3 do roteiro

Entrada: histórico da própria variável `Credit`.

Saída: valor de `Credit` no passo seguinte.

Modelos explicitamente listados:

1. MLP de uma camada.
2. MLP de duas camadas.
3. CNN.
4. LSTM.
5. Stacked LSTM de duas camadas.
6. LSTM bidirecional.
7. CNN-LSTM.
8. ConvLSTM.

O roteiro também solicita comparação dos resultados no item 3.i.

## Experimento multivariado de saída única — Passo 4 do roteiro

Entrada: histórico de múltiplas variáveis do conjunto.

Saída: somente o valor de `Credit` no passo seguinte.

Modelos explicitamente listados:

1. MLP de uma camada.
2. MLP de duas camadas.
3. MLP Multi-Cabeça de uma camada.
4. CNN.
5. CNN Multi-Cabeça.
6. LSTM.
7. Stacked LSTM de duas camadas.
8. LSTM bidirecional.

O roteiro também solicita comparação dos resultados no item 4.i.

## Partição e geração de janelas

A divisão dos dados deve respeitar a ordem cronológica:

- primeiros 70%: treinamento;
- 20% seguintes: validação;
- 10% finais: teste.

A janela temporal ainda não foi escolhida. Deve ser definida e justificada com base na frequência semanal, no tamanho da amostra, no comportamento observado e na viabilidade computacional.

O notebook do professor contém a orientação “ao final, embaralhe a série de treinamento”. A interpretação metodologicamente segura é preservar a ordem temporal para divisão e construção das janelas e, se necessário, embaralhar apenas as amostras/janelas de treinamento durante o ajuste do modelo. Não embaralhar a série bruta antes da divisão nem as amostras de validação/teste.

## Cuidados contra vazamento temporal

- Ajustar scalers, imputadores e outros transformadores somente com o período de treino.
- Aplicar os parâmetros aprendidos no treino aos conjuntos de validação e teste.
- Não usar informações futuras para formar features de uma previsão passada.
- Definir claramente como as janelas próximas às fronteiras treino/validação/teste serão formadas, para não usar rótulos futuros indevidamente.
- Não escolher hiperparâmetros com base no conjunto de teste.

## Métricas

O roteiro usa o termo “acurácia”, embora a tarefa definida seja previsão de valor numérico contínuo (regressão). A métrica exata ensinada/adotada na disciplina deve ser conferida no material de aula antes de fechar a implementação.

Como candidatas adequadas a regressão, avaliar MAE, RMSE e eventualmente MSE e R². A seleção final deve ser justificada e aplicada igualmente aos modelos. MAPE requer cautela se a série-alvo assumir valores próximos de zero ou valores negativos.

## Observações metodológicas

- A previsão de `Credit` não é uma estimativa direta de PD, LGD, EAD ou perda esperada.
- A motivação em LGD deve ser apresentada com cautela, sem alegar causalidade.
- O objetivo é comparar arquiteturas sob condições tão consistentes quanto possível: mesma partição, mesma janela, mesmas variáveis de entrada (quando comparável), mesmos critérios de avaliação e controle de sementes/aleatoriedade quando viável.
- Arquiteturas multi-head e ConvLSTM devem ser implementadas conforme o significado efetivo no notebook/aulas; não presumir que variantes de arquitetura possuem estrutura única sem conferir os exemplos da disciplina.
