# tests/conftest.py
import sys
from pathlib import Path
import pytest_asyncio
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport


# --- Путь к проекту ---
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from src.main import app

# --- AsyncClient для тестов ---
@pytest_asyncio.fixture
async def async_client():
    """
    Асинхронный клиент для тестирования FastAPI.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as client:
        yield client
