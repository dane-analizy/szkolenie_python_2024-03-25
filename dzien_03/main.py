# klucz jest krotką
# d = {
#     (1,2): [3, 4, 5],
#     (3,4): [6,7,8]
# }

# print(d)
# print( d[(3,4)])


# lista = [ i for i in range(10) ]
# d = {i: liczba for i, liczba in enumerate(range(10, 20))}
# print(d)
# print(d[7])

# ZADANIE

"""
Zbuduj słownik przez dict-comprehention, którego kluczem będzie krotka złożona z indeksu pętli i tego indeksu powiększonego o 1, a wartością kwadrat kolejnej liczby
od 0 do 20
"""
# d = { (i, i+1) ....  for i, liczba in enumerate(range(20)) }

# d = {(i, i + 1): liczba**2 for i, liczba in enumerate(range(20))}
# print(d)

# d = {(i, i + 1): i**2 for i in range(20)}


# FUNKCJE

# def funkcja():
#     print("Jestem w środku funkcji")

# print("jestem przed forem, poza funkcją")

# for _ in range(10):
#     funkcja()
#     print("a ja jestem poza funkcją w środku fora")

# print("a ja jestem poza funkcją i po zakończeniu fora")


# def czesc_janek():
#     print("Cześć Janek!")


# def czesc_ania():
#     print("Cześć Ania!")

# def pozdrow(imie):
#     print(f"Cześć {imie}!")

# pozdrow("Zdzichu")
# pozdrow("Basia")


# ZADANIE

"""
Napisz funkcję która na konsoli wypisze "Pozdrawiam IMIE", gdzie imie będzie podanym przez użytkownika ciągiem znaków (w ramach input).
Niech program zapyta o imię 2 razy i wywoła 2 razy przygotowaną funkcję.
"""

# nazwisko = "kowalski"

# def pozdrow(imie):
#     nazwisko = "nowak"
#     print(f"Cześć {imie} {nazwisko}!")
#     imie = "nadpisałem imię"
#     print(imie)


# for _ in range(2):
#     imie = input("Kogo chcesz pozdrowić?")
#     pozdrow(imie)
#     print(imie, nazwisko)


# def pozdrow(imie):
#     imie = input("1.Podaj imię")
#     print(f"Cześć {imie}!")


# pozdrow("Łukasz")


# def pozdrow(imie, wiek, miasto):
#     print(f"Cześć {imie}! Widzę, że masz {wiek} lat i mieszkasz w {miasto}")

# pozdrow("Łukasz", miasto="Warszawa", wiek=35)


# funkcje wywołują inne funkcje, wykorzystujemy zwracanie wartości przez return

# def przygotuj_pozdrowienie(imie, wiek, miasto):
#     pozdrowienie = f"Cześć {imie}! Widzę, że masz {wiek} lat i mieszkasz w {miasto}"
#     return pozdrowienie

# ciag_znakow = przygotuj_pozdrowienie("Ania", 25, "Kraków")
# print(ciag_znakow)
# print(ciag_znakow.split(" "))


# def przygotuj_pozdrowienie(imie, wiek, miasto):
#     pozdrowienie = f"Cześć {imie}! Widzę, że masz {wiek} lat i mieszkasz w {miasto}"
#     return pozdrowienie


# def rozbij_na_slowa(ciag):
#     print(ciag.split(" "))


# def pozdrow_w_kawalkach(imie, wiek, miasto):
#     ciag_znakow = przygotuj_pozdrowienie(imie, wiek, miasto)
#     rozbij_na_slowa(ciag_znakow)


# pozdrow_w_kawalkach("Ania", 25, "Kraków")


# wiele returnów

# def dzialanie(typ_dzialania, liczba_a, liczba_b):
#     if typ_dzialania == "dodawanie":
#         wynik = liczba_a + liczba_b
#     elif typ_dzialania == "odejmowanie":
#         wynik = liczba_a - liczba_b
#     else:
#         print("Nie znam tego działania")
#         wynik = None

#     print("skończyłem i zwracam wynik")
#     return wynik

# wynik_dzialania = dzialanie("dodawanie", 2, 4)

# # pokazanie wyniku
# print(wynik_dzialania)


# wynik_dzialania = dzialanie("mnożenie", 2, 4)

# # pokazanie wyniku
# print(wynik_dzialania)


# ZADANIE
"""
Napisz funkcję, która zwraca wartości:
     - -1 jeśli podana w parametrze liczba jest ujemna
     - +1 jesli podana w parametrze liczba jest dodatnia
     - 0 jeśli liczba z parametru jest zerem 
Wynik, który zwróci funkcja wypisz na ekranie
"""


# def jaka_liczba(liczba):
#     # sprawdzamy czy w ogóle mamy do czyniena z liczbą
#     try:
#         liczba_do_porownania = float(liczba)
#     except:
#         # to nie liczbza - mówimy o błędzie i wychodzimy z None
#         print(f"Nie umiem porównywać z zerem {liczba=}")
#         return None

#     # w tym miejscy mamy liczbę - sprawdzamy jak się ona ma do zera
#     if liczba_do_porownania < 0:
#         wynik = "-1"
#     elif liczba_do_porownania > 0:
#         wynik = "+1"
#     else:
#         wynik = "0"

#     return wynik


# testowe_wartosci = [-5, 5, 0, "ala ma kota"]
# for test in testowe_wartosci:
#     print(f"Testuję: {test=}")
#     moja_liczba = jaka_liczba(test)
#     print(f"Wynik: {moja_liczba=}", end="\n\n")


# wiele operacji w try

# wartosc = "0" # spróbuj z "-1", "1", "ala ma kota"
# try:
#     liczba = float(wartosc)
#     wynik = 1/liczba
#     print(wynik)
# except Exception as e:
#     print(e)

# print("Skonczyułem")


# isinstance - porównanie czy zmienna jest danego typu

# liczba = 12.3
# lista = [123,1241]

# # print(type(liczba))
# # print(type(lista))

# if isinstance(liczba, (int, float) ):
#     print("Zmienna liczba jest typu int albo float")
# else:
#     print("Zmienna liczba NIE jest typu int")


# wersja ze sprawdzaniem typu argumentu
# def jaka_liczba(liczba):
#     # sprawdzamy czy w ogóle mamy do czyniena z liczbą
#     if not isinstance(liczba, (int, float)):
#         print("Zły typ argumentu - musi być int albo float")
#         return None

#     # w tym miejscy mamy liczbę - sprawdzamy jak się ona ma do zera
#     if liczba < 0:
#         wynik = "-1"
#     elif liczba > 0:
#         wynik = "+1"
#     else:
#         wynik = "0"

#     return wynik


# testowe_wartosci = [-5, 5.5, 0, "ala ma kota"]
# for test in testowe_wartosci:
#     print(f"Testuję: {test=}")
#     moja_liczba = jaka_liczba(test)

#     if moja_liczba:
#         print(f"Wynik: {moja_liczba=}", end="\n\n")
#     else:
#         print("Funkcja zwróciła None")


# # wersja z podnoszeniem wyjątku
# def jaka_liczba(liczba):
#     # sprawdzamy czy w ogóle mamy do czyniena z liczbą
#     if not isinstance(liczba, (int, float)):
#         print("Zły typ argumentu - musi być int albo float")
#         raise TypeError("To nie jest dobry typ")
#         return None

#     if liczba == 0:
#         raise ValueError("nie można dzielić przez zero")

#     # w tym miejscy mamy liczbę - sprawdzamy jak się ona ma do zera
#     if liczba < 0:
#         wynik = "-1"
#     elif liczba > 0:
#         wynik = "+1"
#     else:
#         wynik = "0"

#     return wynik


# testowe_wartosci = [-5, 5.5, 0, "ala ma kota"]
# for test in testowe_wartosci:
#     print(f"Testuję: {test=}")
#     try:
#         moja_liczba = jaka_liczba(test)
#     # except Exception as e:
#     #     print(e)
#     #     continue
#     except ValueError as e:
#         print("obsługa wyjątku ValueError")
#         print(e)
#         continue
#     except TypeError as e:
#         print("obsługa wyjątku TypeError")
#         print(e)
#         continue
#     except Exception as e:
#         print("obsługa pozostałych wyjątków")
#         print(e)
#         continue

#     if moja_liczba:
#         print(f"Wynik: {moja_liczba=}", end="\n\n")
#     else:
#         print("Funkcja zwróciła None")

# print("Koniec programu")


# argumenty domyślne

# def pozdrow(imie="ktoś", miasto="nikąd"):
#     return f"Pozdrawiam {imie} z {miasto}"


# ciag = pozdrow("Ania", "Grudziądz")
# print(ciag)


# ciag = pozdrow("Kasia")
# print(ciag)


# ciag = pozdrow(miasto="Rzeszów")
# print(ciag)


# ciag = pozdrow()
# print(ciag)

# ZADANIE

"""
Napisz funkcję która zwróci pod postacią listy list zawartość pliku, którego nazwę przekażemy przez pierwszy argument funkcji.
Plik ma być otwarty z kodowaniem podanym jako drugi argument funkcji. Jeśli kodowanie nie zostanie podane ma przyjąć utf-8.
Wyświetl wynik zwrócony przez funkcję.
"""


# wersja rozbudowana
# def czytaj_plik(nazwa_pliku, kodowanie = "utf-8"):

#     with open(nazwa_pliku, "r", encoding=kodowanie) as fp:
#         dane = fp.readlines()

#     dane = set(dane)
#     zawodnicy = []
#     for wiersz in dane:
#         zawodnicy.append( wiersz.strip().split(";"))

#     return zawodnicy

# dane_z_pliku = czytaj_plik("zawodnicy.csv")
# print(dane_z_pliku)


# wersja pythonic-style
# def czytaj_plik(nazwa_pliku, kodowanie="utf-8"):

#     with open(nazwa_pliku, "r", encoding=kodowanie) as fp:
#         dane = fp.readlines()

#     return [wiersz.strip().split(";") for wiersz in set(dane)]

# dane_z_pliku = czytaj_plik("zawodnicy.csv")
# print(dane_z_pliku)

# ZADANIE
"""
Przerób rozwiązanie poprzedniego ćwiczenia w taki sposób, by rozdzielacz tez był podany przez argument funkcji,
a w przypadku jego niepodania przyjmował ";".
Zwracana ma być lista krotek.
"""


# def czytaj_plik(nazwa_pliku, kodowanie="utf-8", separator=";"):

#     with open(nazwa_pliku, "r", encoding=kodowanie) as fp:
#         dane = fp.readlines()

#     return [tuple(wiersz.strip().split(separator)) for wiersz in set(dane)]


# dane_z_pliku = czytaj_plik("zawodnicy.csv")
# print(dane_z_pliku)

# argumenty args i kwargs
# def funkcja(a, b, *args):
#     print(f"{a=}")
#     print(f"{b=}")
#     print(f"{args=}")
#     for i,arg in enumerate(args):
#         print(f"args[{i}] = {arg}")

# funkcja(1, 10, 50, "ala", 100, "ma", 1000, "kota")


# def funkcja(*args):
#     print(f"{args=}")
#     for i,arg in enumerate(args):
#         print(f"args[{i}] = {arg}")

# funkcja(1, 10, 50, "ala", 100, "ma", 1000, "kota")


# argumenty klucz wartość
# def funkcja(**kwargs):
#     print(f"{kwargs=}")

# funkcja(liczba1=1, dziesiatka=10, liczba2=50, imie="ala")

# def zapis_czlowieka_do_bazy(imie, nazwisko, **kwargs):
#     print(f"{kwargs=}")

#     print(f"{imie} {nazwisko}")
#     print(f"Numer telefonu: {kwargs.get('nr_tel')}")
#     print(f"Wiek: {kwargs.get('wiek')}")
#     print(f"Miasto: {kwargs.get('miasto')}")


# # zapis_czlowieka_do_bazy("Jan", "Kowalski", "Warszawa")
# # zapis_czlowieka_do_bazy("Jan", "Kowalski", miasto="Warszawa")
# zapis_czlowieka_do_bazy("Jan", "Kowalski", miasto="Warszawa", data_urodzenia="2024-12-12")


# Faker
# instalowanie pakietów:
# pip install nazwa-pakietu
# np: pip install faker

# repozytorium z pakietami - https://pypi.org/


# import faker

# f = faker.Faker()


# from faker import Faker

# f = Faker("pl")

# print(f.street_name())

# print(f.address())


# ZADANIE
"""
Korzystając z pakietu Faker wygeneruj 10 000 anonimowych osób. Każda osoba ma mieć: imię (first_name()), nazwisko (last_name()), nazwę firmy (company()),
email (email()),  numer telefonu (phone_number()) i miejsce zamieszkania (city()).
Zapisz te osoby do pliku CSV, gdzie kolumny rozdzielone są ";"
"""
