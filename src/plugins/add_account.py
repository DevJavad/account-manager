import logging
from utils import State, buttons
from core.config import settings
from utils.filters import button
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery


logger = logging.getLogger(__name__)


@Client.on_callback_query(button("add_account") & filters.user(settings.ADMIN))
async def add_account(client: Client, query: CallbackQuery):
    await State.set(query.from_user.id, "get_number")
    await query.message.edit_text(
        "**افزودن اکانت تلگرام جدید** 📱\n\n"
        "لطفا شماره تلفن اکانت را با کد کشور وارد کنید:\n"
        "مثال:\n`+989932338788`",
        reply_markup=buttons.back_to_main
    )