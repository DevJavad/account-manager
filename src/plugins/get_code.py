import logging
from utils.filters import state
from utils import State, buttons
from utils.state import UserData
from core.config import settings
from database.models import Account
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery
from pyrogram.errors import (
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
)


logger = logging.getLogger(__name__)


@Client.on_callback_query(state("get_code") & filters.regex(r"^num:(.+)") & filters.user(settings.ADMIN))
async def get_code(client: Client, query: CallbackQuery):
    message = query.message
    user_id = query.from_user.id

    pressed = query.matches[0].group(1)

    code = await UserData.get(user_id, "code")
    code = code or ""

    if pressed == "del":
        code = code[:-1]

    elif pressed == "send":
        if len(code) != 5:
            return await query.answer("کد باید ۵ رقمی باشد", True)

        await query.answer("در حال ورود...")

        phone_code_hash = await UserData.get(user_id, "phone_code_hash")
        tmp_client: Client = await UserData.get(user_id, "client")
        phone: str = await UserData.get(user_id, "phone")
        api_id = await UserData.get(user_id, "api_id")
        api_hash = await UserData.get(user_id, "api_hash")
        device_model = await UserData.get(user_id, "device_model")
        system_version = await UserData.get(user_id, "system_version")

        try:
            await tmp_client.sign_in(phone, phone_code_hash, code)

        except PhoneCodeInvalid:
            return await query.answer("❌ کد وارد شده اشتباه است", True)

        except PhoneCodeExpired:
            return await query.answer("⏰ کد منقضی شده، دوباره تلاش کنید", True)

        except SessionPasswordNeeded:
            await State.set(user_id, "get_password")
            return await message.edit_text(
                "🔐 این اکانت رمز دو مرحله‌ای دارد.\n"
                "لطفاً پسورد را ارسال کنید:",
                reply_markup=buttons.back_to_main
            )

        session_string = await tmp_client.export_session_string()
        me = await tmp_client.get_me()
        await tmp_client.disconnect()

        await Account.create(
            phone=phone.replace("+", ""),
            api_id=api_id,
            api_hash=api_hash,
            session_string=session_string,
            device_model=device_model,
            system_version=system_version,
            chat_id=me.id,
            is_premium=me.is_premium,
            first_name=me.first_name,
            last_name=me.last_name,
            full_name=me.full_name,
            username=me.username,
            bio=me.bio
        )

        await State.delete(user_id)
        await UserData.delete(user_id)

        return await message.edit_text("✅ اکانت با موفقیت اضافه شد")

    else:
        if len(code) >= 5:
            return await query.answer("کد کامل است", True)

        code += pressed

    await UserData.set(user_id, "code", code)

    display = code + "_"*(5-len(code))

    await message.edit_text(
        "🔢 کد تأیید:\n\n"
        f"`{display}`",
        reply_markup=buttons.code_keyboard()
    )

    await query.answer()