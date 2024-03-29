from flask import Flask, render_template, request

app = Flask(__name__)  # nazwa będzie wzięta z nazwy pliku pythona


# @app.route("/zmienna")
# def main():
#     return render_template("zmienna_z_kodu.html", abc="inna wartosc", xyz=12.34)


# @app.route("/slownik")
# def main_dict():
#     d = {"klucz1": "napis", "klucz2": 123, "klucz3": "jestem kluczem 3"}
#     return render_template("slownik_z_kodu.html", abc=d)


# @app.route("/lista")
# def main_lista():
#     d = ("klucz1", "napis", "klucz2", 123, "klucz3", "jestem kluczem 3")
#     return render_template("lista_z_kodu.html", lista=d)


# parametry z ? - przykładowe wywołanie: /parametry?klucz=124&inny_klucz=asbaegf
@app.route("/parametry")
def parametry():
    # w request.args - słownik z parameterami podanymi w adresie; coś jak **kwargs w funkcjach
    # jeśli chcesz dodać klucz - musisz zrobić kopię
    moje_slownik = request.args.copy()
    moje_slownik["domek"] = "domek jest pusty"
    # return request.args
    return render_template("slownik_z_kodu.html", abc=moje_slownik)


@app.route("/dodawanie/<a>/<b>")
def dodawanie(a, b):
    wynik = float(a) + float(b)
    return str(wynik)


if __name__ == "__main__":
    app.run(debug=True)


# ZADANIE

# dodaj do szablonu 'zmienna_z_kodu.html' wyświetlenie kolejnej zmiennej


# ZADANIE

# Bazując na wyświetlaniu słowników - zrób template pokazujące listę


# ZADANIE
"""
Zrób endpointy:
 - odejmujący liczby a i b, wywoływany w postaci /odejmowanie/a/b
 - mnożący liczby a i b, wywoływany w postaci /mnozenie?a=..&b=...
"""
