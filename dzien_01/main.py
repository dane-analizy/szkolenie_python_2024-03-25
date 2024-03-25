# print("hello world")
# toJestJakasZmienna - tak nie robimy
# to_jest_jakas_zmienna

# a = 1
# b = a + 4
# print(a + 1, b -1)


# a = "nowe"
# a = "inne"
# print(a + "tekst")

# print("ciapki podwójne", 'ciapki pojedyncze')


# zmienna_int = 10
# zmienna_int_zmiana = zmienna_int / 3
# zmienna_float = 1.234
# zmienna_bool = True
# zmienna_string = "napis"
# print(zmienna_int, zmienna_int_zmiana, zmienna_float, zmienna_bool, zmienna_string)

# to będzie błąd:
# print(zmienna_float + zmienna_string)


# zmienna_int: int = 10
# zmienna_int_zmiana: float
# zmienna_int_zmiana  = zmienna_int / 3
# zmienna_float: float= 1.234
# zmienna_bool: bool = True
# zmienna_string: str = "napis"
# # print(zmienna_int, zmienna_int_zmiana, zmienna_float, zmienna_bool, zmienna_string)

# print("Wypisanie zmiennych z .format():")
# print(
#     "tu będzie int: {}\nzmienna_string: {}\nzmienna_int_zmiana: {}\n".format(
#         zmienna_int, zmienna_int_zmiana, zmienna_string
#     )
# )

# print("Wypisanie zmiennych z f-string:")
# print(f"tu będzie int: {zmienna_int}\nzmienna_string: {zmienna_string}\nzmienna_int_zmiana: {zmienna_int_zmiana}\n")


# zmienna_float: float = 1.23456789
# # # print(f'tekst "egege" ')
# # print(f"{zmienna_float:>50}")
# # print(f"{zmienna_float:.0f}")

# print(f"{zmienna_float*50:.1f}")

# imie = "Łukasz"
# print("Twoje imię to {imie}, życzę Ci miłego dnia!")
# print(imie)
# print("Twoje imię to", imie, ", życzę Ci miłego dnia!")
# print("Twoje imię to "+imie, ", życzę Ci miłego dnia!")
# wynik = f"Twoje imię to {imie}, życzę Ci miłego dnia!"
# print(wynik)


# zmienna = input("podaj jakiś ciąg: ")
# print(zmienna)


# print("""
#       tu będzie int: {zmienna_int}\n
#       zmienna_string: {zmienna_string}
#       zmienna_int_zmiana: {zmienna_int_zmiana}
#       """)


# ZADANIE

"""
Napisz program, który pobierze od użytkownika imię i nazwisko (osobno),
a potem wypisze w konsoli pozdrowienie "Witaj IMIĘ NAZWISKO!"
"""

# imie = input("Podaj imię: ")
# nazwisko = input("A jak masz na nazwisko? ")
# imie_nazwisko = f"{imie} {nazwisko}"
# print(f"Witaj {imie_nazwisko}")


# ZADANIE

"""
Napisz prosty kalkulator - pobiera od użytkownika dwie liczby a i b, a potem wyświetla wyniki działań a+b, a-b, a*b, wypisując np.:

a+b: 3.24 + 5.67 = ...
a-b: 3.24 - 5.67 = ...
a*b: 3.24 * 5.67 = ...

"""


# liczba = -10

# print("Przed sprwadzaniem")

# if liczba > 0:
#     print("liczba większa od zera")
# else:
#     print("nie jest większa od zera")

# print("Po sprwadzaniu")


# a = input("Podaj liczbę A: ")
# if a.isnumeric():
#     a = float(a)
# else:
#     print("A musi być liczbą. Kończę program")
#     exit()

# b = input("Podaj liczbę B: ")
# if b.isnumeric():
#     b = float(b)
# else:
#     print("B musi być liczbą. Kończę program")
#     exit()

# wynik_dodawania = a + b
# wynik_odejmowania = a - b
# wynik_mnozenia = a * b

# print(f"""
# Wynik dodawania liczby {a} oraz {b}: {wynik_dodawania}
# Wynik obejmowania liczby {a=} oraz {b=}: {wynik_odejmowania}
# Wynik mnożenia liczby {a=} oraz {b=}: {wynik_mnozenia}
# """)


# ZADANIE

# Napisz program, który pobierze od użytkownika masę i wzrost, a następnie policzy BMI i wypisze wynik na konsolę.

# BMI = masa / wzrost^2
# masa w kg
# wzrost w m

# wzrost ** 2

# wzrost = input("Podaj swój wzrost w centrymetrach: ")
# if wzrost.isnumeric() and wzrost != "0":
#     wzrost = float(wzrost)
#     wzrost = wzrost / 100
# else:
#     print("Wzrost nie może być ani stringiem ani zerem.")
#     exit()

# waga = input("Podaj swoją wagę w kg: ")
# if waga.isnumeric():
#     waga = float(waga)
# else:
#     print("Podano błędą wartość wagi.")
#     exit()
# BMI = waga / wzrost**2
# print(f"Twoje BMI wynosi: {BMI}")


# masa = input("Podaj masę ciała w kg: ")
# wzrost = input("Podaj zwój wzrost w m: ")

# if masa.isnumeric():
#     masa = float(masa)

# if wzrost.isnumeric():
#     wzrost = float(wzrost)

# BMI = masa / wzrost**2
# print(f"Twoje BMI wynosi: {BMI}")


# obsługa wyjątków

# l = "1.23d4"
# f = None

# try:
#     f = float(l)
# except Exception as e:
#     print("nie udało się")
#     print(e)

# print(f"{l=} => {f=}")


# BMI z obsługą wyjątków

# masa = input("Podaj masę ciała w kg: ")
# wzrost = input("Podaj zwój wzrost w m: ")

# try:
#     masa = float(masa)
# except:
#     print("nie udało się masy zrzutować na float")
#     exit()


# try:
#     wzrost = float(wzrost)
# except:
#     print("nie udało się wzrostu zrzutować na float")
#     exit()


# BMI = masa / wzrost**2
# print(f"Twoje BMI wynosi: {BMI}")


# l = 120

# if l < 0:
#     print("ujemna")
# elif l > 100:
#     print("więcej niż 100")
# elif l > 50:
#     print("więcej niż 50")

# l = 25
# if 100 < l < 500:
#     print("wersja 1 pomiędzy 100 a 500")

# if l > 100 and l < 500:
#     print("wersja 2 pomiędzy 100 a 500")

# if l < 100 or l > 1000:
#     print("poniżej 100 albo ponad 1000")


# pętla 10 kroków
# for i in range(10):
#     print(f"{i=}")


# ZADANIE

# Wyświetl 20 kolejnych potęg liczby 2.

# i = 2
# for n in range(20):
#     print(f"{i} do potęgi {n} = {i**n}")

# for i in range(20):
#     j = float(i)
#     j = j**2
#     print(f"{j=}")

# # 20 elementów - od 0 do 19
# for i in range(20):
#     print(f"{i=}")

# # 10 elementów - od 10 do 19
# for i in range(10, 20):
#     print(f"{i=}")

# # 5 elementów - od 10 do 19, co 2
# for i in range(10, 20, 2):
#     print(f"{i=}")

# reszta z dzielenia i część całkowita
# i = 5
# print(i % 2) # reszta
# print(i // 2) # część całkowita

# for i in range(2, 21, 2):
#     print(i)

# for i in range(21):
#     if i % 2 != 0:
#         print(i)


# ZADANIE
# Wydrukuj liczby od 1 do 100 razem z informacją czy liczba jest parzysta czy nieparzysta.

# for i in range(100):
#     if (i + 1) % 2 == 0:
#         print(f"{i+1} - jest parzysta")
#     if (i + 1) % 2 != 0:
#         print(f"{i+1} - nie jest parzysta")


# for i in range(1, 101):
#     if i % 2 == 0:
#         print(f"{i} - jest parzysta")
#     else:
#         print(f"{i} - nie jest parzysta")


# for i in range(1, 101):
#     if i % 2 == 0:
#         print(f"{i} jest liczbą parzystą")
#     else:
#         print(f"{i} jest liczbą nieparzystą")
# else:
#     print("Ja wykonam się zawsze")


# idż do kolejnego kroku
# for i in range(-10, 10):
#     print(i)
#     if i == 0:
#         continue
#     print(1 / i)

# przerwij pętlę
# for i in range(-10, 10):
#     print(i)
#     if i == 0:
#         break
#     print(1 / i)

# for...else
# for i in range(-10, 10):
#     print(i)
#     if i == 0:
#         continue # porównaj z break
#     print(1 / i)
# else:
#     print("jestem else do for")

# i = 0
# while i < 10:
#     print(i)
#     i = i + 1

# i = 1
# while True:
#     i += 1
#     if i % 2 == 0:
#         print(i)
#     if i > 1000:
#         break


# ZADANIE

"""
Napisz symulator lokaty Symulator ma przyjmować zmienne:
- kwotę lokaty
- oprocentowanie w skali roku
- ilość miesięcy na jaką zakładamy lokatę
Symulator ma dla każdego miesiąca lokaty wypisać który to miesiąc oraz ile mamy aktualnie zgromadzone po doliczeniu odsetek. 
Zakładamy kapitalizację odsetek co miesiąc
"""

# ilosc_miesiecy = 12
# oprocentowanie = 5 # wartość w procentach w skali roku
# kwota = 100_123

# oprocentowanie = oprocentowanie / 100 / 12 # przeliczenie na % odsetek w skali miesiąca

# print("wersja FOR:")

# for i in range(ilosc_miesiecy):
#     kwota = kwota + (kwota * oprocentowanie)
#     print(f"Po miesiacu {i+1} otrzymasz kwote rowna: {kwota}")


# print("wersja WHILE:")
# kwota = 100_123
# i = 0
# while i < ilosc_miesiecy:
#     i = i + 1
#     kwota = kwota + (kwota * oprocentowanie)
#     print(f"W {i} miesiącu, kwota lokaty wynosi: {kwota}")


# ZADANIE

"""
Napisz pętlę while która będzie wyświetlała kolejne potęgi liczby 2 aż wartość potęgi (wynik potęgowania)
nie przekroczy wartości podanej przez użytkownika
"""

# wartosc_przekroczenia = 100_000
# potega = 0
# wynik = 2**potega
# while wynik < wartosc_przekroczenia:
#     print(f"2^{potega} = {wynik}")
#     potega += 1
#     wynik = 2**potega


# napis = "Ala ma kota"
# i = 0
# for litera_w_napisie in napis:
#     print(i, litera_w_napisie)
#     i = i + 1

# # pythonowe rozwiązanie tego co wyżej
# napis = "Ala ma kota"
# for i, litera in enumerate(napis):
#     print(i, litera)

# for numer, i in enumerate(range(10)):
#     print(numer, i)

# print(list(range(100)))

# długość tekstu
# s = "Ala ma kota"
# l = 100
# print(len(s))
# print(len(range(10)))

# zmiana wielkości liter
# s = "ala MA kota. a Kot\nma\nPsa"
# print(s.upper(), end="\n====\n")
# print(s.lower(), end="\n====\n")
# print(s.capitalize(), "guowhgouwr", end="\n====\n")
# print(s.title(), end="\n====\n")


# oczyszczanie pustych znaków
# s = "   ala MA kota. a Kot ma Psa   hugy\n\n"
# print(f"|{s}|")
# print(f"|{s.strip()}|")
# print(f"|{s.lstrip()}|")
# print(f"|{s.rstrip()}|")

# zamiana znaków
# s = "Ala ma kota. Pies ma kość. Tomek ma piłkę."
# print(s)
# print(s.replace(".", "="))
# print(s.replace(".", ""))


# ZADANIE

"""
Napisz program, który przyjmie od użytkownika ciąg tekstowy, następnie usunie z niego znaki: ,.?!
a następnie powiększony do dużych liter wyświetli w konsoli.
"""

# sposób pierwszy
# t = input("Podaj Tekst:")
# t = t.replace(" ", "")
# t = t.replace(",", "")
# t = t.replace(".", "")
# t = t.replace("?", "")
# t = t.replace("!", "")
# print(t.upper())


# sposób drugi
# t = input("Podaj Tekst:")
# zle_znaki = ' .,?!#$%&*!@%&()'

# for zly_znak in zle_znaki:
#     t = t.replace(zly_znak, "")

# print(t.upper())


# sposób trzeci
# tekst_wejsciowy = input("Podaj Tekst:")
# zle_znaki = " .,?!"

# tekst_wyjsciowy = ""
# for litera in tekst_wejsciowy:
#     if litera in zle_znaki:
#         continue
#     tekst_wyjsciowy = tekst_wyjsciowy + litera

# print(tekst_wyjsciowy.upper())

# zliczenie wystąpień tekstu w tekście
# s = "Ala ma kota. Pies ma kość. Tomek ma piłkę. Ale Ala nie lubi w nią grać. Taka to nasza Ala"
# print(s.count("a"))
# print(s.lower().count("a"))
# print(s.lower().count("ala "))

# czy ciąg występuje w innym ciągu
# s = "Ala ma kota. Pies ma kość. Tomek ma piłkę. Ale Ala nie lubi w nią grać. Taka to nasza Ala"
# # if "ala" in s.lower():
# if "ala" in s:
#     print("Ala obecna")
# else:
#     print("Ala wyszła")

# wczytanie całego pliki na raz
# file = open("dlugosc_linii.txt", "r", encoding='utf-8')
# file_content = file.read()
# file.close()
# print(file_content)

# print("=+" * 60)

# czytanie linia po linii
# for linia in open("dlugosc_linii.txt", "r", encoding="utf-8"):
#     print(linia.strip(), end="|")


# ZADANIE

# Napisz program który wyświetli na konsoli niepuste linie z pliku tekstowego, którego nazwę poda użytkownik

# nazwa_pliku = input("Podaj nazwę pliku: ")
# nazwa_pliku = "dlugosc_linii.txt"

# for linia in open(nazwa_pliku, "r", encoding="utf-8"):
#     if not len(linia.strip()):
#         continue
#     print(linia.strip())


# nazwa_pliku = "dlugosc_linii.txt"

# for linia in open(nazwa_pliku, "r", encoding="utf-8"):
#     if len(linia.strip()) != 0:
#         print(linia.strip())


# if ...:
#     if egwgw:
#         if egege:
#             zrbo
#         else:
#            zbwgwg
#     else:
#         ijgiwg
# else:
#     rngiwgj


# if not ...
#     continue


# przeszukiwanie w pliku - komenda grep

nazwa_pliku = "pan-tadeusz.txt"
szukane_slowo = "szlachta"

for numer_linii, linia in enumerate(open(nazwa_pliku, "r", encoding="utf-8"), start=1):
    if szukane_slowo.lower() in linia.lower():
        print(f"{numer_linii:>6}: {linia.strip()}")
