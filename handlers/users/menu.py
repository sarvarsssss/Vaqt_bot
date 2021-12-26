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
    await message.answer("Foydalanganingiz uchun Rahmat 😊😊😊", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text='Uzbek')
async def send_link(message: Message):
    await message.answer(f"🗓Hijri kun: {hijri_date} 🗓Gregorian kun: {gregorian_date}\n"
                        f"🕰 Bomdod 👉🏻 {Bomdod}\n"
                        f"🕰 Quyosh 👉🏻 {Quyosh}\n"
                        f"🕰 Peshin 👉🏻 {Peshin}\n"
                        f"🕰 Asr 👉🏻 {Asr}\n"
                        f"🕰 Shom 👉🏻 {Shom}\n"
                        f"🕰 Xufton 👉🏻 {Xufton}\n")
@dp.message_handler(text='English')
async def send_link(message: Message):
    await message.answer(f"🗓 Hijri Date: {hijri_date} 🗓 Gregorian Date: {gregorian_date}\n"
                        f"🕰 Fajr 👉🏻 {Bomdod}\n"
                        f"🕰 Sunrise 👉🏻 {Quyosh}\n"
                        f"🕰 Dhuhr 👉🏻 {Peshin}\n"
                        f"🕰 Asr 👉🏻 {Asr}\n"
                        f"🕰 Maghrib 👉🏻 {Shom}\n"
                        f"🕰 Isha 👉🏻 {Xufton}\n")
