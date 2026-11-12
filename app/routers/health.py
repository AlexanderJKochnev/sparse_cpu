from fastapi import APIRouter

from app.model import get_model
from app.schemas import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    get_model()  # бросит RuntimeError, если модель не загружена
    return HealthResponse(status="ok")