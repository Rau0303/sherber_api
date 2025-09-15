# src.auth.router
from fastapi import APIRouter, Depends
from src.auth.exceptions import EmailAlreadyExistsException, InvalidCredentialsException, PhoneAlreadyExistsException
from src.auth.service import AuthService
from src.exceptions import InternalServerError
from src.auth.schemas import AuthDataSchema, AuthResponseSchema, LoginWithPassword, LoginWithSms, RegisterSchema, SendSms, SendSmsResponseSchema, UserInfoSchema
from src.auth.descriptions import *
from src.auth.dependencies import get_auth_service
from src.utils.jwt import create_access_token
router = APIRouter(prefix="/auth", tags=["Auth"])



@router.post(
    '/register',
    response_model=AuthResponseSchema,
    description=REGISTER_DESCRIPTION
)
async def register_user(
    payload: RegisterSchema, 
    auth_service: AuthService = Depends(get_auth_service)):
    try:
        # 1. Создаём пользователя и получаем user_id
        user_id = await auth_service.register_user(payload=payload)

        # 2. Создаём ClientInfo
        await auth_service.register_client(user_id=user_id, client=payload.client)

        # 3. Генерируем JWT токен
        access_token = create_access_token(subject=user_id)


        # 5. Возвращаем готовый ответ
        return AuthResponseSchema(
            status="success", 
            data=AuthDataSchema(
            user = UserInfoSchema(
                id = user_id,
                phone=payload.phone,
                email=payload.email),
            access_token=access_token,
            token_type='bearer')
            )

    except (PhoneAlreadyExistsException, EmailAlreadyExistsException) as e:
        # Пробрасываем бизнес-ошибки (409 Conflict)
        raise e
    except Exception as e:
        # Любые другие ошибки → InternalServerError
        raise InternalServerError(detail=str(e))



@router.post(
        "/login/sms/verify", 
        response_model=AuthResponseSchema, 
        description=LOGIN_SMS_DESCRIPTION)
async def login_with_sms(payload: LoginWithSms, auth_service: AuthService = Depends(get_auth_service)):
    try:
        user = await auth_service.verify_sms_code(payload=payload)

        await auth_service.register_client(payload=payload.client, user_id=user.id)

        access_token = create_access_token(subject=user.id)


        # 5. Возвращаем готовый ответ
        return AuthResponseSchema(
            status="success", 
            data=AuthDataSchema(
            user = UserInfoSchema(
                id = user.id,
                phone=payload.phone,
                email = user.email),
            access_token=access_token,
            token_type='bearer')
            )
    except Exception as e:
        raise InternalServerError(detail=str(e))



@router.post(
        '/login/send/sms',
        response_model=SendSmsResponseSchema  
)
async def send_sms(payload: SendSms, auth_service: AuthService = Depends(get_auth_service)):
    try:
        await auth_service.create_user_with_sms(payload=payload)

        return SendSmsResponseSchema(
            status='success',
            message='SMS-код успешно отправлен'
        )
    except Exception as e:
        raise InternalServerError(detail= str(e))
    


@router.post(
        "/login/password", 
        response_model=AuthResponseSchema, 
        description=LOGIN_PASSWORD_DESCRIPTION)
async def login_with_password(payload: LoginWithPassword, auth_service: AuthService = Depends(get_auth_service)):
    try:
        user = await auth_service.login_with_password(payload=payload)

        await auth_service.register_client(client=payload.client, user_id=user.id)
        access_token = create_access_token(subject=user.id)

        return AuthResponseSchema(
            status="success", 
            data=AuthDataSchema(
            user = UserInfoSchema(
                id = user.id,
                phone=payload.phone,
                email=user.email ),
            access_token=access_token,
            token_type='bearer')
            )
    except InvalidCredentialsException:
        # Возвращаем ошибку при неверных данных
        raise InvalidCredentialsException()
    except Exception as e:
        # Все остальные ошибки → InternalServerError
        raise InternalServerError(detail=str(e))
