# src/auth/constants.py

# Длина пароля
PASSWORD_MIN_LENGTH: int = 8
PASSWORD_MAX_LENGTH: int = 128

# Длина SMS-кода
SMS_CODE_LENGTH: int = 6
SMS_CODE_REGEX: str = r"^\d{6}$"

# Формат номера телефона
PHONE_REGEX: str = r"^7\d{10}$"
PHONE_LENGTH: int = 11

# TTL для SMS-кода (например, 5 минут)
SMS_CODE_TTL_SECONDS: int = 300

# Лимиты на количество попыток
MAX_LOGIN_ATTEMPTS: int = 5
BLOCK_TIME_SECONDS: int = 900  # блокировка на 15 минут

# Поддерживаемые локали
SUPPORTED_LOCALES: list[str] = ["ru-RU", "en-US"]
