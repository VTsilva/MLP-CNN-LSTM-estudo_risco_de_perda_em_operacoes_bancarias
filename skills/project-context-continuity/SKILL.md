---
name: project-context-continuity
description: Read and maintain the project's compact, durable context so a new agent can continue work without relying on chat history.
---

# Project Context Continuity

## When to use
At the beginning of any substantial task, after major decisions, or before packaging a new project snapshot.

## Required reading
1. `AGENTS.md`
2. `contexto_ia/00_LEIA_PRIMEIRO.md`
3. `contexto_ia/estado_atual.md`
4. `contexto_ia/decisoes.md`
5. Relevant methodology, data dictionary, regulatory context and plans.

## Procedure
1. Inspect `git status --short --branch` and `git remote -v`; preserve all existing changes.
2. Read only context files relevant to the requested task; do not dump full chat history into documentation.
3. Distinguish confirmed facts, provisional assumptions, pending decisions and executed validations.
4. Before a complex task, write a plan in `planos_ia/` with objective, scope, inputs, steps, acceptance criteria and rollback/safety considerations.
5. After execution, update `estado_atual.md`, `decisoes.md` and methodology only where actual facts/decisions changed.
6. Record evidence for claims: file path, command/test, result and timestamp.
7. Keep identifiers and paths ASCII; academic prose may use Portuguese accents.
8. Never commit or push without explicit authorization.

## Output requirements
At task completion, state what changed, tests run, unresolved items and exact added/modified/removed paths. For ZIP-to-ZIP work, compute the diff from actual archive contents rather than relying on memory.
