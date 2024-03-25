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


a = input("Podaj liczbę A: ")
if a.isnumeric():
    a = float(a)
else:
    print("A musi być liczbą. Kończę program")
    exit()
    
b = input("Podaj liczbę B: ")
if b.isnumeric():
    b = float(b)
else:
    print("B musi być liczbą. Kończę program")
    exit()

wynik_dodawania = a + b
wynik_odejmowania = a - b
wynik_mnozenia = a * b

print(f"""
Wynik dodawania liczby {a} oraz {b}: {wynik_dodawania}
Wynik obejmowania liczby {a=} oraz {b=}: {wynik_odejmowania}
Wynik mnożenia liczby {a=} oraz {b=}: {wynik_mnozenia}
""")