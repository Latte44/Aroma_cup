import asyncio
from aiogram import Bot,Dispatcher
from aiogram.types import BotCommand
from commands import router as commands_router
from comandsbasket import router as basket_router
import os 
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(commands_router)
dp.include_router(basket_router)

async def set_commands(bot:Bot):
    commands = [
        BotCommand(command= "start", description= "Почети роботу"),
        BotCommand(command= "menu", description= "Меню"),
        BotCommand(command= "coffee", description= "Кава"),
        BotCommand(command= "desserts", description= "Дессерти"),
        BotCommand(command= "basket", description= "Кошик"),
        BotCommand(command= "Latte", description= "Лате"),
        BotCommand(command= "Cappuccino", description= "Капучино"),
        BotCommand(command= "Americano", description= "Американо"),
        BotCommand(command= "Espresso", description= "Еспресо"),
        BotCommand(command= "Croissant", description= "Круасан"),
        BotCommand(command= "Eclair", description= "Еклер"),
        BotCommand(command= "clear_basket", description= "clear"),
        BotCommand(command= "info", description= "info")
    ]


async def main():
    await set_commands(bot)
    print("бот запущено")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())