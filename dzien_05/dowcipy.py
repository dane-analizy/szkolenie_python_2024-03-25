from flask import Flask, render_template

app = Flask(__name__)  # nazwa będzie wzięta z nazwy pliku pythona


@app.route("/zmienna")
def main():
    return render_template("zmienna_z_kodu.html", abc="inna wartosc", xyz=12.34)


@app.route("/slownik")
def main_dict():
    d = {"klucz1": "napis", "klucz2": 123, "klucz3": "jestem kluczem 3"}
    return render_template("slownik_z_kodu.html", abc=d)


if __name__ == "__main__":
    app.run(debug=True)


# ZADANIE

# dodaj do szablonu 'zmienna_z_kodu.html' wyświetlenie kolejnej zmiennej
