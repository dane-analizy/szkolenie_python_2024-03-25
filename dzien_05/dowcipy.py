from flask import Flask, render_template

app = Flask(__name__)  # nazwa będzie wzięta z nazwy pliku pythona


@app.route("/zmienna")
def main():
    return render_template("zmienna_z_kodu.html", abc="inna wartosc")


if __name__ == "__main__":
    app.run(debug=True)


# ZADANIE

# dodaj do szablonu 'zmienna_z_kodu.html' wyświetlenie kolejnej zmiennej
