from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.config import DATABASE_URL
from loguru import logger

logger.debug("Creating the Sync Engine")
engine = create_engine(DATABASE_URL, echo=True)

logger.debug("Creating the Async Engine")
async_engine = create_async_engine(DATABASE_URL.replace("postgresql", "postgresql+asyncpg"), echo=True)

logger.debug("Creating the sync session")
session = sessionmaker(bind=engine, expire_on_commit=False, class_=Session)

logger.debug("Creating the async session")
async_session = async_sessionmaker(bind=async_engine, expire_on_commit=False, class_=AsyncSession)

logger.info("Database setup completed successfully")

def get_db_sync():
    logger.debug("Opening a new sync database session")
    try:
        with session() as db:
            yield db
    except Exception as e:
        logger.error(f"Error occurred in sync database session: {e}")
        raise
    finally:
        logger.debug("Sync database session closed")

async def get_db_async():
    logger.debug("Opening a new async database session")
    try:
        async with async_session() as db:
            yield db
    except Exception as e:
        logger.error(f"Error occurred in async database session: {e}")
        raise
    finally:
        logger.debug("Async database session closed")

Base = declarative_base()
logger.debug("Declarative base initialized")