from fastapi import FastAPI
from src.sheber_app import sheber_router

app = FastAPI(title='Sheber store app DEV', version='0.0.1')
app.include_router(sheber_router)