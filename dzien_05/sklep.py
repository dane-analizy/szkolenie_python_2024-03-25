from flask import Flask, render_template

app = Flask(__name__)  # nazwa będzie wzięta z nazwy pliku pythona


@app.route("/")
def main():
    return render_template("sklep_hp.html")


@app.route("/produkty")
def produkty():
    return render_template("sklep_produkty.html")


@app.route("/uslugi")
def uslugi():
    return render_template("sklep_uslugi.html")


@app.route("/kontakt")
def kontakt():
    return render_template("sklep_kontakt.html")


@app.route("/o_nas")
def o_nas():
    return render_template("sklep_onas.html")


if __name__ == "__main__":
    # debug=True powoduje, że Flask przeładuje aplikację po zmianie kodu
    app.run(debug=True)


# ZADANIE

# Do szablonów wszystkich stron sklepu dodaj nawigację
