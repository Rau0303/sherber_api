# src/database/session.py
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from src.database.database import async_engine
from typing import AsyncGenerator

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session