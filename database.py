from tortoise import Tortoise # pyright: ignore[reportMissingImports]
from config import settings

async def init_db():
    """Initialize database connection"""
    await Tortoise.init(
        db_url=settings.database_url,
        modules={'models': ['models.user', 'models.product']}
    )
    await Tortoise.generate_schemas(safe=True)

async def close_db():
    """Close database connection"""
    await Tortoise.close_connections()