from flask import Flask, jsonify

app = Flask(__name__)

users_db = [
    {"id": 1, "nome": "Alice", "email": "alice@email.com"},
    {"id": 2, "nome": "Bob", "email": "bob@email.com"}
]

@app.route('/users')
def get_users():
    return jsonify(users_db)

@app.route('/')
def home():
    return "Sou o Servico de Usuarios!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)