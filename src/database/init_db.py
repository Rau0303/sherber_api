# src/database/init_db.py
import asyncio
from src.database.base import Base
from src.database.session import async_engine
from src.database.models.user_model import User
from src.database.models.client_info import ClientInfo

async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)  # создаёт все таблицы

if __name__ == "__main__":
    asyncio.run(init_db())
