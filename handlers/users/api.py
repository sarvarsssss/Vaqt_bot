import requests
from pprint import pprint as print



city = 'tashkent'

url = f"https://api.pray.zone/v2/times/today.json?city=tashkent&juristic=1"

r = requests.get(url)
print((r.status_code))
res = r.json()
gregorian_date = res['results']['datetime'][0]['date']['gregorian']
hijri_date = res['results']['datetime'][0]['date']['hijri']
times = res['results']['datetime'][0]['times']
Bomdod = res['results']['datetime'][0]['times']['Fajr']
Quyosh = res['results']['datetime'][0]['times']['Sunrise']
Peshin = res['results']['datetime'][0]['times']['Dhuhr']
Asr = res['results']['datetime'][0]['times']['Fajr']
Shom = res['results']['datetime'][0]['times']['Maghrib']
Xufton = res['results']['datetime'][0]['times']['Isha']