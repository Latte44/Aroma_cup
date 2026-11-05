from aiogram import Router,types
from aiogram.filters import Command
from aiogram.types import FSInputFile
from data_coffee import get_coffee
from data_desserts import get_desserts


router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привіт це меню Aroma cup. \n "
                         "/info щоб побачити команди")

@router.message(Command("menu"))
async def cmd_menu(message: types.Message):
    await message.answer("Кава - /coffee або десерт - /desserts")

@router.message(Command("info"))
async def cmd_menu(message: types.Message):
    await message.answer("Меню - /menu \n"
                         "Кошик - /basket \n"
                         "Подивитися кошик /Look_basket \n"
                         "Очистити кошик /clear_basket")

@router.message(Command("coffee"))
async def cmd_coffee(message: types.Message):
    coffee = get_coffee()

    for item in coffee:
        text = f"{item['name']} {item['price']} \n {item['ingredients']}"
        poster = item.get("poster")

        if poster:
            await message.answer_photo(FSInputFile(poster), caption=text)
        else:
            await message.answer(text)


@router.message(Command("desserts"))
async def cmd_desserts(message: types.Message):
    desserts = get_desserts()

    for item in desserts:
        text = f"{item['name']} {item['price']} \n {item['ingredients']}"
        poster = item.get("poster")

        if poster:
            await message.answer_photo(FSInputFile(poster), caption=text)
        else:
            await message.answer(text)