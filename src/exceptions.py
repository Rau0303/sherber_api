# src/global_exceptions.py
from fastapi import HTTPException, status

class AppException(HTTPException):
    """Базовый класс для всех пользовательских исключений в проекте"""
    def __init__(self, detail: str, status_code: int = status.HTTP_400_BAD_REQUEST):
        super().__init__(status_code=status_code, detail=detail)


class NotFoundException(AppException):
    """Ресурс не найден"""
    def __init__(self, resource: str = "Resource"):
        super().__init__(
            detail=f"{resource} не найден",
            status_code=status.HTTP_404_NOT_FOUND
        )


class AlreadyExistsException(AppException):
    """Ресурс уже существует"""
    def __init__(self, resource: str = "Resource"):
        super().__init__(
            detail=f"{resource} уже существует",
            status_code=status.HTTP_409_CONFLICT
        )


class UnauthorizedException(AppException):
    """Ошибка авторизации"""
    def __init__(self, detail: str = "Не авторизован"):
        super().__init__(detail=detail, status_code=status.HTTP_401_UNAUTHORIZED)


class ForbiddenException(AppException):
    """Доступ запрещен"""
    def __init__(self, detail: str = "Доступ запрещен"):
        super().__init__(detail=detail, status_code=status.HTTP_403_FORBIDDEN)


class InternalServerError(AppException):
    """Внутренняя ошибка сервера"""
    def __init__(self, detail: str = "Внутренняя ошибка сервера"):
        super().__init__(detail=detail, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)