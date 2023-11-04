# импортирование необходимых библиотек 
import asyncio # асинхронный запуск бота
import logging # логи очев

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode # разметка сообщений html, md
from aiogram.fsm.storage.memory import MemoryStorage # состояние пользователей

import config
from handlers import router

async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage()) # все данные, не сохраненные в БД, будут стерты
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True) # delete all updates after bot worked. it means that bot don't answer to msgs when it didn't run
    await dp.start_polling(bot,allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
