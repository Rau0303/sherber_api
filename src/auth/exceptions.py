from fastapi import HTTPException, status


class AuthException(HTTPException):
    """Базовый класс для исключений аутентификации/регистрации"""
    def __init__(self, detail: str, status_code: int = status.HTTP_400_BAD_REQUEST):
        super().__init__(status_code=status_code, detail=detail)


class InvalidPhoneFormatException(AuthException):
    """Некорректный формат номера"""
    def __init__(self):
        super().__init__(
            detail="Номер телефона должен быть в формате 7XXXXXXXXXX (11 цифр, без +).",
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )


class InvalidSmsCodeException(AuthException):
    """Неверный или просроченный SMS-код"""
    def __init__(self):
        super().__init__(
            detail="Введён неверный или просроченный SMS-код.",
            status_code=status.HTTP_401_UNAUTHORIZED
        )


class InvalidCredentialsException(AuthException):
    """Неверный телефон или пароль"""
    def __init__(self):
        super().__init__(
            detail="Неверный номер телефона или пароль.",
            status_code=status.HTTP_401_UNAUTHORIZED
        )


class EmailAlreadyExistsException(AuthException):
    """Почта уже используется"""
    def __init__(self):
        super().__init__(
            detail="Эта электронная почта уже зарегистрирована.",
            status_code=status.HTTP_409_CONFLICT
        )


class PhoneAlreadyExistsException(AuthException):
    """Телефон уже используется"""
    def __init__(self):
        super().__init__(
            detail="Этот номер телефона уже зарегистрирован.",
            status_code=status.HTTP_409_CONFLICT
        )
