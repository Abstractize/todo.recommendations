from fastapi import FastAPI
from .api.routes import router as recommendation_router
from .core.config import settings

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    from .db import run_migrations

    run_migrations()
    yield


app = FastAPI(title=settings.app_name, lifespan=lifespan)

app.include_router(recommendation_router, prefix="/suggestions")
