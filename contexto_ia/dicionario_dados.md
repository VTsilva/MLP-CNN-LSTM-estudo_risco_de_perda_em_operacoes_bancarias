# Dicionário de dados — NFCI

Arquivo: `data/raw/nfci-data-series-csv.csv`. Frequência: semanal, referência sexta-feira. Target: `Credit`.

| Coluna | Descrição | Observação |
|---|---|---|
| `Friday_of_Week` | Data da semana | Datas no formato americano no CSV Raw |
| `NFCI` | Índice agregado de condições financeiras | Combina múltiplos indicadores; não usar no primeiro desenho multivariado |
| `ANFCI` | NFCI ajustado por condições de atividade e inflação | Índice agregado; excluir do primeiro desenho pela sobreposição |
| `Risk` | Subíndice de risco | Feature candidata; não equivale a probabilidade de default |
| `Credit` | Subíndice das condições dos mercados de crédito | Target; não equivale a taxa de default, PD ou LGD |
| `Leverage` | Subíndice de alavancagem | Feature candidata; sinal padronizado de condições, não montante de dívida em unidade monetária |
| `Nonfinancial_Leverage` | Subíndice de alavancagem não financeira | Feature candidata; famílias e empresas não financeiras |

No snapshot verificado: 2.913 observações, 1971-01-08 a 2026-10-30, sem dados ausentes, datas duplicadas ou intervalos semanais irregulares. Os valores são índices padronizados, não percentuais nem unidades monetárias. O produtor pode revisar observações históricas; preservar o CSV original e registrar a data de extração.
