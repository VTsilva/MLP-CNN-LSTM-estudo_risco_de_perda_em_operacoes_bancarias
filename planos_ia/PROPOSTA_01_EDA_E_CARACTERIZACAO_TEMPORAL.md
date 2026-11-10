# Proposta 01 — EDA e caracterização temporal do dataset NFCI

- **Data de elaboração:** 07/11/2026
- **Status:** Em andamento — EDA inicial executada no notebook principal; interpretação e camadas derivadas ainda pendentes
- **Responsável:** A definir

## 1. Objetivo

Caracterizar o dataset semanal do NFCI, com foco no target `Credit`, para produzir evidências sobre qualidade, comportamento temporal, tendências/ciclos e dependências que apoiem a escolha da janela móvel e das variáveis multivariadas.

## 2. Contexto e decisões relacionadas

Consultar:
- `contexto_ia/visao_geral.md`
- `contexto_ia/estado_atual.md`
- `contexto_ia/decisoes.md`
- `contexto_ia/dicionario_dados.md`
- `contexto_ia/metodologia_provisoria.md`
- `AGENTS.md`

A fonte original é `data/raw/nfci-data-series-csv.csv`. O target é `Credit`.

## 3. Escopo

### Incluído

1. Ingestão técnica do CSV em Bronze, sem modificar Raw.
2. Conversão de datas e tipagem validada.
3. Estatísticas descritivas e auditoria de qualidade.
4. Gráficos temporais do target e das features candidatas.
5. Tendência, médias móveis, variabilidade móvel e mudanças de regime, quando apropriado.
6. Análise de ciclos/sazonalidade sem pressuposições; ACF/PACF e testes de estacionariedade, se úteis.
7. Correlações contemporâneas e defasadas entre variáveis, sem interpretação causal.
8. Recomendações documentadas para janela temporal e desenho multivariado, mantendo decisões ainda pendentes.

### Fora do escopo

- Treinamento de MLP, CNN ou LSTM.
- Escolha final de hiperparâmetros.
- Utilização do conjunto de teste para seleção de features/janela.
- Alegações de previsão direta de LGD ou causalidade.

## 4. Entradas e saídas

| Tipo | Caminho | Descrição |
|---|---|---|
| Entrada | `data/raw/nfci-data-series-csv.csv` | Fonte original, imutável |
| Notebook de trabalho | Raiz do projeto ou diretório de notebooks aprovado | EDA reproduzível |
| Saída | `data/bronze/` | Dados ingeridos e padronizados |
| Saída | `data/silver/` | Dataset validado para análise |
| Saída | `IMGs/eda/` | Gráficos exportados quando úteis |
| Saída | `contexto_ia/estado_atual.md` | Registro do que foi executado |
| Saída | `contexto_ia/decisoes.md` | Novas decisões, se aprovadas |

## 5. Etapas e situação atual

1. Conferir estado Git, arquivos e integridade do Raw.
2. Ingerir e converter `Friday_of_Week` usando `%m/%d/%Y`.
3. Validar ordenação, frequência semanal, duplicatas, nulos e tipos.
4. Gerar estatísticas descritivas de todas as variáveis.
5. Plotar as séries em escalas legíveis e detalhar `Credit`.
6. Investigar tendências, ciclos e autocorrelação.
7. Analisar correlações e relações defasadas, com cautela quanto a colinearidade e não causalidade.
8. Avaliar estacionariedade e transformações apenas se necessárias e justificadas.
9. Documentar evidências e propostas sobre janela e features.
10. Atualizar estado, decisões e o próprio plano com resultados reais.

## 6. Critérios de conclusão

- Código executável e resultados reproduzíveis.
- Raw preservado.
- Transformações e schemas documentados.
- Gráficos com títulos, eixos, unidades e datas legíveis.
- Separação explícita entre observações, hipótese e interpretação.
- Recomendações de janela/features justificadas por evidência, sem decisões silenciosas.

## 7. Riscos e dependências

- Mudanças/vintages do dataset podem afetar reprodutibilidade; preservar CSV usado.
- Correlações entre subíndices não implicam causalidade.
- Tendência e ciclos de longo prazo podem exigir visualizações de diferentes escalas.
- O uso de indicadores agregados pode gerar relações mecânicas; `NFCI` e `ANFCI` não devem ser incluídos automaticamente.
- A métrica “acurácia” do curso ainda precisa de esclarecimento para regressão.

## 8. Registro de execução

EDA inicial executada em `victor_silva_trabalho1.ipynb`; as saídas geradas estão armazenadas no notebook. Ainda faltam a interpretação escrita, o fechamento das decisões de janela/features e a implementação do pipeline Bronze/Silver. Nenhum modelo foi treinado.
