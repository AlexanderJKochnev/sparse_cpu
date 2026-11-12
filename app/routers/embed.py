import logging

from fastapi import APIRouter, HTTPException

from app.schemas import EmbedRequest, EmbedResponse
from app.services.encoder import encode

logger = logging.getLogger(__name__)

router = APIRouter(tags=["embed"])


@router.post("/embed", response_model=EmbedResponse)
def embed(request: EmbedRequest) -> EmbedResponse:
    try:
        vectors = encode(request)
    except Exception as e:
        logger.exception("Ошибка инференса")
        raise HTTPException(status_code=500, detail=str(e))
    return EmbedResponse(embeddings=vectors)