# Instruções para agentes e colaboradores

## Porta de entrada
Ler `README.md`, este arquivo, `contexto_ia/00_LEIA_PRIMEIRO.md`, `contexto_ia/estado_atual.md`, `contexto_ia/decisoes.md`, `contexto_ia/metodologia_provisoria.md`, `contexto_ia/provisionamento_ifrs9_4966.md`, o enunciado e o notebook principal. Aplicar as Skills relevantes em `skills/`.

## Identidade
- Projeto: `MLP-CNN-LSTM-estudo_risco_de_perda_em_operacoes_bancarias`
- GitHub: https://github.com/VTsilva/MLP-CNN-LSTM-estudo_risco_de_perda_em_operacoes_bancarias
- Notebook principal/entrega: `victor_silva_trabalho1.ipynb` na raiz.
- Target: `Credit`, previsão de um passo semanal.

## Regras obrigatórias
1. Preservar `data/raw/nfci-data-series-csv.csv` e o notebook original do professor.
2. Não inventar resultados, execuções, referências ou decisões. Separar confirmado, provisório e pendente.
3. `Credit` não é PD, LGD, EAD, default, inadimplência nem provisão. IFRS 9/CMN 4.966 é contexto de aplicação, não certificação deste modelo.
4. Particionar cronologicamente 70/20/10; scalers ajustados exclusivamente no treino.
5. Não utilizar o teste para escolher features, lookback, hiperparâmetros, arquitetura ou épocas.
6. Lookback 52 é o baseline principal do experimento comparativo; não afirmar sazonalidade anual. Janela descritiva e lookback supervisionado não são a mesma coisa.
7. Manter todos os imports em uma única célula com tag `central-imports`.
8. Para regressão contínua, não usar `accuracy` de classificação. Acompanhar MSE/loss e MAE; acurácia direcional é complementar.
9. Não substituir a inspeção das curvas de treino/validação por EarlyStopping automático. Cada arquitetura deve ter época selecionada e justificativa registrada em `resultados_execucao/selecao_epocas_retreinamento.csv`.
10. O treinamento diagnóstico e o retreinamento são fases distintas. A seleção já revisada pode ser carregada automaticamente; não exigir que o usuário edite dicionários ou flags manualmente. Se novas curvas forem geradas, reavaliar e atualizar o CSV com justificativas.
11. Multi-head: ramo independente por variável e concatenação; documentar entradas, ramos e saída.
12. ConvLSTM: adaptação da sequência em blocos temporais artificiais; explicitar que não há dimensão espacial natural.
13. Cada análise deve ter Markdown anterior (pergunta, motivação e método) e posterior (resultado, interpretação e impacto na próxima decisão).
14. Nomes internos e caminhos ASCII sem acentos; textos acadêmicos em português podem ter acentuação.
15. Em tarefa complexa, criar plano e atualizar contexto/Skills quando procedimento se consolidar.
16. Não fazer commit/push, não alterar o remoto e não descartar alterações sem autorização explícita.

## Arquiteturas implementadas
- Univariado: `mlp_1`, `mlp_2`, `cnn`, `lstm`, `stacked_lstm`, `bilstm`, `cnn_lstm`, `convlstm`.
- Multivariado: `mlp_1`, `mlp_2`, `mlp_multihead_1`, `cnn`, `cnn_multihead`, `lstm`, `stacked_lstm`, `bilstm`.
- Os modelos são regressões de saída única para o próximo `Credit`.

## Fluxo de treinamento
1. Reutilizar diagnósticos salvos quando target, features, lookback, épocas e hiperparâmetros coincidirem; caso contrário, executar diagnóstico com MSE/MAE em treino/validação, sem parada automática.
2. Consultar `resultados_execucao/interpretacao_diagnosticos.md` e `selecao_epocas_retreinamento.csv`; a seleção e justificativa por arquitetura devem estar rastreadas.
3. Retreinar desde inicialização nova usando o treino e as épocas registradas; o notebook está configurado para fazê-lo automaticamente.
4. Avaliar treino, validação e teste na escala original; selecionar arquiteturas pelo MAE de validação com métricas complementares.
5. Comparar com persistência; nunca declarar superioridade neural sem confrontar o baseline.

## Ambiente Python
- Versão de referência: CPython 3.14.x (64-bit), arquivo `.python-version`.
- Instalar com `python -m pip install -r requirements.txt`.
- TensorFlow é fixado em Release Candidate para suporte ao Python 3.14; documentar a versão realmente instalada na execução.

## Validação e comunicação
- Rodar `python tools/validate_notebook.py`.
- Validar estrutura e sintaxe; no ambiente do estudante, executar o notebook completo. Históricos existentes compatíveis devem ser reutilizados e os retreinamentos executados automaticamente.
- A execução dos 16 treinamentos exige TensorFlow e pode demorar conforme hardware.
- Toda entrega ZIP deve incluir: link, resumo, validações/limitações, lista completa de adicionados/modificados/removidos/renomeados e estado Git. Confirmar que nenhum push ocorreu.


## Estado empírico final (09/11/2026)
- Há resultados completos de treino/validação/teste para as 16 arquiteturas em `resultados_execucao/`.
- Melhor univariado pela validação: BiLSTM (MAE val 0,005171; teste 0,002368), superando persistência nas duas partições.
- Melhor multivariado pela validação: LSTM (MAE val 0,017032; teste 0,012216), pior que persistência nas duas partições.
- 52 semanas é escolha operacional fixa, não otimizada. Não declarar ótima ou sazonalidade.
- A execução original: Python 3.14.4, seed base 42, uma execução por arquitetura. TensorFlow/Keras e dispositivo não foram registrados; o manifesto explica a lacuna.
- Discussão e conclusão precisam permanecer Markdown estático, baseada em arquivos finais. É proibido reintroduzir gerador de conclusão em código ou arquivo `conclusao_automatica.md`.
- Antes de nova entrega, executar `python tools/validate_notebook.py` e `python tools/validate_results.py`. O teste neural separado é `python tools/test_neural_integration.py` em ambiente com TensorFlow.
- Para capturar ambiente/hash após nova execução: `python tools/capture_execution_provenance.py`.
