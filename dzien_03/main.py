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
d = { (i, i+1) ....  for i, liczba in enumerate(range(20)) }