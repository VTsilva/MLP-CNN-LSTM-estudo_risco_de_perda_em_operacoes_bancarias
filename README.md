# MLP-CNN-LSTM — previsão de condições de crédito

**Título acadêmico:** Comparação de arquiteturas MLP, CNN e LSTM na previsão de condições de crédito: uma abordagem de séries temporais aplicada ao estudo do risco de perda em operações bancárias.

Repositório: https://github.com/VTsilva/MLP-CNN-LSTM-estudo_risco_de_perda_em_operacoes_bancarias

## Objetivo e delimitação
Comparar oito arquiteturas no experimento univariado e oito no multivariado para prever, em um passo à frente, o subíndice `Credit` do NFCI. O trabalho é contextualizado no risco de crédito e provisionamento, mas `Credit` **não** é PD, LGD, EAD, default, inadimplência nem provisão. O experimento não calcula perdas esperadas IFRS 9/CMN 4.966 nem valida modelo regulatório.

## Notebook principal
`victor_silva_trabalho1.ipynb` é o artefato acadêmico principal. Contém contexto financeiro/regulatório, EDA, preparação, benchmark de persistência e os fluxos completos dos 16 modelos.

## Estrutura
- `contexto_ia/`: memória documental consolidada.
- `planos_ia/`: planos de execução e histórico de tarefas.
- `skills/`: procedimentos reutilizáveis para agentes.
- `data/raw/`: CSV original; demais camadas Medallion só serão preenchidas quando houver transformação justificada.
- `arquivos_de_contexto/`: enunciado e materiais originais.
- `IMGs/`: imagens e gráficos selecionados.
- `resultados_execucao/`: curvas, históricos, interpretação dos diagnósticos, seleção documentada de épocas, métricas e previsões finais geradas pelo notebook.
- `versoes/`: snapshots históricos.

## Recriar o ambiente
Ambiente de referência: CPython 3.14.x (64-bit), conforme `.python-version` e `requirements.txt`. O TensorFlow utilizado neste ambiente é pré-lançamento (Release Candidate); preserve as versões instaladas ao reproduzir o experimento. O ambiente virtual não deve ser incluído no repositório/ZIP.

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# Linux/macOS: source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name nfci-timeseries --display-name "Python (NFCI Timeseries)"
```

Abra o notebook pela raiz do repositório e selecione o kernel `Python (NFCI Timeseries)`.

## Como executar os experimentos

1. Ative o ambiente Python 3.14.x e instale `requirements.txt`.
2. Abra o notebook pela raiz do repositório e execute todas as células de cima para baixo.
3. Os históricos de diagnóstico existentes serão reutilizados quando os parâmetros coincidirem. Para forçar novo diagnóstico, altere `FORCAR_REEXECUCAO_DIAGNOSTICOS = True` na célula de configuração.
4. As épocas e justificativas revistas já estão em `resultados_execucao/selecao_epocas_retreinamento.csv`. Não é necessário preencher dicionários, alterar épocas ou ativar flags: as células seguintes iniciam os retreinamentos automaticamente.
5. O notebook retreina automaticamente as 16 arquiteturas, gera previsões e avalia treino, validação e teste. O teste não participa da escolha dos vencedores.
6. Confira os artefatos em `resultados_execucao/avaliacao_*`, `comparacao_geral_metricas.csv`, `discussao_conclusao.md` e `proveniencia_execucao.json`. Salve o notebook com outputs e preserve a pasta de resultados ao compartilhar o ZIP.

**Importante:** não use `accuracy` de classificação para `Credit`, que é contínuo. O notebook acompanha MSE (loss) e MAE; acurácia direcional aparece apenas como métrica complementar. Caso o professor tenha uma definição específica de acurácia para regressão, confira o material IAD-012.

## Convenções experimentais
- 70% treino, 20% validação, 10% teste em ordem cronológica.
- Um passo à frente; target sempre `Credit`.
- Lookback fixo de 52 semanas, igual para todos os modelos, como escolha operacional para padronizar arquitetura. Não é ótimo validado e não implica sazonalidade anual; não foram treinadas redes com outros lookbacks.
- Scalers ajustados somente no período de treino.
- `shuffle=True` embaralha a ordem de janelas completas de treino; não embaralha a série bruta nem a ordem temporal dentro da janela.
- Diagnóstico sem EarlyStopping para permitir inspeção das curvas.
- Seleção de épocas registrada com justificativa por modelo; retreinamento com pesos reinicializados e número de épocas selecionado.
- Benchmark de persistência `Credit[t+1] = Credit[t]` obrigatório para interpretar o valor agregado das redes.

## Resultados gerados
O notebook preserva históricos, curvas, seleção de épocas, métricas, previsões e discussão/conclusão acadêmicas escritas em Markdown em `resultados_execucao/` e no próprio notebook. Ao devolver o projeto para interpretação, inclua o notebook executado e essa pasta. Não compartilhe a `.venv`.

## Validação técnica
```bash
python tools/validate_notebook.py
```

O GitHub Actions mantém um job leve para validar estrutura do notebook e consistência dos CSVs. Um segundo workflow, manual/agendado, executa um smoke test de uma época por arquitetura com TensorFlow; ele não substitui a execução acadêmica completa.

Após executar o notebook, registre o ambiente com `python tools/capture_execution_provenance.py`. Para esta execução recebida, Python 3.14.4 foi identificado pelo metadado do kernel; TensorFlow/Keras e dispositivo não estavam gravados. Uma execução por seed/modelo foi realizada.

## Continuidade com agentes
Começar por `AGENTS.md` e `contexto_ia/00_LEIA_PRIMEIRO.md`. Aplicar as Skills pertinentes. Em toda transição de ZIP, listar caminhos adicionados, modificados, removidos e renomeados. Não fazer commit ou push sem autorização explícita.
