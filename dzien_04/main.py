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
# get do endpointa
# odpowiedź via .json() do listy dictów
# w kluczu rates jest tabela z notawoaniami walut
# z tej tablei trzeba wyjąć odpowiednie elementy z kluczem code pasującym do waluty i je wywietlić