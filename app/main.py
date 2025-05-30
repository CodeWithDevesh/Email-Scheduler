import app.config
from fastapi import FastAPI
from app.database import session

from loguru import logger


logger.debug("Starting FastAPI application")
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
