"""Structural, syntax and static-report validation for the main academic notebook."""
from __future__ import annotations
import ast
from pathlib import Path
import nbformat

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "victor_silva_trabalho1.ipynb"
STATIC_REPORT = ROOT / "resultados_execucao" / "discussao_conclusao.md"
AUTO_REPORT = ROOT / "resultados_execucao" / "conclusao_automatica.md"
REQUIRED_UNIVARIATE = {"mlp_1", "mlp_2", "cnn", "lstm", "stacked_lstm", "bilstm", "cnn_lstm", "convlstm"}
REQUIRED_MULTIVARIATE = {"mlp_1", "mlp_2", "mlp_multihead_1", "cnn", "cnn_multihead", "lstm", "stacked_lstm", "bilstm"}


def main() -> None:
    notebook = nbformat.read(NOTEBOOK, as_version=4)
    nbformat.validate(notebook)
    cell_ids = [cell.get("id") for cell in notebook.cells]
    if any(not cell_id for cell_id in cell_ids) or len(cell_ids) != len(set(cell_ids)):
        raise SystemExit("Todas as células devem ter IDs não vazios e exclusivos.")

    designated = [i for i, c in enumerate(notebook.cells)
                  if c.cell_type == "code" and "central-imports" in c.get("metadata", {}).get("tags", [])]
    if len(designated) != 1:
        raise SystemExit(f"Esperada exatamente uma célula tagged central-imports; encontradas: {designated}")

    import_cells, sources = [], []
    for index, cell in enumerate(notebook.cells):
        if cell.cell_type != "code":
            continue
        try:
            tree = ast.parse(cell.source or "")
        except SyntaxError as exc:
            raise SystemExit(f"Erro de sintaxe na célula {index}: {exc}") from exc
        if any(isinstance(node, (ast.Import, ast.ImportFrom)) for node in ast.walk(tree)):
            import_cells.append(index)
        sources.append(cell.source or "")
    if import_cells != designated:
        raise SystemExit(f"Imports devem existir somente na célula central {designated}; encontrados: {import_cells}")

    source_text = "\n".join(sources)
    markdown_cells = [c.source for c in notebook.cells if c.cell_type == "markdown"]
    md_text = "\n".join(markdown_cells)
    missing_uni = sorted(m for m in REQUIRED_UNIVARIATE if f'"{m}"' not in source_text)
    missing_multi = sorted(m for m in REQUIRED_MULTIVARIATE if f'"{m}"' not in source_text)
    if missing_uni or missing_multi:
        raise SystemExit(f"Modelos ausentes. Univariados={missing_uni}; multivariados={missing_multi}")
    if "PENDENTE: implementar" in source_text or "TODO_IMPLEMENT_MODEL" in source_text:
        raise SystemExit("Foram encontrados placeholders de implementação de modelos.")
    if "gerar_conclusao_experimental" in source_text or "conclusao_automatica.md" in source_text:
        raise SystemExit("Conclusão deve ser Markdown estático, não gerada por código.")
    if AUTO_REPORT.exists():
        raise SystemExit("Arquivo de conclusão automática não deve existir; use Markdown estático.")
    if "## 10.4 Conclusão" not in md_text or "## 10.3 Discussão comparativa dos resultados" not in md_text:
        raise SystemExit("Discussão e conclusão acadêmicas estáticas devem estar no notebook.")
    if "[preencher]" in md_text.lower() or "[completar" in md_text.lower():
        raise SystemExit("Há referências ou campos acadêmicos não preenchidos no notebook.")
    if len(markdown_cells) < 2 or not notebook.cells[0].source.startswith("# Trabalho 1"):
        raise SystemExit("Célula inicial não contém o título esperado.")
    if not STATIC_REPORT.exists():
        raise SystemExit("Relatório Markdown estático ausente.")
    discussion = next(c.source for c in notebook.cells if c.cell_type == "markdown" and c.source.startswith("## 10.3 Discussão comparativa dos resultados"))
    conclusion = next(c.source for c in notebook.cells if c.cell_type == "markdown" and c.source.startswith("## 10.4 Conclusão"))
    expected_report = "\n\n".join([discussion, conclusion]).strip()
    actual_report = STATIC_REPORT.read_text(encoding="utf-8").strip()
    if actual_report != expected_report:
        raise SystemExit("O relatório Markdown deve corresponder à discussão e conclusão do notebook.")

    print(f"Notebook válido: {len(notebook.cells)} células; imports centralizados na célula {designated[0]}; 16 arquiteturas; discussão/conclusão estáticas sincronizadas.")


if __name__ == "__main__":
    main()
