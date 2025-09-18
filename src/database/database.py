# src/database/database.py
# created by Rauan Aitanatov
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from src.database.settings import settings


sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False
)

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo = True
)

