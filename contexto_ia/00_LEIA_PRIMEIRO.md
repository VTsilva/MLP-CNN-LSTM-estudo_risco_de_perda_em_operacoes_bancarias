# Instruções de leitura do contexto do projeto

Este diretório é a memória documental consolidada do projeto. Seu objetivo é permitir que uma IA, agente ou colaborador compreenda o trabalho sem precisar reler conversas extensas.

## Ordem de leitura

1. `visao_geral.md` — objetivo, pergunta e escopo.
2. `estado_atual.md` — o que existe, o que foi verificado e o que falta.
3. `decisoes.md` — decisões confirmadas, provisórias e pendentes.
4. `metodologia_provisoria.md` — exigências do professor e desenho experimental em discussão.
5. `dicionario_dados.md` — colunas do CSV e interpretação de negócio.
6. `referencias.md` — fontes oficiais e materiais usados.

O notebook original do professor está em `arquivos_de_contexto/`. Ele prevalece como fonte das instruções acadêmicas da disciplina. Em caso de divergência entre uma interpretação resumida neste diretório e o roteiro do professor, conferir o notebook original e registrar a resolução em `decisoes.md`.

## Regras para agentes e IAs

- Não inventar análises, resultados, métricas, referências ou decisões ainda não realizadas.
- Diferenciar fatos verificados, hipóteses e decisões provisórias.
- Não tratar previsão do `Credit` como previsão direta de LGD. A conexão com LGD é a motivação financeira do estudo, não o alvo estatístico atual.
- Preservar o arquivo de `data/raw/` como fonte original, sem sobrescrevê-lo.
- Não alterar o notebook original do professor. Fazer uma cópia para o desenvolvimento.
- Não ajustar transformadores (por exemplo, scaler) com dados de validação ou teste.
- Preservar a ordem temporal nas divisões de treino, validação e teste.
- Atualizar `estado_atual.md` e `decisoes.md` quando houver progresso ou decisão relevante.
- Criar um plano em `planos_ia/` para tarefas complexas antes da execução, quando isso fizer parte do direcionamento do projeto.
- Criar uma Skill apenas quando um procedimento reutilizável estiver suficientemente definido; não criar instruções fictícias para etapas ainda não testadas.

## Convenção de status

- **Confirmado:** explícito no enunciado, verificado diretamente nos arquivos ou decidido pelo responsável pelo projeto.
- **Provisório:** proposta de trabalho ainda sujeita a validação.
- **Pendente:** precisa de decisão, evidência ou execução.
