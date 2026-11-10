# Estado atual do projeto

Data da atualização: 09/11/2026.

## Entrega acadêmica
- Notebook principal: `victor_silva_trabalho1.ipynb` na raiz.
- O notebook contém EDA, preparação, benchmark de persistência, oito arquiteturas univariadas, oito multivariadas, métricas em treino/validação/teste, discussão e conclusão redigidas em Markdown estático.
- `resultados_execucao/interpretacao_diagnosticos.md` consolida a leitura das curvas, épocas escolhidas e resultados finais; `discussao_conclusao.md` espelha as seções finais estáticas do notebook.
- A conclusão **não é gerada por código**. A célula de síntese automática e o arquivo `conclusao_automatica.md` foram removidos; o texto final está em Markdown no notebook e em cópia documental estática em `resultados_execucao/discussao_conclusao.md`.

## Resultados efetivamente recebidos
- Diagnósticos: 8 modelos univariados e 8 multivariados, até 100 épocas por modelo.
- Retreinamentos: 8 modelos univariados e 8 multivariados, com pesos reinicializados e épocas selecionadas a partir das curvas de validação.
- Métricas: 24 linhas por abordagem (8 modelos × treino/validação/teste), mais benchmark de persistência no arquivo consolidado.
- Previsões: 22.888 linhas por abordagem, sem chaves duplicadas; 1.987 alvos de treino, 582 de validação e 292 de teste por modelo.
- Todos os arquivos de métricas e previsões estão presentes em `resultados_execucao/avaliacao_univariado/` e `avaliacao_multivariado/`.

## Conclusão empírica
- Melhor univariado pela MAE de validação: BiLSTM, MAE 0,005171 e RMSE 0,007501; no teste, MAE 0,002368 e RMSE 0,003123.
- Benchmark de persistência: MAE 0,011082 na validação e 0,005188 no teste. A BiLSTM reduz a MAE em 53,34% e 54,36%, respectivamente.
- Melhor multivariado pela MAE de validação: LSTM, MAE 0,017032 e RMSE 0,022459; no teste, MAE 0,012216 e RMSE 0,014274. Não supera persistência em nenhuma das duas partições.
- A MAE do melhor multivariado é 229,39% maior que a do melhor univariado na validação.
- Interpretação: nesta amostra, horizonte, features e configurações, a inclusão de Risk, Leverage e Nonfinancial_Leverage não adicionou informação preditiva incremental suficiente sobre o histórico de Credit.

## Decisões metodológicas e limitações
- Lookback de 52 semanas fica **fixo como escolha operacional comum**, não como ótimo validado e não como evidência de sazonalidade anual. Não foi feita comparação de performance com lookbacks 13, 26 e 104.
- Uma única execução/seed por arquitetura; não houve repetição com várias seeds nem validação de origem móvel.
- 10/16 diagnósticos tiveram o melhor ponto em 99 ou 100 épocas; esses casos atingiram o limite do diagnóstico e não demonstram convergência completa.
- Teste é período mais calmo: desvio-padrão do target aproximadamente 0,1113, contra 0,1875 na validação. Comparar erros absolutos entre partições requer essa ressalva.
- `Credit` é um indicador agregado de condições de crédito dos EUA, não PD, LGD, EAD, default ou provisão. IFRS 9/CMN 4.966 são contexto, não validação regulatória do modelo.
- A acurácia direcional é complementar; para persistência a previsão é sempre direção zero, fazendo a taxa de acerto refletir principalmente a proporção de observações sem variação.

## Reprodutibilidade
- Kernel notebook: Python 3.14.4 (metadata do notebook).
- TensorFlow estava disponível, mas a versão efetiva, a versão Keras e o dispositivo não foram capturados na execução original.
- SHA-256 do CSV e hash das fontes do notebook estão em `resultados_execucao/proveniencia_execucao.json`.
- Para capturar versões completas em futuras execuções, executar `python tools/capture_execution_provenance.py` depois do notebook.
- Cada modelo foi executado uma vez, seed base 42 com derivação por posição do modelo.

## CI
- Job leve: valida estrutura/sintaxe do notebook e consistência dos CSVs de resultados em push/PR/manual.
- Job neural separado: disparo manual ou agendado, instala TensorFlow e realiza um treino de uma época para cada uma das 16 arquiteturas com dados sintéticos mínimos. Não executa os treinamentos acadêmicos completos.

## Estado de versionamento
- O `.git` e o `origin` foram preservados a partir do ZIP recebido.
- Nenhum commit ou push foi executado durante esta atualização.
