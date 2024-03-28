def tuple_list_to_file(lista_elementow, lista_nazw, nazwa_pliku):
    with open(nazwa_pliku, "w", encoding="utf-8") as f:

        wiersz_naglowek = ";".join([str(e) for e in lista_nazw])
        f.write(wiersz_naglowek + "\n")

        for el in lista_elementow:
            wiersz = ";".join([str(e) for e in el])
            f.write(wiersz + "\n")
