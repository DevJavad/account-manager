import logging
from utils import buttons
from core.config import settings
from pyrogram.types import Message
from pyrogram import Client, filters


logger = logging.getLogger(__name__)


@Client.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
    chat_id = message.chat.id
    logger.info("New start: %s", chat_id)
    return await message.reply(
        f"سلام کاربر [ `{chat_id}` ] سیستم آماده است ✅:",
        reply_markup=buttons.start
    )