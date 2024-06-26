# przeszukiwanie w pliku - komenda grep

# nazwa_pliku = "pan-tadeusz.txt"
# szukane_slowo = "szlachta"

# for numer_linii, linia in enumerate(open(nazwa_pliku, "r", encoding="utf-8"), start=1):
#     if szukane_slowo.lower() in linia.lower():
#         print(f"{numer_linii:>6}: {linia.strip()}")


# print("=" * 80)

# # # ZADANIE

# # """
# # Napisz program który będzie pobierał nazwę pliku z kodem w Pythonie.
# # Program będzie wyświetlał wszystkie linie które **nie** są komentarzami i nie są puste, razem z numerem linii
# # """

# # napis = "Ala ma kota"
# # print(napis[0])


# nazwa_pliku = input("Podaj nazwę pliku pythona: ")
# for linia in open(nazwa_pliku, "r", encoding="utf-8"):
#     if len(linia.strip()) > 0 and linia[0] != '#':
#         print(linia.rstrip())

# print(type([1,2]))


# zdefiniowanie listy
# lista = [1, 2, 3, 3.14, 2.78, 21.37, "abc", "def"]
# print(lista)
# print(type(lista))

# # wyswietlenie typów kolejnych elementów na liście
# for element in lista:
#     print(element, type(element))

# lista = [1, 2, 3, 3.14, 2.78, 21.37, "abc", "def"]

# for licznik, element in enumerate(lista):
#     print(licznik, element, type(element))
#     print(f"Pokazuję {licznik} element z listy, który ma wartość: {element:>10} | {type(element)} |")


# from datetime import datetime

# now = datetime.now()
# print(f"{now:%Y-%m-%d-%H}")

# lista = [1, 2, 3, 3.14, 2.78, 21.37, "abc", "def"]
# print(lista[1])  # oczekujemy wartości 2
# print(lista[0:4])  # oczekujemy wartości [1, 2, 3, 3.14]

# print(lista[:4]) # od początku do 4
# print(lista[4:]) # od 4 do końca

# print(lista[2:6:2]) # od 2 do 6 co drugi

# # range(start, stop, krok)
# print(lista[6:4])
# print(lista[6:4:-1]) # od 6 do 4 idąc od tyłu

# print(lista[::-1]) # wszystkie w odwrotnej kolejności

# print(lista[::-2]) # co drugi od końca

# lista = []
# print(range(50), type(range(50)))

# lista = list(range(50))
# print(lista, type(lista))

# wstawianie do listy
# lista = []
# lista.append(1)
# lista.append(2)
# lista.append(3)
# lista.append(4)
# lista.insert(2, "wstawione w index 2")  # pod indeksem 2
# print(lista)
# lista.insert(0, "wstawione w pierszej pozycji")  # pierwszy
# print(lista)
# lista.insert(-1, "wstawione przedostatnie")  # przedostatni
# print(lista)

# lista = list(range(100))
# lista.insert(-10, "abc") # 10 od końca
# print(lista)


# ZADANIE

"""
Napisz kod który umieści w liście 10 kolejnych potęg liczby 2.
Następnie przeiteruj po tej liście i każdy z jej elementów wyświetl na konsoli w osobnej linii.
"""


# lista = []

# n = 2

# i = 0
# while i < 10:
#     lista.append(n**i)
#     i = i + 1

# for potega in range(10):
#     lista.append(n**potega)


# for i in range(len(lista)):
#     print(f"{lista[i]}")

# for i, element in enumerate(lista):
#     print(f"{lista[i]}")

# for el in lista:
#     print(el)


# list = []
# element = 2
# for i in range(10):
#     list.append(element**i)

# print(list)
# print(list(range(10)))

# for n in list:
#     print(n)


# lista = [1, 2, 3, 3.14, 2.78, 21.37, "abc", 3, "def"]
# print(lista)

# lista.clear()
# print(lista)

# for el in lista:
#     print("jestem w pętli")

# print("jestem poza pętli")

# # usunięcie z listy pierwszej wartości 3
# lista.remove(3)
# print(lista)

# # usunięcie elementu o indeksie 3
# lista.pop(3)
# print(lista)


# l1 = [1, 2, 3, 4, 5]
# # l2 = l1.copy()
# # print(l1, l2)
# l2 = l1.copy()

# print(l1, l2)
# l1[1] = "abs"

# print(l1, l2)


# sortowanie
# l1 = [3, 1, 2, 5, 4]
# l1_s1 = sorted(l1)
# print(l1, l1_s1)

# l1.sort()
# print(l1)

# l1 = [3, 1, 2, 5, 4, "abc", "xyz"]
# l1_s1 = sorted(l1, reverse=True)
# print(l1, l1_s1)

# l1.sort()
# print(l1)

# # importowawanie całego modułu
# import random
# random.randint()

# # importowanie jednej funkcji z pakietu
# from random import randint
# randint()


# import random

# print(random.randint(1, 100))


# ZADANIE

"""
Wygeneruj listę 10 losowych liczb z zakresu 1-100.
Posortuj je w kolejności malejącej, a następnie wyświetl każdą liczbę w oddzielnej linii.
"""

# import random

# lista = []
# for i in range(10):
#     liczba_losowa = random.randint(1, 100)
#     lista.append(liczba_losowa)

# lista.sort(reverse=True)

# for el in lista:
#     print(el)

# import random

# lista = []
# for _ in range(10):
#     lista.append(random.randint(1, 100))

# for el in sorted(lista, reverse=True):
#     print(el)


# import random

# lista = []
# for _ in range(10):
#     lista.append(random.randint(1, 100))

# for el in sorted(lista, reverse=True):
#     print(el)


# list comprehention / listy składane
# import random

# # lista = [random.randint(1, 100) for _ in range(10)]
# lista = [i for i in range(10)]

# for el in sorted(lista, reverse=True):
#      print(el)


# ZADANIE

"""
Korzystając z list składanych wygeneruj listę 10 kolejnych potęg dwójki.
Wyświetl tę listę. Spróbuj zrobić to w jak najkrótszym zapisie.
"""

# lista = [2**potega for potega in range(10)]
# print(lista)


# liczby_parzyste = []
# liczby_nieparzyste = []
# for liczba in range(50):
#     if liczba % 2:
#         liczby_nieparzyste.append(liczba)
#     else:
#         liczby_parzyste.append(liczba)


# print(liczby_parzyste)
# print(liczby_nieparzyste)

# liczby_parzyste = [liczba for liczba in range(50) if not liczba % 2]
# liczby_nieparzyste = [liczba for liczba in range(50) if liczba % 2]
# print(liczby_parzyste)
# print(liczby_nieparzyste)


# a = 130
# b = "parzysta" if a % 2 == 0 else "nieparzysta"
# print(a, b)

# if a % 2 == 0:
#     b = "parzysta"
# else:
#     b = "nieparzysta"


# ZADANIE

"""
Wygeneruj dwie listy liczb losowych - losowe parzyste i losowe nieparzyste.
Użyj list składanych, wyświetl obie listy w posortowanej kolejności, od najmniejszej do największej.
"""


# import random

# liczby_parzyste = [i if random.randint(1, 100) % 2 == 0  else "pass" for i in range(50)]
# liczby_nieparzyste = [i if random.randint(1, 100) % 2 else "pass" for i in range(50)]

# print(liczby_parzyste)
# print(liczby_nieparzyste)


# import random

# liczby_parzyste = [i for i in range(50) if not i % 2]
# liczby_nieparzyste = [i for i in range(50) if i % 2]

# print(liczby_parzyste)
# print(liczby_nieparzyste)


# lista_pelna = liczby_nieparzyste + liczby_parzyste

# lista_pelna = liczby_nieparzyste.copy()
# lista_pelna.extend(liczby_parzyste)

# print(lista_pelna)


# linia_csv_kowalski = "Jan;Kowalski;185;67"
# linia_csv_nowak = "Zenon;Nowak;175;78"

# linia_rozdzielona = [linia_csv_kowalski, linia_csv_nowak]

# print(linia_rozdzielona[1])

# kowalski = linia_csv_kowalski.split(";")
# print(kowalski)

# print(",".join(kowalski))


# linia_csv_kowalski = "Jan;Kowalski;185;67"
# linia_csv_nowak = "Zenon;Nowak;175;78"

# linia_rozdzielona = [linia_csv_kowalski.split(";"),
#                      linia_csv_nowak.split(";")]

# print(linia_rozdzielona)


# ZADANIE
# Załaduj do postaci listy list zawartość pliku zawodnicy.csv

# lista_zawodnikow = []
# for linia in open("zawodnicy.csv", "r", encoding="utf-8"):
#     linia_oczyszczona = linia.strip()
#     linia_rozdzielona = linia_oczyszczona.split(";")
#     lista_zawodnikow.append(linia_rozdzielona)

# print(lista_zawodnikow)


# optymalizacja 1
# lista_zawodnikow = []
# for linia in open("zawodnicy.csv", "r", encoding="utf-8"):
#     linia_rozdzielona = linia.strip().split(";")
#     lista_zawodnikow.append(linia_rozdzielona)

# print(lista_zawodnikow)


# optymalizacja 2
# lista_zawodnikow = []
# for linia in open("zawodnicy.csv", "r", encoding="utf-8"):
#     lista_zawodnikow.append(linia.strip().split(";"))

# print(lista_zawodnikow)


# optymalizacja 3 - list comprehention
# lista_zawodnikow = [
#     linia.strip().split(";") for linia in open("zawodnicy.csv", "r", encoding="utf-8")
# ]

# print(lista_zawodnikow)


# ZADANIE

# Dla każdego wpisu w pliku zawodnicy.csv wyświetl na konsoli informację o imieniu, nazwisku, wadze i wzroście oraz BMI.
# BMI = kg / m2


# pierwsza wersja - ELT
# lista_zawodnikow = [
#      linia.strip().split(";") for linia in open("zawodnicy.csv", "r", encoding="utf-8")
# ]
# # ['Zenon', 'Nowak', '175', '78']

# for osoba in lista_zawodnikow:
#     wzrost = float(osoba[2])/100
#     waga = float(osoba[3])
#     bmi = waga / wzrost**2
#     print(f"{osoba[0]} {osoba[1]} przy wzroście {wzrost*100:.1f} cm i wadze {waga:.1f} kg ma BMI = {bmi:.2f}")


# druga wersja - ETL
# ['Zenon', 'Nowak', '175', '78']
# lista_zawodnikow = []
# for linia in open("zawodnicy.csv", "r", encoding="utf-8"):
#     osoba = linia.strip().split(";")
#     imie, nazwisko = osoba[0], osoba[1]
#     wzrost = float(osoba[2]) / 100
#     waga = float(osoba[3])
#     bmi = waga / wzrost**2

#     lista_zawodnikow.append( [imie, nazwisko, wzrost, waga, bmi])

# # print(lista_zawodnikow)

# for osoba in lista_zawodnikow:
#     print(f"{osoba[0]} {osoba[1]} przy wzroście {osoba[2]*100:.1f} cm i wadze {osoba[3]:.1f} kg ma BMI = {osoba[4]:.2f}")


# krotka = ("Zenon", "Nowak", "175", "78")
# # print(krotka)
# # # krotka.append(15)
# # print(sorted(krotka))

# lista_z_krotki = list(krotka)
# print(lista_z_krotki)

# lista = [1,2,3, "abc", "zxy"]
# krotka_z_listy = tuple(lista)
# print(krotka_z_listy)

# k1 = tuple( [i for i in range(10)] )
# print(k1)

# k2 = tuple([i for i in range(10, 20)])
# print(k2)

# print(k2 + k1)

# ZADANIE

"""
Stwórz dwie krotki. Jedna ma zawierać 10 losowych liczb zakresu 1-10, druga 10 losowych liczb zakresu 11-20.
Stwórz trzecią krotkę która ma zawierać dane z obu krotek. Trzecią krotkę wypisz na konsoli.
"""

# import random

# krotka_1_10 = tuple([random.randint(1, 10) for _ in range(10)])
# krotka_11_20 = tuple([random.randint(11, 20) for _ in range(10)])
# krotka_1_20 = krotka_1_10 + krotka_11_20
# print(krotka_1_20)


# lista = [1, 3, 2, 1, 2, 1, 2, 3]
# print(lista)
# print(set(lista))

# print("-" * 80)
# krotka = (1, 2, 1, 2, 1, 2, 3)
# print(krotka)
# print(set(krotka))


# ZADANIE

# Wygeneruj zestaw niepowtarzalnych liczb przy 100-krotnym losowaniu liczby z zakresu 1-50


# import random

# liczby = [random.randint(1, 50) for _ in range(100)]

# print(set(liczby))

# lista = [1,2,4,3,5,1,3,2,1,1]
# lista = list(set(lista))

# z1 = set([1, 2, 3, 4, 5])
# z2 = {i for i in range(3, 10)}
# z1.add(6)
# print(z1, z2)

# print(z1.intersection(z2))  # część wspólna
# print(z1.union(z2))  # suma zbiorów

# print(z1.difference(z2))  # różnica zbiorów z1 i z2
# print(z2.difference(z1))  # różnica zbiorów z2 i z1

# print(z1.difference(z2).union(z2.difference(z1)))


# ZADANIE
# Wypisz na ekranie listę unikalnych zawodników z zawodnicy.csv. Każda z osób ma być elementem typu tuple/krotka.


# lista_zawodnikow = []
# for linia in open("zawodnicy.csv", "r", encoding="utf-8"):
#     osoba = linia.strip().split(";")
#     imie, nazwisko = osoba[0], osoba[1]
#     wzrost = float(osoba[2]) / 100
#     waga = float(osoba[3])
#     bmi = waga / wzrost**2

#     lista_zawodnikow.append( [imie, nazwisko, wzrost, waga, bmi])

# # to nie zadziała:
# set(lista_zawodnikow)

# to zadziała:
# lista_zawodnikow = [linia.strip() for linia in open("zawodnicy.csv", "r", encoding="utf-8")]
# print(len(lista_zawodnikow))

# lista_zawodnikow = set(lista_zawodnikow)
# print(len(lista_zawodnikow))
# print(lista_zawodnikow)

# for wiersz in lista_zawodnikow:
#     osoba = wiersz.split(";")
#     wzrost = float(osoba[2])/100
#     waga = float(osoba[3])
#     bmi = waga / wzrost**2
#     print(f"{osoba[0]} {osoba[1]} przy wzroście {wzrost*100:.1f} cm i wadze {waga:.1f} kg ma BMI = {bmi:.2f}")


# sortowanie listy list

# lista_zawodnikow = []
# for linia in open("zawodnicy.csv", "r", encoding="utf-8"):
#     osoba = linia.strip().split(";")
#     imie, nazwisko = osoba[0], osoba[1]
#     wzrost = float(osoba[2]) / 100
#     waga = float(osoba[3])
#     bmi = waga / wzrost**2

#     if bmi <= 16:
#         bmi_comment = "wygłodzenie"
#     elif bmi <= 17:
#         bmi_comment = "wychudzenie"
#     elif bmi <= 18.5:
#         bmi_comment = "niedowaga"
#     elif bmi <= 25:
#         bmi_comment = "pożądana masa ciała"
#     elif bmi <= 30:
#         bmi_comment = "nadwaga"
#     elif bmi <= 35:
#         bmi_comment = "otyłość I stopnia"
#     elif bmi <= 40:
#         bmi_comment = "otyłość II stopnia (duża)"
#     else:
#         bmi_comment = "otyłość III stopnia (chorobliwa)"

#     lista_zawodnikow.append([imie, nazwisko, wzrost, waga, bmi, bmi_comment])

# for el in sorted(lista_zawodnikow, key=lambda l: l[4], reverse=True):
#     print(el)


# zapisanie listy stringów do pliku
# lista = ["Zenon;Nowak", "Jan;Kowalski", "Andrzej;Gołota", "Julia;Wieniawa"]
# fp = open("plik.txt", "w", encoding="utf-8")
# fp.write("napis\n")
# fp.writelines([f"{el}\n" for el in lista])
# fp.close()


# ZADANIE

# Przepisz tylko unikalne osoby z pliku zawodnicy.csv do nowego pliku - zawodnicy_unikalni.csv
# Jeśli chcesz to posortuj po pierwszej literze imienia dane w pliku wynikowym.

# # wczytujemy plik do listy stringów
# with open("zawodnicy.csv", "r", encoding="utf-8") as fp:
#     lista_zawodnikow = fp.readlines()

# # unikalne i posortowane
# lista_zawodnikow = set(lista_zawodnikow)
# lista_zawodnikow = sorted(lista_zawodnikow)

# # zapisujemy
# with open("zawodnicy_unikalni.csv", "w", encoding="utf-8") as fp:
#     fp.writelines(lista_zawodnikow)


# ZADANIE

"""
Dane z pliku zawodnicy.csv wzbogacone o wyliczony wskaźnik BMI zapisz do pliku zawodnicy_bmi.csv.
Wynikowo mają pozostać unikalni zawodnicy.
"""

# wczytanie wierszy
# with open("zawodnicy.csv", "r", encoding="utf-8") as fp:
#     lista_zawodnikow = fp.readlines()

# # unikalne
# lista_zawodnikow = set(lista_zawodnikow)

# # dla wszystkich zawodników na liście:
# lista_osob = []
# for linia in lista_zawodnikow:
#     # czyszczenie danych (rozdzielanie, zamiana na float)
#     osoba = linia.strip().split(";")
#     imie, nazwisko = osoba[0], osoba[1]
#     wzrost = float(osoba[2]) / 100
#     waga = float(osoba[3])

#     # wyliczenie BMI
#     bmi = waga / wzrost**2

#     # do nowej listy dodaj "obiekt" zadwodnika z wyliczonymi rzeczami
#     lista_osob.append([imie, nazwisko, wzrost*100, waga, round(bmi, 2)])

# # sortowanie po 2-elemencie (wzrost)
# lista_osob.sort(key=lambda l:l[2])

# # zapis do pliku
# with open("zawodnicy_bmi.csv", "w", encoding="utf-8") as fp:
#     for osoba in lista_osob:
#         # konieczna zmiana float na str w locie - bo join() nie umie łączyć inaczej
#         osoba_str = ";".join( [str(o) for o in osoba] )

#         # zapis konkretnej linii
#         fp.write(osoba_str+"\n")


# słowniki

# slownik = dict()
# slownik1 = {"klucz": "wartość",
#            "imie": "jan",
#            "nazwisko": "nowak",
#            "wiek": 25}
# slownik2 = {"klucz": "wartość", "imie": "zdzichu", "nazwisko": "kowalski", "wiek": 50}
# print(slownik1)
# print(slownik2)

# slownik = {"klucz": "wartość", "imie": "jan", "nazwisko": "nowak", "wiek": 25,
#            "klucz": "wartość", "imie": "zdzichu", "nazwisko": "kowalski", "wiek": 50}
# print(slownik)


# slownik = {"klucz": "wartość", "imie": "jan", "nazwisko": "nowak", "wiek": 25}
# for po całym słowniku - daje klucze
# for k in slownik:
#     print(k)

# for po kluczach
# for k in slownik.keys():
#     print(k)

# for po wartościach
# for v in slownik.values():
#     print(v)

# iterowanie po 2 listach na raz
# for k,v in zip(slownik.keys(), slownik.values()):
#     print(f"klucz: {k}\nwartość:{v}\n\n")

# iterowanie po kluczach i wartościach słownika na raz
# for k, v in slownik.items():
#     print(f"klucz: {k}\nwartość:{v}\n\n")


# print(slownik['imie'])
# print(slownik["drugie_imie"])

# slownik['drugie_imie'] = "krzysztof"
# if "drugie_imie" in slownik.keys():
#     print(slownik["drugie_imie"])
# else:
#     print("NIE MA TAKIEGO KLUCZA")

# print(slownik)

# print(slownik.get("drugie_imie", "nie ma takiego numeru"))
# licznik_slow = {}

# licznik_slow[nowe_slowo] = licznik_slow.get(nowe_slowo, 0) + 1


# ZADANIE

"""
Policz ile razy występują poszczególne słowa w tekście "Pana Tadeusza".
Użyj słowników - kluczem niech będzie słowo zapisane małymi literami, a wartością - liczba jego wystąpień.
"""

# # wczytać cały plik open().read()
# tekst = open("pan-tadeusz.txt", "r", encoding="utf-8").read()

# # zamienić tekst na małe litery
# # moźe usunąć jakieś dodatkowe znaki - ., \n ? !
# tekst = tekst.lower()

# zle_znaki = '.,?!\n'
# for zz in zle_znaki:
#     tekst = tekst.replace(zz, " ")

# # podzielić tekst na słowa split()
# slowa = tekst.split(" ")

# # zbudować pusty słownik
# licznik_slow = {}

# # przejść słowo po słowie i dodać w słowniku odpowiednią liczbę
# for nowe_slowo in slowa:
#     # czyste_nowe_slowo = lematyzuj(nowe_slowo)
#     if len(nowe_slowo) <=5:
#         continue
#     licznik_slow[nowe_slowo] = licznik_slow.get(nowe_slowo, 0) + 1

# print(licznik_slow.get("tadeusz"))

# # print(licznik_slow)

# posortowany_slownik = sorted(licznik_slow.items(), key=lambda l: l[1])
# print(posortowany_slownik)


# d = {
#     "imie": "jan",
#     "nazwisko": "kowalski",
#     "wiek": 25,
#     "samochody": [
#         {"marka": "Ford", "model": "Focus", "rok_produkcji": 2020},
#         {"marka": "Opel", "model": "Astra", "rok_produkcji": 2018},
#     ],
#     "dlugosc_palcow_lewa_reka": [3, 5, 6, 5, 4],
# }
# print(d)

# # print(d['wiek'])

# print(len(d["dlugosc_palcow_lewa_reka"]))

# d["dlugosc_palcow_lewa_reka"].append("jest ok")

# print(d["dlugosc_palcow_lewa_reka"][-1])


# print(d["samochody"][0]['model'])


# zapis słownika do jsona
# import json
# d = {
#     "imie": "jan",
#     "nazwisko": "kowalski",
#     "wiek": 25,
#     "samochody": [
#         {"marka": "Ford", "model": "Focus", "rok_produkcji": 2020},
#         {"marka": "Opel", "model": "Astra", "rok_produkcji": 2018},
#     ],
#     "dlugosc_palcow_lewa_reka": [3, 5, 6, 5, 4],
# }
# with open("pan_jan.json", "w", encoding="utf-8") as fp:
#     json.dump(d, fp)


# odzczyt jsonwa do słownika 
import json

with open("pan_jan.json", "r", encoding="utf-8") as fp:
    d = json.load(fp)

print(d)
