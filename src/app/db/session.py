from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from ..core.config import settings

engine = create_async_engine(settings.sql_connection_string, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_db():
    async with async_session() as session:
        yield session
