import app.config
from fastapi import FastAPI, Depends
from app.database import get_db_async
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from loguru import logger


logger.debug("Starting FastAPI application")
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/health")
async def health_check(db: AsyncSession = Depends(get_db_async)):
    try:
        async with db.begin():
            await db.execute(text("SELECT 1"))
        return {"status": "healthy"}
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return {"status": "unhealthy", "error": str(e)}