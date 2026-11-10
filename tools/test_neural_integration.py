"""One-epoch TensorFlow integration smoke test for all 16 notebook architectures.

This is deliberately separate from the light CI. It validates model construction,
input adapters, one training step and output shape without running academic training.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import nbformat
import tensorflow as tf

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "victor_silva_trabalho1.ipynb"


def find_source(notebook, marker: str) -> str:
    matches = [
        cell.source for cell in notebook.cells
        if cell.cell_type == "code" and marker in cell.source
    ]
    if len(matches) != 1:
        raise RuntimeError(f"Esperada uma célula contendo {marker!r}; encontradas {len(matches)}")
    return matches[0]


def main() -> None:
    notebook = nbformat.read(NOTEBOOK, as_version=4)
    namespace = {
        "np": np,
        "pd": __import__("pandas"),
        "tf": tf,
        "TENSORFLOW_DISPONIVEL": True,
        "TENSORFLOW_ERRO": None,
        "WINDOW_SIZE": 52,
        "FEATURES_MULTIVARIATE": ["Credit", "Risk", "Leverage", "Nonfinancial_Leverage"],
        "LEARNING_RATE": 0.001,
        "display": lambda *_args, **_kwargs: None,
    }
    source_tf = find_source(notebook, "def obter_tensorflow():")
    source_models = find_source(notebook, "def construir_modelo(")
    exec(compile(source_tf, "notebook_cell_obter_tensorflow", "exec"), namespace)
    exec(compile(source_models, "notebook_cell_model_builders", "exec"), namespace)

    models = {
        "univariado": ["mlp_1", "mlp_2", "cnn", "lstm", "stacked_lstm", "bilstm", "cnn_lstm", "convlstm"],
        "multivariado": ["mlp_1", "mlp_2", "mlp_multihead_1", "cnn", "cnn_multihead", "lstm", "stacked_lstm", "bilstm"],
    }
    features = {
        "univariado": ["Credit"],
        "multivariado": namespace["FEATURES_MULTIVARIATE"],
    }
    passed = 0
    for mode, model_ids in models.items():
        n_features = len(features[mode])
        x = np.random.default_rng(123).normal(size=(8, 52, n_features)).astype(np.float32)
        y = np.random.default_rng(456).normal(size=(8, 1)).astype(np.float32)
        for pos, model_id in enumerate(model_ids):
            tf.keras.backend.clear_session()
            tf.keras.utils.set_random_seed(1000 + pos)
            model = namespace["construir_modelo"](model_id, mode, n_features=n_features)
            model_input = namespace["converter_entrada_modelo"](model_id, x, mode, features[mode])
            model.fit(model_input, y, epochs=1, batch_size=4, shuffle=False, verbose=0)
            prediction = model.predict(model_input, verbose=0)
            if prediction.shape != (8, 1) or not np.isfinite(prediction).all():
                raise AssertionError(f"Saída inválida: {mode}/{model_id}, shape={prediction.shape}")
            passed += 1
            print(f"OK: {mode}/{model_id}")
    print(f"Smoke test neural concluído: {passed}/16 arquiteturas construídas, treinadas por 1 época e avaliadas.")


if __name__ == "__main__":
    main()
