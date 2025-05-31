from dotenv import load_dotenv
import os
from loguru import logger
import sys

load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVELL", "WARNING").upper()
logger.info(f"Setting log level to {LOG_LEVEL}")
if LOG_LEVEL not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
    logger.error(
        f"Invalid LOG_LEVEL: {LOG_LEVEL}. Must be one of DEBUG, INFO, WARNING, ERROR, CRITICAL."
    )
    raise ValueError(
        f"Invalid LOG_LEVEL: {LOG_LEVEL}. Must be one of DEBUG, INFO, WARNING, ERROR, CRITICAL."
    )

logger.remove()
logger.add(
    sys.stdout,
    level=LOG_LEVEL,
    format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    filter=None,
    colorize=None,
    serialize=False,
    backtrace=True,
    diagnose=True,
    enqueue=False,
    context=None,
    catch=True,
)
logger.debug("Logger configured successfully")


logger.debug("Loading configuration from environment variables")

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    logger.info(f"Database URL loaded successfully")
else:
    logger.warning("Database URL is not set. Using default value.")
    DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/EmailScheduler"

logger.debug("Configuration loaded successfully")
