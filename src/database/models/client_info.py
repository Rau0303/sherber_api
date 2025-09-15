from sqlalchemy import String, Boolean, Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
from src.database.base import Base


class ClientInfo(Base):
    __tablename__ = "client_info"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    platform: Mapped[str] = mapped_column(String(20), nullable=False)
    os_version: Mapped[str] = mapped_column(String(50), nullable=False)
    app_version: Mapped[str] = mapped_column(String(20), nullable=False)
    app_build_version: Mapped[str] = mapped_column(String(20), nullable=False)
    locale: Mapped[str] = mapped_column(String(10), nullable=False)
