import asyncio
from typing import Any


class State:
    states: dict[int, str] = {}
    lock = asyncio.Lock()

    @classmethod
    async def set(cls, user_id: int, state: str):
        async with cls.lock:
            cls.states[user_id] = state

    @classmethod
    async def get(cls, user_id: int) -> str | None:
        async with cls.lock:
            return cls.states.get(user_id)

    @classmethod
    async def delete(cls, user_id: int):
        async with cls.lock:
            cls.states.pop(user_id, None)


class UserData:
    data: dict[int, dict[str, str]] = {}
    lock = asyncio.Lock()

    @classmethod
    async def set(cls, user_id: int, key: str, value: Any):
        async with cls.lock:
            if user_id not in cls.data:
                cls.data[user_id] = {}

            cls.data[user_id][key] = value

    @classmethod
    async def get(cls, user_id: int, key: str | None = None) -> Any:
        async with cls.lock:
            if key is None:
                return cls.data.get(user_id)

            return cls.data.get(user_id, {}).get(key)

    @classmethod
    async def delete(cls, user_id: int, key: str | None = None):
        async with cls.lock:
            if user_id not in cls.data:
                return

            if key is None:
                cls.data.pop(user_id)
            else:
                cls.data[user_id].pop(key, None)
                if not cls.data[user_id]:
                    cls.data.pop(user_id)