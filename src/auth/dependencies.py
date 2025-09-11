from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.session import get_async_session
from src.auth.service import AuthService


# 2. Инжектим сервис авторизации
def get_auth_service(session: AsyncSession = Depends(get_async_session)) -> AuthService:
    return AuthService(session)

