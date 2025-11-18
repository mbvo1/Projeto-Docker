from flask import Flask, jsonify

app = Flask(__name__)
meus_usuarios = [
    {"id": 1, "nome": "Ana Silva", "curso": "Engenharia"},
    {"id": 2, "nome": "Beto Costa", "curso": "Direito"},
    {"id": 3, "nome": "Carla Tech", "curso": "Computacao"}
]

@app.route('/usuarios')
def listar():
    return jsonify(meus_usuarios)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)