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
lista = [1, 2, 3, 3.14, 2.78, 21.37, "abc", "def"]
print(lista)
print(type(lista))

# wyswietlenie typów kolejnych elementów na liście
for element in lista:
    print(element, type(element))
