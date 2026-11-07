# Estado atual do projeto

**Última atualização:** 07/11/2026.

## Resumo executivo

A estrutura de diretórios foi criada. O notebook de referência do professor e o CSV original do NFCI estão armazenados. A base foi inspecionada programaticamente: possui 2.913 observações semanais e sete colunas, sem valores ausentes, datas duplicadas ou intervalos semanais irregulares. O target definido pelo responsável pelo projeto é `Credit`.

Ainda não foram executadas a análise exploratória, a preparação das camadas Bronze/Silver/Gold, a modelagem ou a avaliação dos modelos.

## Arquivos existentes

| Caminho | Conteúdo | Situação |
|---|---|---|
| `arquivos_de_contexto/trabalho 1 previsao univariada e multivariada passo unico.ipynb` | Roteiro original do professor | Preservado, não alterado |
| `data/raw/nfci-data-series-csv.csv` | CSV original com as séries NFCI | Preservado, não alterado |
| `data/bronze/` | Dados importados/padronizados | Ainda sem dados derivados |
| `data/silver/` | Dados tratados e validados | Ainda sem dados derivados |
| `data/gold/` | Dados finais para modelagem | Ainda sem dados derivados |
| `contexto_ia/` | Documentação inicial | Criada |
| `planos_ia/` | Diretrizes e modelo de plano | Criados; nenhum plano de execução específico concluído |
| `skills/` | Diretrizes e modelo de Skill | Criados; nenhuma Skill operacional criada |
| `IMGs/` | Materiais visuais | Diretório criado, sem artefatos |

## Verificação técnica do CSV original

- Arquivo: `data/raw/nfci-data-series-csv.csv`.
- Dimensão: **2.913 linhas × 7 colunas** (incluindo a coluna de data).
- Colunas: `Friday_of_Week`, `NFCI`, `ANFCI`, `Risk`, `Credit`, `Leverage`, `Nonfinancial_Leverage`.
- Primeira observação: **08/01/1971**.
- Última observação: **30/10/2026**.
- Frequência: semanal, com intervalo de sete dias entre observações consecutivas.
- Datas duplicadas: nenhuma.
- Valores ausentes: nenhum nas sete colunas.
- Datas inválidas na interpretação utilizada: nenhuma.
- Ordenação: cronológica crescente.

**Atenção ao formato de data:** o arquivo utiliza `MM/DD/YYYY`. Por exemplo, `01/08/1971` significa 8 de janeiro de 1971, e não 1º de agosto. Ao importar com pandas, usar explicitamente `format='%m/%d/%Y'` (ou estratégia equivalente claramente validada).

Essas verificações descrevem o arquivo recebido neste projeto; devem ser repetidas no início do pipeline para garantir a integridade do arquivo efetivamente utilizado em cada execução.

## Requisitos já identificados no notebook do professor

O notebook contém 76 células e apresenta um roteiro com:

1. Download/descrição, subamostragem e limpeza.
2. Análise estatística, gráficos, identificação de tendências/ciclos e divisão temporal 70%/20%/10%.
3. Previsão univariada de um passo à frente e comparação de modelos.
4. Previsão multivariada de saída única e um passo à frente.
5. Discussão comparativa entre abordagens univariada e multivariada.
6. Etapa opcional de críticas e sugestões.

A especificação dos modelos está resumida em `metodologia_provisoria.md`; o notebook original é a referência integral.

## Próximas atividades ainda não executadas

- Confirmar as variáveis de entrada do experimento multivariado.
- Fazer EDA e documentar tendências, ciclos, distribuição, correlações e autocorrelação.
- Definir janela temporal e estratégia de criação das sequências.
- Definir métricas de avaliação compatíveis com regressão e alinhadas às orientações da disciplina.
- Implementar o pipeline de dados e produzir as camadas Bronze, Silver e Gold.
- Desenvolver a cópia de trabalho do notebook.
- Treinar e comparar os modelos.
- Consolidar o notebook final e conferir os critérios de entrega.
