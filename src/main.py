from fastapi import FastAPI
from src.database.init_db import init_db 
from src.sheber_app import sheber_router

app = FastAPI(title='Sheber store app DEV', version='0.0.1')
app.include_router(sheber_router)


@app.on_event("startup")
async def startup():
    await init_db()