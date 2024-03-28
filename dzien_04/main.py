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

# import yaml
# import requests


# # plik z konfiguracją"
# CONFIG_FILE = "waluty.yaml"


# # wczytanie konfiguracji
# with open(CONFIG_FILE, "r", encoding="utf-8") as f:
#     config = yaml.safe_load(f)


# # odpytanie NBP
# res = requests.get(config['BASE_URL'])

# # czy udało się poprawnie odpytać NBP
# if res.status_code != 200:
#     print(f"Problem z usługą {config['BASE_URL']}")
#     exit()

# # przetworzenie odpowiedzi z NBP
# cala_odpowiedz = res.json()
# tabela_kursow = cala_odpowiedz[0]["rates"]

# # wyświetlenie kursów wg listy z konfigu
# for el in tabela_kursow:
#     if el["code"] in config['OBSLUGIWANE_WALUTY']:
#         print(f'Aktualny kurs {el["currency"]} ({el["code"]}) = {el["mid"]}')


# ZADANIE

"""
Utwórz nowy pakiet "tools" z modułem "internet" oraz modułem "config".

W "internet" powinna znaleźć się funkcja get_json_from_url() , która z podanego jako argument adresu URL pobiera zawartość i zwraca JSON (słownik). Jeśli w pobranej
zawartości jest lista - zwracamy pierwszy element z tej listy. Jeśli nie uda się pobrać zawartości to zwracany jest pusty słownik "return {}".

W "config" wrzuć funkcję czytającą konfigurację z pliku YAML podanego jako parametr - read_config()
"""


# from tools.internet import get_json_from_url
# from tools.config import read_config

# config = read_config("waluty.yaml")

# res = get_json_from_url(config["BASE_URL"])
# tabela_kursow = res["rates"]

# for el in tabela_kursow:
#     if el["code"] in config['OBSLUGIWANE_WALUTY']:
#         print(f'Aktualny kurs {el["currency"]} ({el["code"]}) = {el["mid"]}')


# ZADANIE
"""
Używając przygotowanego wcześniej pakietu:
 - pobierz listę notować USD z okresu 2023-01-01 do 2024-03-28 ("https://api.nbp.pl/api/exchangerates/rates/a/usd/2024-01-01/2024-03-28/?format=json")
 - do pliku USD.csv zapisz wszystkie pobrane wartości w formacie: data, numer notowania i kurs
"""


"""
Odpowiedź z API:
{
    ...
    "rates": [
        {
            "no": "001/A/NBP/2024",
            "effectiveDate": "2024-01-02",
            "mid": 3.9432
        },
        {
            "no": "002/A/NBP/2024",
            "effectiveDate": "2024-01-03",
            "mid": 3.9909
        },
        ...
    ]
}
"""


# from tools.internet import get_json_from_url

# DATA_OD = "2024-01-01"
# DATA_DO = "2024-03-28"

# API_URL = (
#     f"https://api.nbp.pl/api/exchangerates/rates/a/usd/{DATA_OD}/{DATA_DO}/?format=json"
# )


# def nbp_rates_to_tuple(notowania):
#     return [tuple([el["effectiveDate"], el["no"], el["mid"]]) for el in notowania]


# def tuple_list_to_file(lista_elementow, lista_nazw, nazwa_pliku):
#     with open(nazwa_pliku, "w", encoding="utf-8") as f:

#         wiersz_naglowek = ";".join([str(e) for e in lista_nazw])
#         f.write(wiersz_naglowek + "\n")

#         for el in lista_elementow:
#             wiersz = ";".join([str(e) for e in el])
#             f.write(wiersz + "\n")


# def main():
#     dane = get_json_from_url(API_URL)
#     notowania = dane["rates"]
#     notowania = nbp_rates_to_tuple(notowania)
#     tuple_list_to_file(
#         lista_elementow=notowania,
#         lista_nazw=["data", "tabela", "kurs"],
#         nazwa_pliku="usd.csv",
#     )


# if __name__ == "__main__":
#     main()


# wersja po przerzuceniu do tools/files.py funkcji tuple_list_to_file()


# from tools.files import tuple_list_to_file
# from tools.internet import get_json_from_url

# DATA_OD = "2024-01-01"
# DATA_DO = "2024-03-28"

# API_URL = (
#     f"https://api.nbp.pl/api/exchangerates/rates/a/usd/{DATA_OD}/{DATA_DO}/?format=json"
# )


# def nbp_rates_to_tuple(notowania):
#     return [tuple([el["effectiveDate"], el["no"], el["mid"]]) for el in notowania]


# def main():
#     dane = get_json_from_url(API_URL)
#     notowania = dane["rates"]
#     notowania = nbp_rates_to_tuple(notowania)
#     tuple_list_to_file(
#         lista_elementow=notowania,
#         lista_nazw=["data", "tabela", "kurs"],
#         nazwa_pliku="usd.csv",
#     )


# if __name__ == "__main__":
#     main()


# requests.POST - wysyłanie danych
# poligon doświadczalny https://httpbin.org/


# import requests

# res = requests.post("https://httpbin.org/post")
# print(res)

# print(res.json())


# import requests

# res = requests.post("https://httpbin.org/post?arg1=abs&arg2=123")
# print(res)

# print(res.json())


# import requests

# dane_json = {"klucz1": 1, "klucz2": "abc"}
# dane_data = "ciag bajtow"

# res = requests.post("https://httpbin.org/post", data=dane_data)
# print(res)

# print(res.json())


# import requests

# dane_json = {"klucz1": 1, "klucz2": "abc"}
# dane_data = "ciag bajtow"

# res = requests.post("https://httpbin.org/post", json=dane_json)
# print(res)

# print(res.json())


# import requests
# from requests.auth import HTTPBasicAuth

# login = "user1234"
# haslo = "tajne_haslo"

# res = requests.get(
#     "https://httpbin.org/basic-auth/user1234/tajne_haslo",
#     auth=HTTPBasicAuth(login, haslo)
# )
# print(res)
# print(res.json())


# ZADANIE

"""
Korzystają z API NBP (endpoint https://api.nbp.pl/api/exchangerates/rates/a/usd/2024-01-01/2024-03-26/?format=json)
pobierz tablicę z historycznymi notowaniami USD i wypisz na ekranie dni, w których dolar kosztował mniej niż 4 zł.
Wykorzystaj już przygotowane funkcje i pakiety
"""


"""
Odpowiedź z API:
{
    ...
    "rates": [
        {
            "no": "001/A/NBP/2024",
            "effectiveDate": "2024-01-02",
            "mid": 3.9432
        },
        {
            "no": "002/A/NBP/2024",
            "effectiveDate": "2024-01-03",
            "mid": 3.9909
        },
        ...
    ]
}
"""


# from tools.internet import get_json_from_url

# notowania_usd = get_json_from_url(
#     "https://api.nbp.pl/api/exchangerates/rates/a/usd/2024-01-01/2024-03-26/?format=json"
# )

# notowania_usd_pod_4zl = [
#     (dzien["effectiveDate"], dzien["mid"])
#     for dzien in notowania_usd["rates"]
#     if dzien["mid"] < 4
# ]

# notowania_usd_pod_4zl = sorted(notowania_usd_pod_4zl, key=lambda t: t[1])

# for d in notowania_usd_pod_4zl:
#     print(d[0], d[1])


# w DBeaver -> SQL editor -> Open SQL Console, wkleić kod, zaznaczyć i uruchomić: Run SQL Query (pod prawym guzikiem) albo Ctrl+Enter)

"""
create table players (
	player_id serial primary key,
	first_name text not null,
	last_name text not null,
	height numeric not null,
	weight numeric not null
);

insert into players (first_name,last_name,height,weight)  
values ('Jan', 'Kowalski', 1.84, 85);  
  
insert into players (first_name,last_name,height,weight)  
values ('Marian', 'Nowak', 1.90, 50);  
  
insert into players (first_name,last_name,height,weight)  
values ('Zdzisław', 'Dyrman', 1.73 ,74);  
  
insert into players (first_name,last_name,height,weight)  
values ('Zenon', 'Brzęczyk', 1.64, 95);  
  
insert into players (first_name,last_name,height,weight)  
values ('Chuck','Norris', 1.82, 78);  
  
insert into players (first_name,last_name,height,weight)  
values ('Krzysztof','Jarzyna', 1.68, 70);

"""


# pakiet SQLAlchemy - zainstaluj przez: pip install sqlalchemy

# pakiety do konkretnych silników baz danych
"""
- pakiet do łączenia się z postgresql
    - `pip install psycopg2`
- pakiet do łączenia się z Oraclem
    - `pip install cx_oracle`
- pakiet do łączenia się z MS SQL
    - `pip install pymssql`
"""

# jak budować connection string - per baza / pakiet
# https://docs.sqlalchemy.org/en/20/core/engines.html#backend-specific-urls


from sqlalchemy import create_engine
from tools.config import read_config

db_config = read_config("db_config.yaml")
print(db_config)


conn_str = f"postgresql+psycopg2://{db_config['db_user']}:{db_config['db_pass']}@{db_config['db_host']}:{db_config['db_port']}/{db_config['db_name']}"
engine = create_engine(conn_str)
print(engine)
