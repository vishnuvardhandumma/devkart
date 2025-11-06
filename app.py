from flask import Flask, render_template, jsonify

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Wireless Mouse", "price": 499},
    {"id": 2, "name": "Laptop Bag", "price": 1299},
    {"id": 3, "name": "USB-C Charger", "price": 799},
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/products")
def product_page():
    return render_template("products.html", products=PRODUCTS)

@app.route("/api/products")
def products_api():
    return jsonify(PRODUCTS)

@app.route("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
