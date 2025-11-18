from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    try:
        
        resposta = requests.get('http://api-usuarios:5000/usuarios')

        dados = resposta.json()
   
        html = "<h1>Lista de Alunos (Vindo da API)</h1>"
        html += "<ul>"
        for aluno in dados:
            html += f"<li><b>{aluno['nome']}</b> - {aluno['curso']}</li>"
        html += "</ul>"
        return html
        
    except Exception as e:
        return f"Erro ao conectar na API: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)