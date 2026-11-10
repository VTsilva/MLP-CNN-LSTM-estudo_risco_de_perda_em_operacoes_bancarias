"""Capture runtime provenance and attach it to existing result configuration files.

Run from the repository root after executing the notebook:
    python tools/capture_execution_provenance.py
"""
from __future__ import annotations
import hashlib
import importlib.metadata as metadata
import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "victor_silva_trabalho1.ipynb"
DATA = ROOT / "data" / "raw" / "nfci-data-series-csv.csv"
RESULTS = ROOT / "resultados_execucao"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def package_version(name: str):
    try:
        return metadata.version(name)
    except metadata.PackageNotFoundError:
        return None


def notebook_source_hash(path: Path) -> str:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    payload = "\n".join(
        cell.get("cell_type", "") + "\n" + "".join(cell.get("source", []))
        for cell in notebook.get("cells", [])
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def main() -> None:
    if not NOTEBOOK.exists() or not DATA.exists():
        raise SystemExit("Execute o script na raiz de um repositório completo do projeto.")
    try:
        import tensorflow as tf
        tensorflow_version = tf.__version__
        keras_version = getattr(tf.keras, "__version__", None) or package_version("keras")
        devices = [{"name": d.name, "type": d.device_type} for d in tf.config.list_physical_devices()]
        tensorflow_available = True
    except Exception as exc:
        tensorflow_version = None
        keras_version = package_version("keras")
        devices = []
        tensorflow_available = False
        tensorflow_error = repr(exc)
    else:
        tensorflow_error = None

    manifest = {
        "captured_at_utc": datetime.now(timezone.utc).isoformat(),
        "python_version": sys.version,
        "python_implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "packages": {
            name: package_version(name)
            for name in ["numpy", "pandas", "scipy", "scikit-learn", "matplotlib", "seaborn", "statsmodels", "tensorflow", "keras", "jupyterlab", "ipykernel"]
        },
        "tensorflow_available": tensorflow_available,
        "tensorflow_version": tensorflow_version,
        "keras_version": keras_version,
        "devices": devices,
        "tensorflow_import_error": tensorflow_error,
        "data_file": str(DATA.relative_to(ROOT)),
        "data_sha256": sha256(DATA),
        "notebook_file": str(NOTEBOOK.relative_to(ROOT)),
        "notebook_sha256": sha256(NOTEBOOK),
        "notebook_source_sha256": notebook_source_hash(NOTEBOOK),
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    manifest_path = RESULTS / "proveniencia_execucao.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for config_path in RESULTS.glob("**/configuracao*.json"):
        config = json.loads(config_path.read_text(encoding="utf-8"))
        config["proveniencia_execucao"] = {
            "manifesto": str(manifest_path.relative_to(ROOT)),
            "python_version": sys.version,
            "tensorflow_version": tensorflow_version,
            "keras_version": keras_version,
            "devices": devices,
            "data_sha256": manifest["data_sha256"],
            "notebook_source_sha256": manifest["notebook_source_sha256"],
        }
        config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Proveniência registrada em {manifest_path.relative_to(ROOT)}")
    print(f"Python: {platform.python_version()} | TensorFlow: {tensorflow_version} | devices: {devices}")


if __name__ == "__main__":
    main()
