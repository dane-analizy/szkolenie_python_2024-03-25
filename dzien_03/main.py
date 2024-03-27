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
Napisz funkcję która na konsoli wypisze "Pozdrawiam IMIE", gdzie imie będzie podanym przez użytkownia ciągiem znaków (w ramach input).
Niech program zapyta o imię 2 razy i wywoła 2 razy przygotowaną funkcję.
"""