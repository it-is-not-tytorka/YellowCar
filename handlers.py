# код для бота, ответы на сообщения

from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

import kb
import text

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Hello world")


@router.message(F.text == "Menu")
@router.message(F.text == "Enter to menu")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

@router.message(Command("whoami"))
async def who_am_i_handler(msg: Message):
    if msg.from_user.id == 526156868:
        await msg.answer(f"My lord")
    elif msg.from_user.id == 1608449223:
        await msg.answer(f"Мой любимый лисенок")
    else:
        await msg.answer(f"I know your name, {msg.from_user.full_name}")


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Your ID: {msg.from_user.id}")
