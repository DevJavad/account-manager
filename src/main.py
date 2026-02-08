import logging
from pyrogram import Client
from core.config import settings
from database import connect, disconnect


logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


client = Client(
    "main",
    settings.API_ID,
    settings.API_HASH,
    bot_token=settings.TOKEN,
    workdir="sessions",
    plugins=dict(root="plugins")
)


@client.on_start()
async def start(client):
    logger.info("Start bot...")
    await connect(settings.DB_URL)


@client.on_stop()
async def stopo(client):
    logger.info("Stop bot....")
    await disconnect()


if __name__ == "__main__":
    client.run()