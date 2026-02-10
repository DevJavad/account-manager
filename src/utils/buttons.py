from database.models import Account
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

start: InlineKeyboardMarkup = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("📱 لیست اکانت‌ها", "accounts_list"),
        InlineKeyboardButton("📊 آمار سیستم", "system_stats")
    ],
    [
        InlineKeyboardButton("➕ افزودن اکانت جدید", "add_account"),
        InlineKeyboardButton("🔄 بروزرسانی اطلاعات", "update_data")
    ],
])

back_to_main = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 بازگشت", "back_to_main")]]
)


def accounts_list(accounts: list[Account]) -> InlineKeyboardMarkup:
    rows = []
    row = []

    for account in accounts:
        row.append(
            InlineKeyboardButton(
                f"📱 {account.phone}", callback_data=f"acc:{account.id}")
        )

        if len(row) == 2:
            rows.append(row)
            row = []

    if row:
        rows.append(row)

    return InlineKeyboardMarkup(rows)


def code_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton("1", callback_data="num:1"),
            InlineKeyboardButton("2", callback_data="num:2"),
            InlineKeyboardButton("3", callback_data="num:3")
        ],
        [
            InlineKeyboardButton("4", callback_data="num:4"),
            InlineKeyboardButton("5", callback_data="num:5"),
            InlineKeyboardButton("6", callback_data="num:6")
        ],
        [
            InlineKeyboardButton("7", callback_data="num:7"),
            InlineKeyboardButton("8", callback_data="num:8"),
            InlineKeyboardButton("9", callback_data="num:9")
        ],
        [
            InlineKeyboardButton("⌫ حذف", callback_data="num:del"),
            InlineKeyboardButton("0", callback_data="num:0"),
            InlineKeyboardButton("✅ ارسال", callback_data="num:send")
        ],
        [
            InlineKeyboardButton("🔙 بازگشت", callback_data="back_to_main")
        ]
    ]

    return InlineKeyboardMarkup(buttons)


def acc_panel(id: int) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton("🔧 پنل مدیریت", f"panel:{id}"),
            InlineKeyboardButton("🗑 حذف اکانت", f"delete_acc:{id}")
        ],
        [
            InlineKeyboardButton("🔄 به‌روزرسانی اطلاعات", f"refresh_acc:{id}"),
            InlineKeyboardButton("📤 ارسال پیام", f"send_msg:{id}")
        ],
        [
            InlineKeyboardButton("🔙 بازگشت به لیست", "account_list")
        ]
    ]

    return InlineKeyboardMarkup(buttons)