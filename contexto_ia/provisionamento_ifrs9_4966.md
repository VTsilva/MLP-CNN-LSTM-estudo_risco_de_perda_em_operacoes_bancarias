# Contexto regulatório: provisionamento, IFRS 9 e Resolução CMN 4.966

## Objetivo deste documento

Oferecer o contexto bancário que motiva o estudo, sem atribuir ao dataset ou ao modelo uma finalidade regulatória que eles não possuem.

## Perdas de crédito esperadas

A IFRS 9 introduziu um modelo de perdas de crédito esperadas (*Expected Credit Loss — ECL*). A mensuração considera valores ponderados por probabilidade, valor do dinheiro no tempo e informações razoáveis e sustentáveis sobre eventos passados, condições atuais e previsões econômicas. O modelo geral diferencia estágios de risco: estágio 1 (perdas associadas a eventos de default possíveis nos próximos 12 meses), estágio 2 (perdas esperadas ao longo da vida após aumento significativo do risco de crédito) e estágio 3 (ativos *credit-impaired*, com perdas esperadas ao longo da vida).

A perda esperada de 12 meses do estágio 1 não significa que só se consideram fluxos de caixa perdidos nos próximos 12 meses. Refere-se às perdas ao longo da vida do instrumento que decorrem de eventos de default possíveis nos próximos 12 meses.

## Brasil: Resolução CMN 4.966/2021

A Resolução CMN nº 4.966/2021 estabelece critérios contábeis aplicáveis às instituições financeiras e demais instituições autorizadas a funcionar pelo Banco Central, no escopo definido pela norma. Não deve ser descrita como simples tradução jurídica da IFRS 9. A aplicação geral teve início em 1º de janeiro de 2025, observadas disposições e transições específicas.

Pontos úteis para a narrativa:

- Art. 40: a avaliação considera a probabilidade de o instrumento se tornar ativo problemático e a expectativa de recuperação. A estimativa deve considerar, entre outros elementos, custos, garantias, valor presente, taxas históricas de recuperação e previsões econômicas.
- Art. 47: estabelece os estágios e o horizonte de reconhecimento das perdas esperadas.
- Art. 48: prevê revisão periódica da estimativa conforme a regra aplicável.

Na consulta desta atualização, a página consolidada do Banco Central identifica a versão vigente como atualizada em 29/08/2025 e lista, entre as alterações, a Resolução CMN nº 5.244/2025 (vigente desde 01/09/2025). Antes da entrega acadêmica, consultar novamente a página oficial para confirmar se houve atualização posterior e citar a versão efetivamente acessada.

## Modelagem de risco: PD, LGD e EAD

Uma decomposição didática usual é `EL ≈ PD × LGD × EAD`:

- PD: probabilidade de default.
- LGD: proporção da exposição que não será recuperada após o default.
- EAD: exposição estimada no momento do default.

É uma decomposição de modelagem, não uma fórmula que, isoladamente, esgota os requisitos de ECL. O processo regulatório pode envolver cenários macroeconômicos prospectivos, desconto, dados de carteira e critérios de estágio.

Técnicas podem incluir regressão logística e ensembles para PD; modelos de recuperação, regressões de severidade, modelos Beta ou modelos de sobrevivência para LGD; modelos de conversão de limite/exposição para EAD; e modelos econométricos ou de séries temporais para cenários macroeconômicos. As normas não prescrevem MLP, CNN ou LSTM.

## Relação correta com o projeto

O dataset do Chicago Fed contém o NFCI e subíndices, incluindo `Credit`, `Risk`, `Leverage` e `Nonfinancial_Leverage`. `Credit` representa condições agregadas dos mercados de crédito dos Estados Unidos. Não é default, inadimplência, PD, LGD, EAD ou provisão.

O estudo pode demonstrar uma tarefa de previsão de indicador macrofinanceiro que ilustra como séries de condições financeiras podem ser analisadas como informação complementar ao contexto macroeconômico de risco. Não pode afirmar que estima perdas contábeis, atende diretamente à IFRS 9/Resolução 4.966 ou é transferível para uma carteira brasileira sem dados e validações adicionais.

## Fontes oficiais

- IFRS Foundation, IFRS 9 Financial Instruments (2024 issued standards): https://www.ifrs.org/content/dam/ifrs/publications/pdf-standards/english/2024/issued/part-a/ifrs-9-financial-instruments.pdf
- Banco Central do Brasil, Resolução CMN nº 4.966/2021 (versão consolidada): https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?numero=4966&tipo=RESOLU%C3%87%C3%83O+CMN
- Banco Central do Brasil, Resolução CMN nº 5.244/2025, que altera a Resolução 4.966: https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?numero=5244&tipo=Resolu%C3%A7%C3%A3o+CMN
- Banco Central do Brasil, transição dos impactos do IFRS 9 no capital regulatório: https://www.bcb.gov.br/detalhenoticia/ (consultar nota institucional vinculada à Resolução CMN 4.966 e à Resolução BCB 352; confirmar URL específica antes da citação final)
- Chicago Fed, metodologia NFCI: https://www.chicagofed.org/research/data/nfci/about
