import logging
from utils import State, buttons
from core.config import settings
from utils.filters import button
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery


logger = logging.getLogger(__name__)


@Client.on_callback_query(button("back_to_main"))
async def add_account(client: Client, query: CallbackQuery):
    await State.delete(query.from_user.id)
    return await query.message.edit_text(
        f"به منوی اصلی بازگشتیم 🔁",
        reply_markup=buttons.start
    )