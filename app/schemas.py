from typing import Literal

from pydantic import BaseModel, Field


class EmbedRequest(BaseModel):
    texts: list[str] = Field(..., min_length=1)
    type: Literal["query", "document"] = "document"


class EmbedResponse(BaseModel):
    embeddings: list[dict[str, float]]


class HealthResponse(BaseModel):
    status: str