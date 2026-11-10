# Plano concluído — fechamento da comparação e robustez documental

- **Data:** 09/11/2026
- **Entrada:** ZIP executado enviado pelo responsável em 09/11/2026.
- **Objetivo:** interpretar os 16 retreinamentos, concluir a comparação e resolver lacunas de lookback, proveniência, CI e referências.

## Evidências revisadas
- 24 métricas por abordagem (8 arquiteturas × 3 partições), 54 linhas no consolidado incluindo baselines; 22.888 previsões por abordagem.
- Univariado: BiLSTM selecionada por MAE de validação 0,005171; MAE teste 0,002368; supera persistência por 53,34% na validação e 54,36% no teste.
- Multivariado: LSTM selecionada por validação, mas MAE 0,017032 na validação e 0,012216 no teste, pior que persistência (0,011082 e 0,005188).
- Teste tem desvio-padrão do target 0,1113, abaixo da validação 0,1875.

## Decisões
1. Manter lookback 52 fixo como escolha operacional comum; não alegar ótimo. Não executar varredura de lookbacks neste fechamento.
2. Registrar uma execução por modelo e ausência de múltiplas seeds/rolling origin como limitação.
3. Salvar hash SHA-256 do CSV e fingerprint do código; capturar ambiente completo em execução futura por script.
4. Separar CI leve e integração neural manual/agendada.
5. Substituir conclusão automática por discussão e conclusão estáticas em Markdown.
6. Completar referências sem inventar autoria/data do material da disciplina.

## Critérios de aceite
- Notebook tem discussão e conclusão Markdown estáticas e referências sem placeholders.
- CSVs e previsões passam validação estrutural.
- Integração neural executa construtores e um treino curto por arquitetura no workflow separado.
- Git metadata preservado; nenhum commit/push.
