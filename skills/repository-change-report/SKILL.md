---
name: repository-change-report
description: Produce reproducible project ZIP snapshots and report exact file changes from one archive version to the next.
---

# Repository Change Report

## When to use
Whenever delivering a new ZIP or modifying repository structure, documentation, notebook, code, dependencies or CI.

## Procedure
1. Treat the user's latest uploaded ZIP as the source of truth.
2. Extract without dropping `.git` or unrelated local changes. Never push or commit unless explicitly requested.
3. Record baseline archive entries and hashes before editing.
4. Apply changes with ASCII-only internal paths and stable filenames.
5. Validate archive, notebook format, imports, execution and tests appropriate to scope.
6. Create the ZIP and reopen it; run `ZipFile.testzip()` and compare file entries.
7. Calculate added, modified, removed and renamed paths from baseline vs output.
8. Include the exact download link and a complete change list in the response.

## Required response format
- ZIP link and optional direct links to key files.
- concise summary of work completed.
- validations and limitations.
- `Adicionados`, `Modificados`, `Removidos` lists containing all exact paths.
- Git state: report whether `.git` was preserved and explicitly state whether commit/push occurred.

Do not infer file paths from names; use paths verified in the active filesystem/archive. Never claim a validation that was not executed.
