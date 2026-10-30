import asyncio
from aiogram import Bot,Dispatcher
from aiogram.types import BotCommand
from commands import router

TOKEN = ""
bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(router)
async def set_commands(bot:Bot):
    commands = [
        BotCommand(command= "start", description= "Почети роботу"),
        BotCommand(command= "menu", description= "Меню"),
        BotCommand(command= "coffee", description= "Кава")
    ]

async def main():
    await set_commands(bot)
    print("бот запущено")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())