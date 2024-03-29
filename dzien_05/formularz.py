from flask import Flask, redirect, render_template, request, url_for

app = Flask("formularz")


@app.route("/formularz")
def formularz():
    return render_template("formularz.html")


@app.route("/trash")
@app.route("/smietnik")
def smietnik():
    return "Jestem śmietnikiem"


@app.route("/")
def main_page():
    # czy masz ustawionego cookie
    # jeśli nie -> return redirect("/formularz") logowanie -> redirect(url_for("formularz"))
    # jeśli tak -> return redirect("/twoj wall na fb")
    return ""


@app.route("/login2", methods=["POST", "GET"])
def login():
    # w request.form przychodzi:
    # ImmutableMultiDict([('login_name', 'moj-login'), ('pass_name', 'moje-haslo')])
    print(request.form)

    if request.method == "GET":
        print("Nie pytaj mnie GETem")
        return redirect(url_for("formularz"))

    elif request.method == "POST":
        return request.form

    else:
        print("Jakiś błąd")
        return "Weź nie pytaj"


if __name__ == "__main__":
    app.run(debug=True)
