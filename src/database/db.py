from tortoise import Tortoise
import logging


logger = logging.getLogger(__name__)


async def connect(db_url: str) -> None:
    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["database.models"]}
    )
    await Tortoise.generate_schemas()

    logger.info("connect to the database: %s", db_url)


async def disconnect():
    await Tortoise.close_connections()

    logger.info("disconnected the database")