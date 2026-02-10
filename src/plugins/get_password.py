from utils import State
from utils.filters import state
from utils.state import UserData
from core.config import settings
from pyrogram.types import Message
from database.models import Account
from pyrogram import Client, filters


@Client.on_message(state("get_password") & filters.user(settings.ADMIN))
async def get_password(client: Client, message: Message):
    user_id = message.from_user.id
    password = message.text

    phone: str = await UserData.get(user_id, "phone")
    tmp_client: Client = await UserData.get(user_id, "client")
    api_id = await UserData.get(user_id, "api_id")
    api_hash = await UserData.get(user_id, "api_hash")
    device_model = await UserData.get(user_id, "device_model")
    system_version = await UserData.get(user_id, "system_version")

    try:
        await tmp_client.check_password(password)
    except Exception:
        return await message.reply("❌ پسورد اشتباه است")

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

    await message.reply("✅ اکانت با موفقیت اضافه شد")