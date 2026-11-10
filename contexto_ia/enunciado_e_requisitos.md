# Enunciado e requisitos acadêmicos

Este documento consolida as instruções recebidas do responsável pelo projeto e os requisitos conferidos no notebook original do professor. O notebook original em `arquivos_de_contexto/trabalho 1 previsao univariada e multivariada passo unico.ipynb` deve ser consultado em caso de dúvida e não pode ser alterado.

## Objetivo geral do Trabalho 1

Familiarizar o estudante com o uso de diversos modelos baseados em redes neurais (MLP, CNN, LSTM) para previsão de séries temporais. A série escolhida deve ser real, conter duas ou mais variáveis e pelo menos 1.000 pontos consecutivos.

## Requisitos fornecidos pelo responsável

1. Após filtrar e preparar os dados, realizar análise básica da série, plotar gráficos e determinar ciclos e tendências básicas.
2. Dividir cronologicamente os dados em 70% treinamento, 20% validação e 10% teste.
3. Determinar o tamanho da janela móvel.
4. Treinar os modelos acompanhando as funções de custo e a métrica de desempenho em treinamento e validação.
5. Determinar manualmente, por inspeção dos gráficos, o número ideal de épocas, identificando o início de overfitting. Se a quantidade inicial de épocas for insuficiente, continuar até observar overfitting ou plateau da função de custo de validação.
6. Retreinar o modelo até o número de épocas escolhido e calcular desempenho em treinamento, validação e teste.
7. Executar primeiro previsão univariada (somente uma variável; a mesma variável será prevista), com previsão do próximo valor da série (passo único).
8. Comparar todos os modelos univariados e identificar o melhor, com gráficos/tabelas que mostrem capacidades e limitações.
9. Repetir o processo em abordagem multivariada: considerar outras variáveis do dataset, mas prever somente o próximo valor de uma variável-alvo.
10. Produzir relatório profissional, claro e objetivo, explicando métodos, escolhas e resultados.
11. A entrega formal será somente um arquivo `.ipynb`, com nome `<nome_do_estudante>_trabalho1.ipynb`.
12. A avaliação considera correção do código e execução, clareza, legibilidade e profissionalismo.

## Inventário de modelos do notebook do professor

### Passo 3 — Previsão univariada, saída única, passo único

- 3.a MLP de 1 camada.
- 3.b MLP de 2 camadas.
- 3.c CNN.
- 3.d LSTM.
- 3.e Stacked LSTM de 2 camadas.
- 3.f LSTM bidirecional.
- 3.g CNN-LSTM.
- 3.h ConvLSTM.
- 3.i Comparação dos resultados.

### Passo 4 — Previsão multivariada, saída única, passo único

- 4.a MLP de 1 camada.
- 4.b MLP de 2 camadas.
- 4.c MLP multi-cabeça de 1 camada.
- 4.d CNN.
- 4.e CNN multi-cabeça.
- 4.f LSTM.
- 4.g Stacked LSTM de 2 camadas.
- 4.h LSTM bidirecional.
- 4.i Comparação dos resultados.

### Outros passos do notebook original

- Passo 1: download, descrição, subamostragem se justificada e limpeza.
- Passo 2.a: estatísticas, gráficos e identificação de características básicas.
- Passo 2.b: divisão 70/20/10 e tamanho da janela; visualização das partições. O notebook original inclui instrução para embaralhar o conjunto de treinamento.
- Passo 5: discussão final entre previsão univariada e multivariada.
- Passo 6: críticas e sugestões (opcional).

## Interpretação para este projeto

- Variável-alvo escolhida: `Credit`.
- Univariado: entradas formadas pelo histórico de `Credit`; saída é `Credit` no instante imediatamente seguinte.
- Multivariado: entradas formadas pelo histórico de `Credit` e por variáveis adicionais aprovadas após EDA; saída única continua sendo `Credit` no instante seguinte.
- O dataset recebido possui seis variáveis numéricas e uma data, excedendo a exigência mínima de duas variáveis.

## Ponto metodológico que precisa de cuidado

O enunciado usa a palavra “acurácia”, mas `Credit` é uma variável numérica contínua e o trabalho é uma tarefa de regressão. O agente deve verificar como a métrica foi definida no curso IAD-012 e no material de aula. Até essa verificação, não rotular MAE/RMSE ou uma métrica arbitrária como “acurácia” sem explicação. É adequado apresentar métricas de erro de regressão (por exemplo, MAE, RMSE e MSE) como complemento, explicando a definição adotada.

## Fonte primária

Notebook original fornecido pelo professor: `arquivos_de_contexto/trabalho 1 previsao univariada e multivariada passo unico.ipynb`.
