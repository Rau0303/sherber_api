from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas import ClientSchema
from src.auth.exceptions import EmailAlreadyExistsException, InvalidCredentialsException, InvalidSmsCodeException, PhoneAlreadyExistsException
from src.database.models.user_model import User
from src.exceptions import InternalServerError
from src.auth.utils import client_schema_to_model, register_schema_to_model, user_model_from_sms, verify_password
from src.auth.schemas import LoginWithPassword, LoginWithSms, RegisterSchema, SendSms

class AuthService:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def register_user(self, payload: RegisterSchema) -> int:
        try:
            # 1. Проверка телефона
            stmt = select(User).where(User.phone == payload.phone)
            result = await self.session.execute(stmt)
            if result.scalar_one_or_none():
                raise PhoneAlreadyExistsException()

            # 2. Проверка почты (если передана)
            if payload.email:
                stmt = select(User).where(User.email == payload.email)
                result = await self.session.execute(stmt)
                if result.scalar_one_or_none():
                    raise EmailAlreadyExistsException()

            # 3. Создаём нового пользователя
            user = register_schema_to_model(register=payload)
            self.session.add(user)

            try:
                await self.session.commit()  # только коммит оборачиваем в try/except для неожиданных ошибок
            except Exception as e:
                await self.session.rollback()
                raise InternalServerError(detail=str(e))

            return user.id

        except (PhoneAlreadyExistsException, EmailAlreadyExistsException):
            raise  
    
    async def register_client(self, payload: ClientSchema, user_id:int):
        client = client_schema_to_model(payload=payload, user_id=user_id)
        self.session.add(client)
        await self.session.commit()

    async def login_with_password(self, payload: LoginWithPassword)-> User:
        stmt = select(User).where(User.phone == payload.phone)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()

        if user is None:
            raise InvalidCredentialsException()

        if not verify_password(password=payload.password, hashed=user.hashed_password):
            raise InvalidCredentialsException()

        return user

    async def create_user_with_sms(self, payload: SendSms):
        '''
        так как у нас нет смс провайдера пока записываем статичный код
        '''

        user = user_model_from_sms(payload=payload)

        self.session.add(user)

        try:
            await self.session.commit()
        except Exception as e:
            await self.session.rollback()
            raise InternalServerError(detail=str(e))
        

    async def verify_sms_code(self, payload: LoginWithSms)-> User:
        stmt = select(User).where(User.phone == payload.phone)
        result = await self.session.execute(stmt)
        user = result.scalar_one_or_none()

        if user is None:
            raise InvalidCredentialsException()
        
        if not verify_password(password=payload.sms_code, hashed=user.sms_code):
            raise InvalidSmsCodeException()
        
        stmt = (
        update(User)
        .where(User.id == user.id)
        .values(is_active=True)
        )
        await self.session.execute(stmt)
        await self.session.commit()
        return user
        







