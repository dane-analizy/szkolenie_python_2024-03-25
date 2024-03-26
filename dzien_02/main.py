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
