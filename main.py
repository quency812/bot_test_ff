from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
import asyncio
from data import put_info, get_info, create
from markup import main_keyboard, find_by

bot = Bot("6416221486:AAHVV8ZwUNWVPm1tiBTOVs7B_-RNO4xiKGE")
dp = Dispatcher()


@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer(f"Главное меню", reply_markup=main_keyboard())
    create()


c = 0
data_lst = []


@dp.message(F.text == "Создать")
async def without_puree(message: Message):
    global c, data_lst
    await message.reply("Введите id ")
    c = 1


@dp.message(F.text == "Найти человека")
async def without_puree(message: Message):
    global c
    await message.reply("Выберете по чеум искать", reply_markup=find_by())


@dp.message(F.text == "НАЗАД")
async def without_puree(message: Message):
    await message.answer(f"Главное меню", reply_markup=main_keyboard())


@dp.message(F.text == "ID")
async def without_puree(message: Message):
    global c
    await message.reply("Введите ID", reply_markup=find_by())
    c = 4


@dp.message(F.text == "TG")
async def without_puree(message: Message):
    global c
    await message.reply("Введите TG", reply_markup=find_by())
    c = 5


@dp.message(F.text == "CHANEL")
async def without_puree(message: Message):
    global c
    await message.reply("Введите CHANEL", reply_markup=find_by())
    c = 6


@dp.message(F.text)
async def without_puree(message: Message):
    global c, data_lst
    if c == 1:
        data_lst.append(message.text)
        await message.reply("Введите tg ")
        c = 2
    elif c == 2:
        data_lst.append(message.text)
        await message.reply("Введите chanel ")
        c = 3
    elif c == 3:
        data_lst.append(message.text)
        c = 0
        put_info(data_lst)
        data_lst = []
    elif c == 4:
        c = 0
        await message.reply("Поиск по ID")
        print("id", message.text)
        await message.answer(get_info("id", message.text))
    elif c == 5:
        c = 0
        await message.reply("Поиск по TG")
        print("tg", message.text)
        await message.answer(get_info("tg", message.text))
    elif c == 6:
        c = 0
        await message.reply("Поиск по CHANEL")
        print("chanel", message.text)
        await message.answer(get_info("chanel", message.text))


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        print("Бот работает")
        asyncio.run(main())
    except:
        print("Бот перестал работать")
