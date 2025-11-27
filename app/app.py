from flask import Flask, render_template, request, redirect, url_for
from db import get_connection

app = Flask(__name__)

@app.route("/")
def index():
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT id, name, price FROM products;")
        products = cur.fetchall()
    conn.close()
    return render_template("index.html", products=products)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    price = request.form["price"]
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("INSERT INTO products (name, price) VALUES (%s, %s);", (name, price))
        conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
