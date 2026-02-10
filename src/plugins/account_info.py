import logging
from utils.filters import state
from utils import State, buttons
from utils.state import UserData
from core.config import settings
from database.models import Account
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import CallbackQuery


logger = logging.getLogger(__name__)


@Client.on_callback_query(filters.regex(r"^acc:(\d+)$") & filters.user(settings.ADMIN))
async def account_info(client: Client, query: CallbackQuery):
    acc_id = int(query.matches[0].group(1))

    account = await Account.get_or_none(id=acc_id)

    if not account:
        return await query.answer("❌ اکانت مورد نظر یافت نشد!", show_alert=True)

    try:
        premium_status = "✅" if account.is_premium else "❌"

        info_text = (
            f"📱 <b>اطلاعات اکانت #{account.id}</b>\n\n"
            f"📞 <b>شماره تلفن:</b> <code>{account.phone}</code>\n"
            f"🆔 <b>آیدی چت:</b> <code>{account.chat_id}</code>\n\n"

            f"👤 <b>اطلاعات کاربری:</b>\n"
            f"   • نام: {account.first_name or '—'}\n"
            f"   • نام خانوادگی: {account.last_name or '—'}\n"
            f"   • نام کامل: {account.full_name or '—'}\n"
            f"   • یوزرنیم: @{account.username or '—'}\n"
            f"   • بیوگرافی: {account.bio or '—'}\n\n"

            f"⚙️ <b>اطلاعات فنی:</b>\n"
            f"   • API ID: <code>{account.api_id}</code>\n"
            f"   • API Hash: <code>{account.api_hash[:20]}...</code>\n"
            f"   • مدل دستگاه: <code>{account.device_model}</code>\n"
            f"   • نسخه سیستم: <code>{account.system_version}</code>\n"
            f"   • وضعیت پرمیوم: {premium_status}\n"
        )

        await query.edit_message_text(
            info_text,
            reply_markup=buttons.acc_panel(acc_id),
            parse_mode=ParseMode.HTML,
        )

    except Exception as error:
        logger.error("Error to show account info %s: %s", acc_id, error)
        await query.answer("❌ خطایی در نمایش اطلاعات رخ داد!", show_alert=True)