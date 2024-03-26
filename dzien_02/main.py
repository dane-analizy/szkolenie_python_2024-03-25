# przeszukiwanie w pliku - komenda grep

nazwa_pliku = "pan-tadeusz.txt"
szukane_slowo = "szlachta"

for numer_linii, linia in enumerate(open(nazwa_pliku, "r", encoding="utf-8"), start=1):
    if szukane_slowo.lower() in linia.lower():
        print(f"{numer_linii:>6}: {linia.strip()}")


# print("=" * 80)

# # ZADANIE

# """
# Napisz program który będzie pobierał nazwę pliku z kodem w Pythonie.
# Program będzie wyświetlał wszystkie linie które **nie** są komentarzami i nie są puste, razem z numerem linii
# """

napis = "Ala ma kota"
print(napis[0])
