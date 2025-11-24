import os
os.system("cls")

import requests as rq

url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/'

data = rq.get(url).json()

print(data[0])