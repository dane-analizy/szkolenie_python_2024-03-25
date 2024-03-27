def __czytaj_plik_do_listy_tupli(nazwa_pliku, kodowanie="utf-8", separator=";"):
    with open(nazwa_pliku, "r", encoding=kodowanie) as fp:
        dane = fp.readlines()
    return [tuple(wiersz.strip().split(separator)) for wiersz in dane]


def czytaj_plik_do_slownika(nazwa_pliku, kodowanie="utf-8", separator=";"):
    dane_z_pliku = __czytaj_plik_do_listy_tupli(nazwa_pliku, kodowanie, separator)
    lista_wyjsciowa = [
        {
            "imie": osoba[0],
            "nazwisko": osoba[1],
            "wzrost": float(osoba[2]),
            "waga": float(osoba[3]),
        }
        for osoba in dane_z_pliku
    ]
    return lista_wyjsciowa
