import logging
from utils.filters import state
from utils import State, buttons
from utils.state import UserData
from core.config import settings
from pyrogram.types import Message
from database.models import Account
from pyrogram import Client, filters


logger = logging.getLogger(__name__)


@Client.on_message(state("get_number") & filters.private)
async def start(client: Client, message: Message):
    chat_id = message.chat.id
    text = message.text

    if not text.startswith("+"):
        return await message.reply(
            "لطفاً شماره تلفن اکانت را با کد کشور وارد کنید:\n"
            "مثال: \n`+989123456789`",
            reply_markup=buttons.back_to_main
        )

    phone = text.replace("+", "").strip()
    existing = await Account.get_or_none(phone=phone)
    if existing:
        return await message.reply(
            "❌ این شماره تلفن قبلاً در سیستم ثبت شده است",
            reply_markup=buttons.back_to_main
        )

    try:
        tmp_client = Client(
            f"acc_{phone}",
            settings.API_ID,
            settings.API_HASH,
            phone_number=text,
            in_memory=True
        )
        await tmp_client.connect()
        sent_code = await tmp_client.send_code(phone)

        await UserData.set(chat_id, "phone_code_hash", sent_code.phone_code_hash)
        await State.set(chat_id, "get_code")

        return await message.reply(
            "✅ کد تأیید به اکانت تلگرام شما ارسال شد.\n"
            "کد را وارد کنید:",
            reply_markup=buttons.code_keyboard()
        )

    except Exception as error:
        logger.error("Send code error to %s: %s", phone, error)
        return await message.reply(
            f"❌ خطایی رخ داد: {str(error)}",
            reply_markup=buttons.back_to_main
        )