# Plano — Revisão da EDA, narrativa, ambiente e CI

**Status:** concluído para documentação, EDA existente e estrutura de ambiente. Modelos neurais continuam pendentes.

## Objetivo
Transformar o notebook em relatório acadêmico encadeado, corrigir importações, justificar a janela e preparar reprodutibilidade/CI.

## Escopo executado
- Reorganizar o contexto IFRS 9/CMN 4.966 e explicitar limites do NFCI.
- Inserir explicações antes e interpretações/decisões após análises principais.
- Centralizar imports e tornar TensorFlow opcional para EDA.
- Documentar janela descritiva versus lookback e baseline 52 com sensibilidade 13/26/52/104.
- Adicionar associação defasada e benchmark de persistência.
- Otimizar dependências, `.gitignore` e CI para validação/execução do notebook.
- Criar/atualizar Skills e contexto.

## Validações executadas
- `nbformat.validate`: aprovado.
- `python tools/validate_notebook.py`: aprovado; imports apenas na célula tagueada `central-imports`.
- `jupyter nbconvert --to notebook --execute ... --allow_errors=False`: 41 células de código executadas, zero erros.
- 9 células com imagens PNG embutidas no notebook executado.
- Auditoria do CSV executada: 2.913 observações semanais, zero ausências/duplicatas e intervalos de sete dias.
- TensorFlow não estava instalado no ambiente desta sessão; nenhum treinamento neural foi realizado.
- Workflow GitHub Actions criado; não foi executado no GitHub nesta sessão.
- ZIP e diff de arquivos serão validados antes da entrega.

## Próximas tarefas
1. Conferir definição de acurácia nos materiais de IAD-012.
2. Comparar lookbacks pela validação e decidir feature set.
3. Implementar arquiteturas gradualmente conforme material da disciplina.
4. Treinar, selecionar épocas manualmente e comparar ao benchmark.
5. Executar notebook inteiro no CI e atualizar documentação dos resultados efetivos.
