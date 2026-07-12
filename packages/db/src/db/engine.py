from config import settings
from sqlalchemy import text
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine


def build_database_url() -> str:
    database_settings = settings.database

    return str(
        URL.create(
            "postgresql+asyncpg",
            username=database_settings.user,
            password=database_settings.password,
            host=database_settings.host,
            port=database_settings.port,
            database=database_settings.database,
        )
    )


async def ping_database(engine: AsyncEngine) -> None:
    async with engine.connect() as connection:
        await connection.execute(text("SELECT 1"))


engine: AsyncEngine = create_async_engine(
    build_database_url(),
    echo=False,
    pool_pre_ping=True,
)
