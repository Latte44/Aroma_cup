from aiogram import Router,types
from aiogram.filters import Command
from aiogram.types import FSInputFile
from data_Basket import get_basket
import os
import json

router = Router()

@router.message(Command("basket"))
async def cmd_menu(message: types.Message):
    print("basket Сработал")
    await message.answer("що додати до кошика \n"
                         "/Latte \n"
                         "/Cappuccino \n"
                         "/Americano \n"
                         "/Espresso \n"
                         "/Croissant \n"
                         "/Eclair \n")

z = os.path.dirname(__file__)
file = os.path.join(z, "basket.json")

def save_to_json(data):
    try:
        with open(file, "r", encoding="utf-8") as f:
            basket = json.load(f)
    except:
        basket = []

    basket.append(data)

    with open(file, "w", encoding="utf-8") as f:
        json.dump(basket, f, ensure_ascii=False, indent=4)

@router.message(Command("Look_basket"))
async def cmd_menu(message: types.Message):
    basket = get_basket()
    
    text = "Ваш кошик \n \n"
    total = 0

    for item in basket:
        text += f"{item['name']} - {item['price']} грн\n"
        total = total + item["price"]

    text += f"Разом: {total} грн"
    await message.answer(text)


@router.message(Command("Latte"))
async def cmd_menu(message: types.Message):
    Latte = {"name": "Latte","price": 75}

    save_to_json(Latte)

@router.message(Command("Cappuccino"))
async def cmd_menu(message: types.Message):
    Cappuccino = {"name": "Cappuccino", "price": 65}

    save_to_json(Cappuccino)

@router.message(Command("Americano"))
async def cmd_menu(message: types.Message):
    Americano = {"name": "Americano", "price": 45}

    save_to_json(Americano)

@router.message(Command("Espresso"))
async def cmd_menu(message: types.Message):
    Espresso = {"name": "Espresso", "price": 40}

    save_to_json(Espresso)

@router.message(Command("Croissant"))
async def cmd_menu(message: types.Message):
    Croissant = {"name": "Croissant", "price": 50}

    save_to_json(Croissant)

@router.message(Command("Eclair"))
async def cmd_menu(message: types.Message):
    Eclair = {"name": "Eclair", "price": 30}

    save_to_json(Eclair)

@router.message(Command("clear_basket"))
async def cmd_clear_basket(message: types.Message):
    print("clear_basket сработал")
    with open(file, "w", encoding="utf-8") as f:
        json.dump([], f)
    await message.answer(f"кошик очищений")