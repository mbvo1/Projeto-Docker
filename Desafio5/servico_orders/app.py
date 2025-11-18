from flask import Flask, jsonify

app = Flask(__name__)

orders_db = [
    {"id": 101, "item": "Notebook", "valor": 2500},
    {"id": 102, "item": "Mouse Gamer", "valor": 150}
]
@app.route('/orders')
def get_orders():
    return jsonify(orders_db)

@app.route('/')
def home():
    return "Sou o Servico de Pedidos!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)