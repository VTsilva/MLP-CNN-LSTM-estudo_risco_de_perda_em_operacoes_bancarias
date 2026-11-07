# Dicionário de dados — NFCI

## Identificação do arquivo

- Arquivo original: `data/raw/nfci-data-series-csv.csv`.
- Fonte institucional indicada: Federal Reserve Bank of Chicago.
- Página de dados: https://www.chicagofed.org/research/data/nfci/current-data
- Frequência: semanal.
- Período observado no arquivo recebido: 08/01/1971 a 30/10/2026.
- Formato de data do CSV: `MM/DD/YYYY`.
- Dimensão verificada: 2.913 observações e sete colunas.

## Colunas

| Nome no CSV | Descrição resumida | Papel no projeto |
|---|---|---|
| `Friday_of_Week` | Data de referência semanal, associada à sexta-feira da semana. | Índice temporal. |
| `NFCI` | National Financial Conditions Index, indicador agregado das condições financeiras dos EUA. | Não incluir no primeiro modelo multivariado; estudar redundância. |
| `ANFCI` | Adjusted National Financial Conditions Index, versão ajustada do NFCI para considerar condições macroeconômicas. | Não incluir no primeiro modelo multivariado; estudar redundância. |
| `Risk` | Subíndice relacionado à dimensão de risco das condições financeiras. | Feature multivariada candidata. |
| `Credit` | Credit Subindex, subíndice das condições do mercado de crédito. | Target escolhido. |
| `Leverage` | Subíndice relacionado às condições de alavancagem. | Feature multivariada candidata. |
| `Nonfinancial_Leverage` | Subíndice de alavancagem do setor não financeiro, abrangendo famílias e empresas não financeiras. | Feature multivariada candidata. |

## Interpretação geral dos índices

Os indicadores do NFCI são construídos para resumir condições financeiras relativas à média histórica. Em termos gerais, valores positivos indicam condições mais restritivas que a média e valores negativos indicam condições mais flexíveis. A interpretação específica de cada componente deve seguir a documentação oficial do Chicago Fed.

O NFCI é um índice agregado; o ANFCI é uma versão ajustada para o contexto macroeconômico. `Risk`, `Credit` e `Leverage` são dimensões/subíndices. `Nonfinancial_Leverage` detalha a alavancagem de agentes não financeiros.

## Variável-alvo

`Credit` foi escolhida para representar o comportamento das condições de crédito. O modelo deverá prever o próximo valor semanal de `Credit`.

## Features candidatas

Para o primeiro experimento multivariado, a proposta é utilizar o histórico de:

- `Credit` (defasagens da própria variável-alvo);
- `Risk`;
- `Leverage`;
- `Nonfinancial_Leverage`.

A seleção é provisória e deverá ser confirmada após EDA e avaliação de colinearidade/redundância.

## Cautela de interpretação

Os indicadores compartilham fundamentos e podem apresentar dependência estrutural. Não assumir independência estatística entre as colunas. Em especial, o NFCI agregado tem relação de composição com seus subíndices; incluir o agregado para prever um de seus próprios componentes pode criar informação redundante ou uma relação parcialmente mecânica.

O arquivo CSV, isoladamente, não contém documentação completa da metodologia de construção. Para interpretações definitivas, consultar as referências oficiais listadas em `referencias.md`.
