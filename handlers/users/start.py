from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.namoz import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu Alaykum, {message.from_user.full_name}!")
    await message.answer("Tilni Tanlang \nChoose Language", reply_markup=menu)