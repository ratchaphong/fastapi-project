from typing import Union
from contextlib import asynccontextmanager

from fastapi import FastAPI
from config import settings
from database import init_db, close_db
from routers import routers

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize database on startup and close it on shutdown"""
    try:
        await init_db()
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise e
    yield
    try:
        await close_db()
    except Exception as e:
        print(f"Error closing database: {e}")
        raise e

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan,
)

# Include routers
for router in routers:
    app.include_router(router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/env")
async def get_env():
    return {
        "app_name": settings.app_name,
        "app_version": settings.app_version,
        "debug": settings.debug,
        "database_url": settings.database_url if settings.database_url else "Not set",
        "api_key": "***" if settings.api_key else "Not set",  
        "max_items": settings.max_items,
        "environment": settings.environment
    }