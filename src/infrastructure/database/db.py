from .models import Base
from .session import async_engine


async def initialize_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
