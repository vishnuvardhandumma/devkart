from flask import Flask, render_template, jsonify

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Wireless Mouse", "price": 499, "image": "https://m.media-amazon.com/images/I/61LtuGzXeaL._AC_SL1500_.jpg"},
    {"id": 2, "name": "Laptop Bag", "price": 1299, "image": "https://m.media-amazon.com/images/I/81lB-Cu9nJL._AC_SL1500_.jpg"},
    {"id": 3, "name": "USB-C Charger", "price": 799, "image": "https://m.media-amazon.com/images/I/61uY6pYtLCL._AC_SL1500_.jpg"},
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def products_page():
    return render_template("products.html", products=PRODUCTS)

@app.route("/cart")
def cart_page():
    return render_template("cart.html")

@app.route("/account")
def account_page():
    return render_template("account.html")

@app.route("/api/products")
def products_api():
    return jsonify(PRODUCTS)

@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
