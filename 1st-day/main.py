from flask import Flask

from flask import render_template


app = Flask(__name__)


@app.route("/")
def index():
    title = "web"
    lot = [("Lada", "крутая тачка для внатуре чётких типов", "40.000"), ("Mercedes", "для крутых", "3.000.000"), ("кадилак маргешткэка", "для богатых", "30.000.000")]

    return render_template("index.html", title=title, lot=lot)


@app.route("/lot/<header>/<text>/<price>")
def lot(header, text, price):
    title = "lot"
    lot = [(header, text, price)]

    return render_template("index.html", title=title, lot=lot)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5050)
