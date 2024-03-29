# aplikacja, która wyświetla dowcipy z bazy (nasza baza, tabela jokes, ...)
# na głównej stronie - mamy listę kategorii dowcipów i tylko tyle (kolumna type)
# można kliknąć w kategorię i przejść do listy dowcipów tylko z tej kategorii, wyświetlonych wg kolejności pokazanej przez kolumnę id
# wyświetlamy tylko setup i punchline


# strona główna:
"""
- programming -> click  -> /jokes/progrmaming
- general -> click  -> /jokes/general
"""


# strona z listą dowcipów z kategorii
"""
/jokes/general

A: setup
B: punchline
---
A: setup
B: punchline
---
"""


# ROZWIĄZANIE

# lista kategorii dowcipów: "select distinct type from jokes"
# dowcipy z jednej kategorii: "select distinct  setup, punchline from jokes  where type = KATEGORIA"

from flask import Flask, render_template
from tools.config import read_config
from tools.db import get_sql_results

CONFIG_FILE = "config_db.yaml"


app = Flask(__name__)

config = read_config(CONFIG_FILE)


@app.route("/")
@app.route("/menu")
def menu():
    jokes_cat = get_sql_results(config, "select distinct type from jokes")
    jokes_cat = [ t[0] for t in jokes_cat]
    return render_template("menu.html", lista=jokes_cat)


@app.route("/jokes/<joke_cat>")
def jokes(joke_cat):
    jokes_cat = get_sql_results(config, "select distinct type from jokes")
    jokes_cat = [ t[0] for t in jokes_cat]

    sql_query = f"select distinct  setup, punchline from jokes where type = '{joke_cat}'"
    jokes = get_sql_results(config, sql_query)

    return render_template(
        "dowcipy.html",
        jokes=jokes,
        lista=jokes_cat,
        kategoria=joke_cat,
    )


if __name__ == "__main__":
    app.run(debug=True)
