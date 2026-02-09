import logging
from utils import buttons
from core.config import settings
from utils.filters import button
from database.models import Account
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery


logger = logging.getLogger(__name__)


@Client.on_callback_query(button("accounts_list") & filters.user(settings.ADMIN))
async def accounts_list(client: Client, query: CallbackQuery):
    accounts = await Account.all()

    if not accounts:
        return await query.message.edit_text(
            "هیچ اکانتی ثبت نشده ❌", reply_markup=buttons.back_to_main
        )

    return await query.message.edit(
        "📱 لیست اکانت‌ها:", reply_markup=buttons.accounts_list(accounts)
    )