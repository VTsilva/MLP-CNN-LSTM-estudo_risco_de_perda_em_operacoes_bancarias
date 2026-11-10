# Resultados da execução concluída

Os arquivos `diagnostico_univariado/` e `diagnostico_multivariado/` contêm históricos e curvas das 16 arquiteturas. As pastas `avaliacao_univariado/` e `avaliacao_multivariado/` contêm métricas e previsões de treino, validação e teste após retreinamento.

- `comparacao_geral_metricas.csv`: tabela consolidada com 54 linhas (16 modelos × 3 partições + persistência × 3 partições por experimento).
- `selecao_epocas_retreinamento.csv`: épocas selecionadas e justificativas.
- `interpretacao_diagnosticos.md`: interpretação das curvas diagnósticas.
- `discussao_conclusao.md`: discussão e conclusão acadêmicas estáticas, escritas a partir dos resultados recebidos.
- `proveniencia_execucao.json`: metadados recuperados, hashes dos dados/fontes e lacunas da execução original.

Não existe conclusão gerada automaticamente. A conclusão formal está em Markdown no notebook.

Valide os resultados com `python tools/validate_results.py`. Em próximas execuções, capture ambiente e hashes completos com `python tools/capture_execution_provenance.py`.
