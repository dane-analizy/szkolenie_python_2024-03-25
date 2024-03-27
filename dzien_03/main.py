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


# ZADADANIE
"""
Napisz funkcję, która zwraca wartości:
     - -1 jeśli podana w parametrze liczba jest ujemna
     - +1 jesli liczba jest dodatnia
     - 0 jeśli liczba z parametru jest zerem 
Wynik, który zwróci funkcja wypisz na ekranie
"""