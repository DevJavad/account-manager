from .state import State
from pyrogram.filters import create
from pyrogram.types import CallbackQuery, Message


def button(data: str):
    async def func(_, __, query: CallbackQuery):
        return query.data == data

    return create(func)


def state(name: str):
    async def func(_, __, update: CallbackQuery | Message):
        state = await State.get(update.from_user.id)
        return state == name

    return create(func)