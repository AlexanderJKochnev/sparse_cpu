import logging

import torch
from sentence_transformers import SparseEncoder

from app.config import settings

logger = logging.getLogger(__name__)

_model: SparseEncoder | None = None


def load_model() -> None:
    global _model
    torch.set_num_threads(settings.cpu_threads)

    logger.info("Загружаю SparseEncoder из %s (threads=%d)",
                settings.model_dir, settings.cpu_threads)
    _model = SparseEncoder(
        settings.model_dir,
        device="cpu",
        local_files_only=True,
    )
    _model.eval()
    logger.info("Модель загружена")


def get_model() -> SparseEncoder:
    if _model is None:
        raise RuntimeError("Модель не загружена (load_model не вызван)")
    return _model