from fastapi import FastAPI
from .api.routes import router as recommendation_router
from .core.config import settings

app = FastAPI(title=settings.app_name)

app.include_router(recommendation_router, prefix="/suggestions")
