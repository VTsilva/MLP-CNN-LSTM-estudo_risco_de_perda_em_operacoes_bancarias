# Registro de decisões e premissas

| ID | Tema | Decisão/entendimento | Status | Observação |
|---|---|---|---|---|
| D-001 | Tema | Previsão de condições de crédito no contexto de risco bancário/provisionamento | Confirmado | Motivação, não promessa de modelo regulatório |
| D-002 | Repositório | `MLP-CNN-LSTM-estudo_risco_de_perda_em_operacoes_bancarias` | Confirmado | GitHub pessoal do responsável |
| D-003 | Target | `Credit` | Confirmado | Não é LGD, PD nem taxa de inadimplência |
| D-004 | Fonte | Chicago Fed NFCI, CSV em `data/raw/` | Confirmado | Preservar snapshot original |
| D-005 | Frequência | Semanal, sextas-feiras | Verificado | 2.913 registros completos no snapshot |
| D-006 | Horizonte | Um passo à frente | Confirmado | Exigência do trabalho |
| D-007 | Partições | 70% treino, 20% validação, 10% teste, cronológicas | Confirmado | Teste não orienta escolhas |
| D-008 | Features multivariadas | `Credit`, `Risk`, `Leverage`, `Nonfinancial_Leverage` | Confirmado para o experimento executado | As variáveis adicionais foram testadas, mas não geraram ganho sobre persistência; isso não prova irrelevância em outras especificações |
| D-009 | Índices agregados | Excluir `NFCI` e `ANFCI` do primeiro desenho | Provisório | Redundância/sobreposição estrutural; estudo separado pode ser avaliado |
| D-010 | Lookback | 52 semanas fixas em todos os modelos como escolha operacional de contexto anual aproximado | Confirmado para este trabalho | Não houve teste de performance com 13, 26 ou 104; não chamar 52 de ótimo nem afirmar sazonalidade anual |
| D-011 | Janela descritiva | Média/desvio móvel de 52 semanas para visualizar nível e volatilidade local | Confirmado como descritiva | Não equivale ao lookback de entrada do modelo |
| D-012 | Escalonamento | Ajustar scaler somente com treino | Diretriz obrigatória | Aplicar parâmetros à validação/teste sem reajuste |
| D-013 | Arquiteturas univariadas | 8 modelos definidos no roteiro | Confirmado | Lista no contexto metodológico |
| D-014 | Arquiteturas multivariadas | 8 modelos definidos no roteiro | Confirmado | Lista no contexto metodológico |
| D-015 | Épocas | Inspeção manual de curvas treino/validação | Confirmado | Não substituir por early stopping automático |
| D-016 | Métricas | MAE/MSE/RMSE, R² e acurácia direcional complementar | Implementado com ressalva | `accuracy` de classificação não se aplica diretamente ao target contínuo; conferir eventual definição específica de IAD-012 se exigida pelo docente |
| D-017 | Embaralhamento | Apenas ordem de janelas completas de treino; não embaralhar série bruta nem janelas internas | Provisório | Confirmar interpretação com aula |
| D-018 | Entrega | Um notebook `.ipynb` final | Confirmado | Estrutura auxiliar não substitui entrega |
| D-019 | Contexto regulatório | IFRS 9 e Resolução CMN 4.966 contextualizam ECL e provisões | Confirmado | Não afirmar que a norma prescreve MLP/CNN/LSTM |
| D-020 | Importações | Uma única célula de imports no notebook | Padrão do projeto | Células de código posteriores não devem conter import |
| D-021 | Repositório | Identificadores internos e caminhos sem acentos | Padrão do projeto | Textos acadêmicos podem manter acentuação |
| D-022 | Git | Não executar commit/push sem pedido explícito | Confirmado | Preservar histórico e mudanças locais |

## Pendências e limitações ainda abertas
- A definição específica de “acurácia” usada pelo docente em IAD-012 não foi confirmada. O notebook utiliza métricas adequadas à regressão e reporta acurácia direcional apenas como complemento; não aplica accuracy de classificação a um target contínuo.
- Não foi feita sensibilidade de desempenho para lookbacks 13, 26 e 104 semanas. A janela 52 permanece fixa e operacional, sem alegação de otimalidade.
- Não foram executadas múltiplas seeds nem validação temporal de origem móvel; estabilidade entre inicializações e origens não foi quantificada.
- O enunciado didático deve ser consultado caso haja exigência adicional sobre embaralhamento das janelas ou definições específicas de métricas que não esteja refletida no notebook.

| D-023 | Loss/metric | MSE como loss; MAE como métrica de acompanhamento; avaliação final MAE/MSE/RMSE/R² e direção | Implementado | Não utilizar accuracy de classificação para target contínuo; confirmar definição da disciplina |
| D-024 | Arquiteturas | Construtores executáveis para as 16 arquiteturas listadas no enunciado | Implementado | Multi-head por ramo de variável; parâmetros iniciais documentados em metodologia |
| D-025 | ConvLSTM | ConvLSTM2D com janela 52 reorganizada em 13 blocos de 4 semanas | Implementado com ressalva | Eixo espacial é representação artificial; destacar como limitação |
| D-026 | Épocas | Diagnóstico até 100 épocas sem EarlyStopping; seleção registrada após inspeção e justificativa por arquitetura | Implementado | Casos com mínimo em 99/100 atingiram o limite; ver D-033 e relatório de diagnóstico |
| D-027 | Retreinamento | Recriar modelo com seed controlada e treinar no bloco treino pelo número de épocas selecionado e justificado | Implementado | O notebook carrega o CSV de seleção e executa automaticamente, sem flags ou dicionários manuais |
| D-028 | Resultados | Exportar históricos, curvas, métricas e previsões em `resultados_execucao/` | Implementado | Pasta deve acompanhar notebook devolvido para interpretação |


| D-029 | Diagnósticos recebidos | 16 históricos de diagnóstico interpretados e comparados com retreinamentos finais | Confirmado | Relatório em `resultados_execucao/interpretacao_diagnosticos.md` contém curvas, épocas selecionadas e métricas finais |
| D-030 | Épocas selecionadas | Registrar seleção e justificativa por arquitetura em CSV | Implementado | Critério ancorado no menor `val_loss` e inspeção das curvas; ver `selecao_epocas_retreinamento.csv` |
| D-031 | Retreinamento | Automatizar a execução após carregar seleção registrada | Implementado | Não exigir preenchimento manual de dicionários ou flags |
| D-032 | Reutilização dos diagnósticos | Carregar históricos existentes se configuração coincidir | Implementado | Evita repetir os 16 diagnósticos; `FORCAR_REEXECUCAO_DIAGNOSTICOS=True` força novo diagnóstico |
| D-033 | Diagnóstico limitado a 100 épocas | Assinalar como limitação casos com menor `val_loss` nas épocas 99/100 | Confirmado | Melhor ponto observado não equivale a convergência; se requisito exigir plateau/overfit, estender diagnósticos |
| D-034 | Resultado final | BiLSTM univariada supera persistência em validação e teste; nenhuma arquitetura multivariada supera persistência | Confirmado | Métricas finais nas mesmas partições; ver tabelas CSV e discussão/conclusão estáticas |
| D-035 | Ambiente | Python 3.14.x como referência atual | Confirmado | `.python-version` e `requirements.txt`; TensorFlow 2.22.0rc0 é pré-lançamento para suporte ao Python 3.14 e deve ser registrado em cada execução |


| D-036 | Lookback final | Manter 52 semanas como parâmetro fixo para comparação de arquiteturas | Confirmado | A tabela de 13/26/52/104 ilustra apenas o custo amostral; a sensibilidade de desempenho ficou fora do escopo executado |
| D-037 | Reprodutibilidade | Registrar SHA-256 dos dados e fontes do notebook; capturar Python, TensorFlow, Keras, plataforma e dispositivos nas próximas execuções | Implementado parcialmente | Execução recebida identifica Python 3.14.4, seed base 42 e dados; TensorFlow/Keras e dispositivo não foram registrados retrospectivamente |
| D-038 | Repetições | Uma execução por arquitetura é a evidência disponível | Limitação registrada | Múltiplas seeds e avaliação rolling-origin não foram executadas; estabilidade entre inicializações não foi quantificada |
| D-039 | Conclusão | Conclusão e discussão acadêmicas devem ser Markdown estático escrito a partir dos resultados | Confirmado | Não gerar conclusão por função Python; `conclusao_automatica.md` removido |
| D-040 | CI neural | Adicionar smoke test separado e acionável manualmente/agendado para testar construtores e um treino curto das 16 arquiteturas | Implementado | Não substitui a execução integral do experimento acadêmico |

| D-041 | Resultado univariado | BiLSTM selecionada por menor MAE de validação (0,005171); MAE teste 0,002368 | Confirmado | Redução de MAE vs. persistência: 53,34% na validação e 54,36% no teste |
| D-042 | Resultado multivariado | LSTM foi a melhor arquitetura multivariada pela validação, mas não superou persistência | Confirmado | MAE 0,017032 na validação e 0,012216 no teste; persistência 0,011082 e 0,005188 |
| D-043 | Conclusão acadêmica | Discussão e conclusão mantidas como Markdown estático no notebook | Confirmado | Sincronizadas com `resultados_execucao/discussao_conclusao.md`; conclusão automática em código removida |
