import dotenv
import os
from loguru import logger
import sys

dotenv.load_dotenv()

logger.remove()
LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()
if LOG_LEVEL not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
    raise ValueError(
        f"Invalid LOG_LEVEL: {LOG_LEVEL}. Must be one of DEBUG, INFO, WARNING, ERROR, CRITICAL."
    )
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


logger.debug("Loading configuration from environment variables")

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/EmailScheduler"
)
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
REDIS_CACHE_TTL = int(os.getenv("REDIS_CACHE_TTL", 60 * 60 * 24))  # Default to 24 hours
REDIS_CACHE_KEY_PREFIX = os.getenv("REDIS_CACHE_KEY_PREFIX", "app_cache")
REDIS_CACHE_ENABLED = os.getenv("REDIS_CACHE_ENABLED", "true").lower() in (
    "true",
    "1",
    "t",
)
logger.debug("Configuration loaded successfully")
