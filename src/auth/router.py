# src.auth.router
from fastapi import APIRouter, Depends
from src.auth.service import AuthService
from src.exceptions import InternalServerError
from src.auth.schemas import AuthResponseSchema, LoginWithPassword, LoginWithSms, RegisterSchema
from src.auth.descriptions import *
from src.auth.dependencies import get_auth_service
router = APIRouter(prefix="/auth", tags=["Auth"])



@router.post(
    '/register',
    response_model=AuthResponseSchema,
    description=REGISTER_DESCRIPTION)
async def register_user(payload: RegisterSchema,auth_service: AuthService = Depends(get_auth_service)):
    try:
        pass
   
    except Exception as e:
        raise InternalServerError(str(e))



@router.post(
        "/login/sms", 
        response_model=AuthResponseSchema, 
        description=LOGIN_SMS_DESCRIPTION)
async def login_with_sms(payload: LoginWithSms, auth_service: AuthService = Depends(get_auth_service)):
    pass



@router.post(
        "/login/password", 
        response_model=AuthResponseSchema, 
        description=LOGIN_PASSWORD_DESCRIPTION)
async def login_with_password(payload: LoginWithPassword, auth_service: AuthService = Depends(get_auth_service)):
    pass