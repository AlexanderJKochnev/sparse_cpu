from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.model import load_model
from app.routers import embed, health


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_model()
    yield


app = FastAPI(title="sparse-embedder", lifespan=lifespan)
app.include_router(health.router)
app.include_router(embed.router)