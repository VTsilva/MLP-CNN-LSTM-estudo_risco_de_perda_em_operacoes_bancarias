# Dados — arquitetura Medallion

Os dados serão organizados em camadas, preservando a origem e a rastreabilidade de cada transformação.

- `raw/`: cópias originais obtidas da fonte, sem tratamento. Não sobrescrever.
- `bronze/`: ingestão técnica, parsing de datas, tipagem e padronização inicial, preservando os valores de origem.
- `silver/`: dados validados e tratados, com regras documentadas e seleção das colunas necessárias.
- `gold/`: conjuntos finais específicos para EDA/modelagem, incluindo features, target e partições quando aplicável.

Cada transformação deverá ter origem, regras, data de execução e destino documentados. Não ajustar scalers ou outros transformadores usando validação ou teste.
