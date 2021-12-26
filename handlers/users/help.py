from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "Assalamu Alaykum \nBu bot orqali siz namoz vaqtlaini bilib olishingiz mumkin \nVa bu bot har kuni yangilangan vaqtni ko'rsatadi 😊😊😊",)
    
    await message.answer("\n".join(text))
