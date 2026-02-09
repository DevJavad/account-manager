import logging
from utils import State, buttons
from utils.state import UserData
from core.config import settings
from utils.filters import button
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery


logger = logging.getLogger(__name__)


@Client.on_callback_query(button("back_to_main") & filters.user(settings.ADMIN))
async def add_account(client: Client, query: CallbackQuery):
    user_id = query.from_user.id
    await State.delete(user_id)
    await UserData.delete(user_id)
    return await query.message.edit_text(
        f"به منوی اصلی بازگشتیم 🔁",
        reply_markup=buttons.start
    )