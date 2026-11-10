# Leia primeiro — continuidade do projeto

1. Leia `README.md` e `AGENTS.md` na raiz.
2. Consulte `estado_atual.md`, `decisoes.md`, `metodologia_provisoria.md` e `enunciado_e_requisitos.md`.
3. Abra `victor_silva_trabalho1.ipynb`: é o artefato principal e contém EDA + os fluxos de 8 modelos univariados e 8 multivariados.
4. Consulte as Skills aplicáveis, especialmente `neural-timeseries-experiment` e `academic-notebook-storytelling`.
5. O ambiente de referência atual é Python 3.14.x (64-bit), conforme `.python-version` e `requirements.txt`.
6. O ZIP recebido já contém diagnósticos executados para os 16 modelos. A interpretação está em `resultados_execucao/interpretacao_diagnosticos.md`; as épocas selecionadas e justificativas estão em `resultados_execucao/selecao_epocas_retreinamento.csv`.
7. O notebook reutiliza os diagnósticos existentes quando a configuração coincide e executa automaticamente os retreinamentos. Não é necessário preencher dicionários `None` ou alterar flags.
7. Preserve os dados Raw e o notebook do professor. Não faça commit/push sem autorização.

## Artefatos de execução
Após executar, consulte `resultados_execucao/` para históricos, curvas, métricas e previsões. Para uma análise de resultados, peça o ZIP atualizado com essa pasta e o notebook salvo com as saídas.


## Estado final da execução recebida (09/11/2026)
Os 16 retreinamentos estão concluídos e os CSVs de métricas/previsões foram conferidos. Melhor univariado: BiLSTM; melhor multivariado: LSTM, porém inferior à persistência. A discussão e a conclusão acadêmica são Markdown estático no notebook, não geradas por código. Ver `resultados_execucao/discussao_conclusao.md` e `estado_atual.md`.
