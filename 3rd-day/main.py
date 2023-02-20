from flask import Flask

from flask import render_template, request, flash


app = Flask(__name__)
app.config["SECRET_KEY"] = "19022008"


@app.route("/")
def index():
    title = "web"
    lot = [("Lada", "крутая тачка", "10.000"), ("Mercedes", "машина премиум класса", "5.000.000"),
           ("Renault Logan", "средняя ценовая категория", "1.000.000")]

    return render_template("index.html", title=title, lot=lot)


@app.route("/lot/<header>/<text>/<price>")
def lot(header, text, price):
    title = "lot"
    lot = [(header, text, price)]

    return render_template("index.html", title=title, lot=lot)


@app.route("/base")
def base_index():
    return render_template("base_index.html")


@app.route("/extend_base")
def extend_base():
    lot = [("Lada", "крутая тачка", "10.000"), ("Mercedes", "машина премуим классх", "5.000.000"),
           ("Renault Logan", "средняя ценовая категория", "1.000.000")]
    return render_template("extend_base_index.html", lst=lot)


@app.route("/form", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        if len(request.form["username"]) >= 4:
            flash("Форма отправлена", category="success")
        else:
            flash("Ошибка", category="error")
    return render_template("form_index.html")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5050)
