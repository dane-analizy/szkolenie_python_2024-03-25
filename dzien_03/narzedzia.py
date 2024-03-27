def czytaj_plik_do_listy_tupli(nazwa_pliku, kodowanie="utf-8", separator=";"):
    with open(nazwa_pliku, "r", encoding=kodowanie) as fp:
        dane = fp.readlines()
    return [tuple(wiersz.strip().split(separator)) for wiersz in dane]


def czytaj_plik_do_slownika(nazwa_pliku, kodowanie="utf-8", separator=";"):
    dane_z_pliku = czytaj_plik_do_listy_tupli(nazwa_pliku, kodowanie, separator)
    lista_wyjsciowa = [
        {
            "imie": osoba[0],
            "nazwisko": osoba[1],
            "wzrost": float(osoba[2]),
            "waga": float(osoba[3])
        }
        for osoba in dane_z_pliku
    ]
    return lista_wyjsciowa


def policz_bmi(masa, wzrost):
    wzrost_m = wzrost/100
    try:
        bmi = masa / (wzrost_m**2)
    except Exception as e:
        print(e)
        return -1
    return round(bmi, 2)
