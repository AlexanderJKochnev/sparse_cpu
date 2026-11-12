from app.model import get_model
from app.schemas import EmbedRequest


def encode(request: EmbedRequest) -> list[dict[str, float]]:
    model = get_model()

    if request.type == "query":
        embeddings = model.encode_query(request.texts, convert_to_tensor=False)
    else:
        embeddings = model.encode_document(request.texts, convert_to_tensor=False)

    result: list[dict[str, float]] = []
    for emb in embeddings:
        if isinstance(emb, dict):
            result.append({k: float(v) for k, v in emb.items()})
        else:
            decoded = model.decode([emb])[0]
            result.append({token: float(score) for token, score in decoded})
    return result