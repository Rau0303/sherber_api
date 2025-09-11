from sqlalchemy import String, Boolean, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from typing import Optional
from src.database.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    phone: Mapped[str] = mapped_column(String(11), unique=True, nullable=False, index=True)
    email: Mapped[Optional[str]] = mapped_column(String(255), unique=True, nullable=True, index=True)
    hashed_password: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)

    sms_code: Mapped[Optional[str]] = mapped_column(String(6), nullable=True)
    sms_code_created_at: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)

    platform: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    app_version: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    app_build_version: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    locale: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_blocked: Mapped[bool] = mapped_column(Boolean, default=False)
    login_attempts: Mapped[int] = mapped_column(Integer, default=0)
    last_login: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)

    firebase_token: Mapped[Optional[str]] = mapped_column(String(512), nullable=True, comment="Токен для Firebase push-уведомлений")

    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())