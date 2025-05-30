from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from app.config import DATABASE_URL
from loguru import logger

logger.trace("Creating the Sync Engine")
engine = create_engine(DATABASE_URL, echo=True)

logger.trace("Creating the Async Engine")
async_engine = create_async_engine(DATABASE_URL.replace("postgresql", "postgresql+asyncpg"), echo=True)

logger.trace("Creating the sync session")
session = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)

logger.trace("Creating the async session")
async_session = sessionmaker(bind=async_engine, expire_on_commit=False, class_=AsyncSession)

def get_db_sync():
    try:
        db = session()
        yield db
    except Exception as e:
        logger.error(f"Sync Database session error: {e}")
        raise
    finally:
        db.close()

async def get_db_async():
    try:
        db = async_session()
        yield db
    except Exception as e:
        logger.error(f"Async Database session error: {e}")
        raise
    finally:
        await db.close()