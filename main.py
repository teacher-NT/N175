import os
os.system("cls")
books = {
    "O'tkan kunlar": {
        "muallifi": "Abdulla Qodiriy",
        "janri": "Roman",
        "chop etilgan yili": 1926,
        "tarjimalar soni": 5
    },
    "Mehrobdan chayon": {
        "muallifi": "Abdulla Qodiriy",
        "janri": "Roman",
        "chop etilgan yili": 1929,
        "tarjimalar soni": 3
    },
    "Kecha va kunduz": {
        "muallifi": "Cho'lpon",
        "janri": "Roman",
        "chop etilgan yili": 1934,
        "tarjimalar soni": 4
    },
    "Sarob": {
        "muallifi": "Abdulla Qahhor",
        "janri": "Roman",
        "chop etilgan yili": 1935,
        "tarjimalar soni": 2
    },
    "Ulug'bek xazinasi": {
        "muallifi": "Odil Yoqubov",
        "janri": "Tarixiy roman",
        "chop etilgan yili": 1974,
        "tarjimalar soni": 6
    },
    "Don Kixot": {
        "muallifi": "Migel de Servantes",
        "janri": "Roman",
        "chop etilgan yili": 1605,
        "tarjimalar soni": 50
    },
    "Urush va tinchlik": {
        "muallifi": "Lev Tolstoy",
        "janri": "Tarixiy roman",
        "chop etilgan yili": 1869,
        "tarjimalar soni": 45
    },
    "Alkimyogar": {
        "muallifi": "Paulo Koelyo",
        "janri": "Falsafiy roman",
        "chop etilgan yili": 1988,
        "tarjimalar soni": 80
    },
    "1984": {
        "muallifi": "Jorj Oruell",
        "janri": "Antiutopik roman",
        "chop etilgan yili": 1949,
        "tarjimalar soni": 65
    },
    "Kichkina shahzoda": {
        "muallifi": "Antuan de Sent-Ekzyuperi",
        "janri": "Falsafiy ertak",
        "chop etilgan yili": 1943,
        "tarjimalar soni": 300
    }
}

name = 'urush Va Tinchlik'

# print(books[name])
for book in books:
    if name.lower() == book.lower():
        print(books[book])
        break
else:
    print("Kitob topilmadi")
