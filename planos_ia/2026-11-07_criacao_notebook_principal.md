# Plano — Criação do notebook principal

- **Data:** 07/11/2026
- **Status:** Concluído
- **Entrada:** ZIP `Trabalho_1_Redes_recorrentes_V1.zip`
- **Objetivo:** criar o notebook principal do estudo na raiz do repositório, preservando o roteiro original do professor.

## Escopo executado

1. Inspecionar o projeto, instruções de agentes, contexto metodológico, dataset e notebook original.
2. Criar `victor_silva_trabalho1.ipynb` com formato de relatório acadêmico profissional.
3. Implementar células de imports/configuração, localização do CSV, ingestão, tipagem, auditoria e estatísticas.
4. Implementar visualizações da série, rolling mean/volatility, distribuições, correlações, ACF/PACF, periodograma e testes ADF/KPSS.
5. Implementar a divisão cronológica 70/20/10, funções genéricas de janela e escalonamento sem vazamento, e funções genéricas para treinamento/avaliação.
6. Estruturar as seções dos 8 modelos univariados e 8 multivariados, mantendo os detalhes de arquitetura pendentes quando dependentes do material de aula.
7. Atualizar README, AGENTS, contexto, metodologia e manifest para apontar o notebook principal e o estado real.

## Arquivos criados/alterados

### Criado
- `victor_silva_trabalho1.ipynb`
- `planos_ia/2026-11-07_criacao_notebook_principal.md`

### Alterados
- `README.md`
- `AGENTS.md`
- `contexto_ia/00_LEIA_PRIMEIRO.md`
- `contexto_ia/estado_atual.md`
- `contexto_ia/metodologia_provisoria.md`
- `contexto_ia/decisoes.md`
- `planos_ia/README.md`
- `PACKAGE_MANIFEST.json`

## Validações

- Notebook validado com `nbformat`.
- Todas as 72 células do notebook foram executadas sequencialmente com `nbclient`, sem erros após correção da visualização de distribuições.
- Ingestão e auditoria confirmaram 2.913 observações, 6 variáveis numéricas, ausência de nulos e duplicatas e frequência semanal regular.
- Partições temporais verificadas: 2.039 treino, 582 validação e 292 teste.
- Não foi iniciado treinamento de redes neurais. TensorFlow não está instalado no ambiente de geração; as funções importam TensorFlow de forma tardia e informam dependência ausente se chamadas.
- O notebook original do professor e o CSV raw permaneceram inalterados.
- Nenhum commit ou push foi realizado.

## Limitações e pendências preservadas

- Interpretação escrita dos achados da EDA.
- Definição fundamentada de `WINDOW_SIZE`.
- Confirmação da definição de “acurácia” utilizada em IAD-012.
- Seleção final das features multivariadas.
- Detalhes de MLP/CNN multi-cabeça, CNN-LSTM e ConvLSTM conforme os exemplos da disciplina.
- Implementar, treinar, inspecionar épocas, retreinar e avaliar os 16 experimentos.

## Resultado

Notebook principal criado e executado como scaffold de desenvolvimento. Não contém resultados preditivos fictícios nem conclusões não verificadas.
