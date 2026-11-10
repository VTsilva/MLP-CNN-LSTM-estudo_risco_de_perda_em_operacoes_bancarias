"""Validate consistency of the committed experiment result CSV files."""
from __future__ import annotations
import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "resultados_execucao"
EXPECTED_MODELS = {
    "univariado": {"mlp_1", "mlp_2", "cnn", "lstm", "stacked_lstm", "bilstm", "cnn_lstm", "convlstm"},
    "multivariado": {"mlp_1", "mlp_2", "mlp_multihead_1", "cnn", "cnn_multihead", "lstm", "stacked_lstm", "bilstm"},
}
EXPECTED_PARTITIONS = {"Treinamento": 1987, "Validacao": 582, "Teste": 292}
METRICS = ["MAE", "MSE", "RMSE", "R2", "Acuracia_direcional"]


def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def check(condition: bool, message: str):
    if not condition:
        raise SystemExit(message)


def main():
    consolidated = RESULTS / "comparacao_geral_metricas.csv"
    check(consolidated.exists(), f"Arquivo ausente: {consolidated}")
    rows = read_csv(consolidated)
    for experiment, expected_models in EXPECTED_MODELS.items():
        exp_rows = [r for r in rows if r.get("experimento") == experiment and r.get("modelo_id") != "persistencia"]
        actual_models = {r["modelo_id"] for r in exp_rows}
        check(actual_models == expected_models, f"{experiment}: modelos divergentes. {actual_models}")
        for model_id in expected_models:
            model_rows = [r for r in exp_rows if r["modelo_id"] == model_id]
            check({r["particao"] for r in model_rows} == set(EXPECTED_PARTITIONS), f"{experiment}/{model_id}: partições incompletas")
            check(len(model_rows) == 3, f"{experiment}/{model_id}: esperado uma linha por partição")
            for r in model_rows:
                for metric in METRICS:
                    value = float(r[metric])
                    check(math.isfinite(value), f"Métrica não finita: {experiment}/{model_id}/{r['particao']}/{metric}")
                check(float(r["MAE"]) >= 0 and float(r["RMSE"]) >= 0, "Erro negativo em MAE/RMSE")
        for partition, expected_n in EXPECTED_PARTITIONS.items():
            pred_path = RESULTS / f"avaliacao_{experiment}" / f"predicoes_{experiment}.csv"
            check(pred_path.exists(), f"Arquivo ausente: {pred_path}")
            pred_rows = read_csv(pred_path)
            part_rows = [r for r in pred_rows if r["particao"] == partition]
            check(len(part_rows) == expected_n * len(expected_models), f"{experiment}/{partition}: contagem de previsões inesperada ({len(part_rows)})")
            keys = [(r["modelo_id"], r["particao"], r["data"]) for r in part_rows]
            check(len(keys) == len(set(keys)), f"Chaves duplicadas em {pred_path}")
            for r in part_rows:
                check(math.isfinite(float(r["observado"])) and math.isfinite(float(r["previsto"])), f"Previsão não finita em {pred_path}")
    print("Resultados consistentes: 8 modelos por abordagem, 3 partições e previsões sem duplicatas.")


if __name__ == "__main__":
    main()
