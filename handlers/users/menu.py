from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.namoz import menu
from loader import dp
import requests
city = 'tashkent'
url = f"https://api.pray.zone/v2/times/today.json?city=tashkent&juristic=1"
r = requests.get(url)
res = r.json()
gregorian_date = res['results']['datetime'][0]['date']['gregorian']
hijri_date = res['results']['datetime'][0]['date']['hijri']
times = res['results']['datetime'][0]['times']
Bomdod = res['results']['datetime'][0]['times']['Fajr']
Quyosh = res['results']['datetime'][0]['times']['Sunrise']
Peshin = res['results']['datetime'][0]['times']['Dhuhr']
Asr = res['results']['datetime'][0]['times']['Asr']
Shom = res['results']['datetime'][0]['times']['Maghrib']
Xufton = res['results']['datetime'][0]['times']['Isha']





@dp.message_handler(Command("Namoz_Vaqti"))
async def send_link(message: Message):
    await message.answer("Tilni Tanlang \nChoose Language", reply_markup=menu)
@dp.message_handler(text='Log Out')
async def send_link(message: Message):
    await message.answer("Foydalanganingiz uchun Rahmat πππ", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text='Uzbek')
async def send_link(message: Message):
    await message.answer(f"πHijri kun: {hijri_date} πGregorian kun: {gregorian_date}\n"
                        f"π° Bomdod ππ» {Bomdod}\n"
                        f"π° Quyosh ππ» {Quyosh}\n"
                        f"π° Peshin ππ» {Peshin}\n"
                        f"π° Asr ππ» {Asr}\n"
                        f"π° Shom ππ» {Shom}\n"
                        f"π° Xufton ππ» {Xufton}\n")
@dp.message_handler(text='English')
async def send_link(message: Message):
    await message.answer(f"π Hijri Date: {hijri_date} π Gregorian Date: {gregorian_date}\n"
                        f"π° Fajr ππ» {Bomdod}\n"
                        f"π° Sunrise ππ» {Quyosh}\n"
                        f"π° Dhuhr ππ» {Peshin}\n"
                        f"π° Asr ππ» {Asr}\n"
                        f"π° Maghrib ππ» {Shom}\n"
                        f"π° Isha ππ» {Xufton}\n")
