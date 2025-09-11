from pydantic import BaseModel, Field, EmailStr
from src.schemas import ClientSchema
from src.auth.constants import *

class LoginWithSms(BaseModel):
    phone: str = Field(
        ...,
        description="Номер телефона в формате 7XXXXXXXXXX (11 цифр, без +)",
        pattern=PHONE_REGEX,
        min_length=PHONE_LENGTH,
        max_length=PHONE_LENGTH,
        examples=["77011234567"]
    )
    sms_code: str = Field(
        ...,
        min_length=SMS_CODE_LENGTH,
        max_length=SMS_CODE_LENGTH,
        description="Код из SMS (строго 6 цифр)",
        pattern=SMS_CODE_REGEX,
        examples=["123456"]
    )
    client: ClientSchema
    


class LoginWithPassword(BaseModel):
    phone: str = Field(
        ...,
        description="Номер телефона в формате 7XXXXXXXXXX (11 цифр, без +)",
        pattern=PHONE_REGEX,
        min_length=PHONE_LENGTH,
        max_length=PHONE_LENGTH,
        examples=["77011234567"]
    )
    password: str = Field(
        ...,
        min_length=PASSWORD_MIN_LENGTH,
        max_length=PASSWORD_MAX_LENGTH,
        description="Пароль пользователя (от 8 символов, любые символы)",
        examples=["qwerty123", "My$ecureP@ssw0rd"]
    )
    client: ClientSchema



class RegisterSchema(BaseModel):
    phone: str = Field(
        ...,
        description="Номер телефона в формате 7XXXXXXXXXX (11 цифр, без +)",
        pattern=PHONE_REGEX,
        min_length=PHONE_LENGTH,
        max_length=PHONE_LENGTH,
        examples=["77011234567"]
    )
    password: str = Field(
        ...,
        min_length=PASSWORD_MIN_LENGTH,
        max_length=PASSWORD_MAX_LENGTH,
        description="Пароль пользователя (от 8 символов, любые символы)",
        examples=["qwerty123", "My$ecureP@ssw0rd"]
    )
    email: EmailStr | None = Field(
        None,
        description="Электронная почта (опционально при регистрации, обязательно для сброса пароля)",
        examples=["user@example.com"]
    )
    client: ClientSchema




# RESPONSE


class UserInfoSchema(BaseModel):
    id: int = Field(..., description="ID пользователя", example=123)
    phone: str = Field(..., description="Номер телефона пользователя", example="77011234567")
    email: EmailStr | None = Field(None, description="Электронная почта пользователя", example="user@example.com")

class AuthDataSchema(BaseModel):
    user: UserInfoSchema
    access_token: str = Field(..., description="JWT токен для авторизации", example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...")
    token_type: str = Field(..., description="Тип токена, обычно 'bearer'", example="bearer")

class AuthResponseSchema(BaseModel):
    status: str = Field("success", description="Статус запроса", example="success")
    data: AuthDataSchema