# Skills para agentes e IAs

Uma **Skill** é um pacote de instruções reutilizáveis para orientar um agente/IA a executar uma atividade específica de forma consistente. Em geral, descreve quando usar o procedimento, entradas esperadas, etapas, padrões, saídas e critérios de qualidade.

Neste projeto, as Skills não serão usadas como um diário de conversas nem como substitutas de `contexto_ia/`. A separação é:

- `contexto_ia/`: o que é o projeto, o que sabemos e quais decisões estão vigentes.
- `planos_ia/`: o que será feito em uma tarefa específica.
- `skills/`: como executar repetidamente um tipo de tarefa.

## Política de criação

Criar uma Skill somente quando houver um procedimento recorrente suficientemente compreendido e validado. Não criar Skills operacionais baseadas em suposições ou processos que ainda não foram testados.

## Estrutura sugerida

```text
skills/
├── README.md
├── TEMPLATE_SKILL.md
└── nome-da-skill/
    └── SKILL.md
```

O formato poderá ser adaptado ao agente/ambiente que for utilizar as Skills. Não se deve presumir que todos os agentes reconheçam automaticamente um arquivo `SKILL.md` local.

Até 07/11/2026, nenhuma Skill operacional foi criada; apenas as diretrizes e o template estão disponíveis.
