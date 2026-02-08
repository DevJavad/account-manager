import logging
from typing import Optional
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

filters.create()


def button(data: str):
    async def func(_, __, query: CallbackQuery):
        return query.data == data

    return filters.create(func)