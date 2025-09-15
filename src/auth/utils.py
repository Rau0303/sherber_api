# src/auth/utils.py
from src.database.models.client_info import ClientInfo
from src.schemas import ClientSchema
from src.auth.schemas import RegisterSchema, SendSms
from src.database.models.user_model import User
from passlib.context import CryptContext
from datetime import datetime, timezone

# Используем argon2 вместо bcrypt
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(password: str) -> str:
    """Хешируем пароль"""
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    """Проверяем пароль"""
    return pwd_context.verify(password, hashed)


def register_schema_to_model(payload: RegisterSchema) -> User:
    """Преобразуем RegisterSchema в User"""
    return User(
        phone=payload.phone,
        email=payload.email,
        hashed_password=hash_password(payload.password),
    )

from datetime import datetime, timezone

def user_model_from_sms(payload: SendSms) -> User:
    """Создаёт объект User с полями для SMS-кода"""
    now = datetime.now(timezone.utc).replace(tzinfo=None)  # убираем tzinfo
    return User(
        phone=payload.phone,
        sms_code=hash_password(password='2002'),
        sms_code_created_at=now,
        is_active=False
    )





def client_schema_to_model(payload: ClientSchema, user_id: int) -> ClientInfo:
    """Преобразуем ClientSchema в ClientInfo"""
    return ClientInfo(
        user_id=user_id,
        platform=payload.platform,
        os_version=payload.os_version,
        app_version=payload.app_version,
        app_build_version=payload.app_build_version,
        locale="ru-RU"
    )
