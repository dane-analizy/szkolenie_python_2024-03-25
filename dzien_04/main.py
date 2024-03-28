# pip install requests

# import requests


# # poprawne zapytanie o istniejący adres
# response = requests.get("https://google.com/")
# print(response)

# print(response.status_code)

# # nie ma takiego adresu
# response = requests.get("https://google.com/dupa123")
# print(response)

# print(response.status_code)


# import requests
# import json

# # poprawne zapytanie o istniejący adres
# response = requests.get("https://jsystems.pl/Universe/samaTabelka.do")

# print(response.status_code)

# content = response.content.decode()
# print(content)
# print("=" * 80)
# lista_szkolen = json.loads(content)
# print(lista_szkolen)
# print("=" * 80)
# print(response.json())


# import requests
# print(requests.get("https://api.nbp.pl/api/exchangerates/tables/a/?format=json").json())


# ZADANIE

"""
Korzystając z API NBP - endpoint: https://api.nbp.pl/api/exchangerates/tables/a/?format=json
pobierz listę aktualnych notowań i wyświetl z niej notowania walut: EUR, USD, CHF.
"""

# import requests
# get do endpointa https://api.nbp.pl/api/exchangerates/tables/a/?format=json
# odpowiedź via .json() do listy dictów
# w kluczu rates jest tabela z notowaniami walut
# z tej tabeli trzeba wyjąć odpowiednie elementy z kluczem code pasującym do waluty i je wyświetlić

# import requests


# BASE_URL = "https://api.nbp.pl/api/exchangerates/tables/a/?format=json"
# OBSLUGIWANE_WALUTY = ("EUR", "CHF", "USD", "IDR")


# res = requests.get(BASE_URL)

# if res.status_code != 200:
#     print(f"Problem z usługą {BASE_URL}")
#     exit()

# cala_odpowiedz = res.json()
# tabela_kursow = cala_odpowiedz[0]["rates"]

# for el in tabela_kursow:
#     if el["code"] in OBSLUGIWANE_WALUTY:
#         print(f'Aktualny kurs {el["currency"]} ({el["code"]}) = {el["mid"]}')


# konfiguracja - yaml
# https://blog.prokulski.science/2021/03/29/pliki-konfiguracyjne-python-r/


# pip install pyyaml

import yaml
import requests


# plik z konfiguracją"
CONFIG_FILE = "waluty.yaml"


# wczytanie konfiguracji
with open(CONFIG_FILE, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)


# odpytanie NBP
res = requests.get(config['BASE_URL'])

# czy udało się poprawnie odpytać NBP
if res.status_code != 200:
    print(f"Problem z usługą {config['BASE_URL']}")
    exit()

# przetworzenie odpowiedzi z NBP
cala_odpowiedz = res.json()
tabela_kursow = cala_odpowiedz[0]["rates"]

# wyświetlenie kursów wg listy z konfigu
for el in tabela_kursow:
    if el["code"] in config['OBSLUGIWANE_WALUTY']:
        print(f'Aktualny kurs {el["currency"]} ({el["code"]}) = {el["mid"]}')
