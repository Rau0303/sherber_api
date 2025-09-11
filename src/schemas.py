from enum import Enum
from pydantic import BaseModel, Field


class PlatformEnum(str, Enum):
    ios = "ios"
    android = "android"
    web = "web"


class ClientSchema(BaseModel):
    platform: PlatformEnum = Field(
        ...,
        description="Платформа клиента",
        examples=["ios"]  # можно ios/android/web
    )
    os_version: str = Field(
        ...,
        description="Версия ОС",
        examples=["iOS 17.2", "Android 14"]
    )
    app_version: str = Field(
        ...,
        description="Версия приложения",
        examples=["1.0.5"]
    )
    app_build_version: str = Field(
        ...,
        description="Номер билда",
        examples=["102"]
    )
    locale: str = Field(
        ...,
        description="Язык/регион клиента",
        examples=["ru-RU", "en-US"]
    )
