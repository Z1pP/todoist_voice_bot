import logging

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from infrastructure.config.settings import settings

logger = logging.getLogger(__name__)

async_engine = create_async_engine(settings.DATABSE_URL, future=True)
session_maker = async_sessionmaker(async_engine, expire_on_commit=False)
