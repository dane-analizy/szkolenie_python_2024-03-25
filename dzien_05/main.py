# frame work do robienia "szybkich" aplikacji https://streamlit.io/


# Flask

# pip install flask

# from flask import Flask

# # app = Flask("nasza apka") # w nawiasie nazwa naszej aplikacji
# app = Flask(__name__) # nazwa będzie wzięta z nazwy pliku pythona

# # print(app)

# if __name__ == '__main__':
#     app.run()


# from flask import Flask

# app = Flask(__name__)  # nazwa będzie wzięta z nazwy pliku pythona


# @app.route("/")
# def home_page():
#     print("uruchamiam stronę główną")
#     return "To ja, strona główna i życzę miłego dnia"


# @app.route("/stronapierwsza")
# def strona_pierwsza():
#     return "Jestem stroną pierwszą"


# @app.route("/stronadruga")
# def strona_druga():
#     return "Jestem stroną drugą"


# if __name__ == "__main__":
#     # debug=True powoduje, że Flask przeładuje aplikację po zmianie kodu
#     app.run(debug=True)


# ZADANIE

# Do powyższej aplikacji dodaj kilka kolejnych strony.


from flask import Flask, render_template

app = Flask(__name__)  # nazwa będzie wzięta z nazwy pliku pythona


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/druga")
def home_page():
    return render_template("druga_strona.html")


def dodawanie(a, b):
    return a + b


@app.route("/suma")
def suma():
    a = 1
    b = 2
    wynik = dodawanie(a, b)
    return f'{{ "a": {a}, "b": {b}, "suma": {wynik} }}'


if __name__ == "__main__":
    # debug=True powoduje, że Flask przeładuje aplikację po zmianie kodu
    app.run(debug=True)


# ZADANIE

# Dodaj kilka podstron, które będą pokazywać inne pliki html.
