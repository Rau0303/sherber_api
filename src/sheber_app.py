from fastapi import APIRouter
from src.auth.router import router as auth_router

sheber_router = APIRouter()


sheber_router.include_router(auth_router)