import logging
from utils.filters import state
from utils import State, buttons
from utils.state import UserData
from core.config import settings
from pyrogram.types import Message
from database.models import Account
from pyrogram import Client, filters
from pyrogram.errors import (
    PhoneNumberBanned,
    PhoneNumberInvalid,
    PhoneNumberFlood
)


logger = logging.getLogger(__name__)


@Client.on_message(state("get_number") & filters.user(settings.ADMIN))
async def start(client: Client, message: Message):
    chat_id, text = message.chat.id, message.text.strip()

    if not text.startswith("+"):
        return await message.reply(
            "❌ شماره تلفن نامعتبر است!\n"
            "لطفاً شماره را با فرمت صحیح وارد کنید:\n"
            "مثال: `+989123456789`",
            reply_markup=buttons.back_to_main
        )

    phone = text.replace("+", "").strip()
    existing = await Account.get_or_none(phone=phone)
    if existing:
        return await message.reply(
            "❌ این شماره تلفن قبلاً در سیستم ثبت شده است",
            reply_markup=buttons.back_to_main
        )

    wait_message = await message.reply("🔄 در حال ارسال کد تأیید به تلگرام...")

    try:
        tmp_client = Client(
            f"acc_{phone}",
            settings.API_ID,
            settings.API_HASH,
            in_memory=True
        )
        await tmp_client.connect()
        sent_code = await tmp_client.send_code(text)

        await State.set(chat_id, "get_code")
        await UserData.set(chat_id, "client", tmp_client)
        await UserData.set(chat_id, "phone", text)
        await UserData.set(chat_id, "api_id", settings.API_ID)
        await UserData.set(chat_id, "api_hash", settings.API_HASH)
        await UserData.set(chat_id, "phone_code_hash", sent_code.phone_code_hash)


        logger.info("Code send to %s", phone)
        return await wait_message.edit(
            f"✅ کد تأیید به اکانت تلگرام شماره `{phone}` ارسال شد.\n\n"
            "لطفاً کد را وارد کنید:",
            reply_markup=buttons.code_keyboard()
        )

    except PhoneNumberInvalid:
        logger.warning("Invalid phone number: %s", phone)
        return await wait_message.edit(
            "❌ شماره تلفن نامعتبر است!\n"
            "لطفاً شماره را با فرمت صحیح وارد کنید:\n"
            "مثال: `+989123456789`",
            reply_markup=buttons.back_to_main
        )

    except PhoneNumberBanned:
        logger.warning("Banned phone number: %s", phone)
        return await wait_message.edit(
            "⛔ این شماره تلفن توسط تلگرام مسدود شده است.\n\n"
            "متأسفانه امکان ورود به این اکانت وجود ندارد.\n"
            "لطفاً از یک شماره تلفن دیگر استفاده کنید.",
            reply_markup=buttons.back_to_main
        )

    except PhoneNumberFlood:
        logger.warning("Flood phone number: %s", phone)
        return await wait_message.edit(
            "⚠️ برای این شماره درخواست‌های زیادی ارسال شده است.\n"
            "تلگرام به‌صورت موقت ارسال کد را محدود کرده.\n\n"
            "⏳ لطفاً چند دقیقه تا چند ساعت بعد دوباره تلاش کنید.",
            reply_markup=buttons.back_to_main
        )

    except Exception as error:
        logger.exception("Error to send code for (%s): %s", phone, error)
        return await wait_message.edit(
            f"❌ خطایی رخ داد:\n`{str(error)}`",
            reply_markup=buttons.back_to_main
        )