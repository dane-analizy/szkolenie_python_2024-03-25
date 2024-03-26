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


linia_csv_kowalski = "Jan;Kowalski;185;67"
linia_csv_nowak = "Zenon;Nowak;175;78"

linia_rozdzielona = [linia_csv_kowalski, linia_csv_nowak]

print(linia_rozdzielona[1])

kowalski = linia_csv_kowalski.split(";")
print(kowalski)

print(",".join(kowalski))
