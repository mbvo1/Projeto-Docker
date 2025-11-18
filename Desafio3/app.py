from flask import Flask
from redis import Redis
import socket

app = Flask(__name__)

try:
    cache = Redis(host='redis-server', port=6379)
except Exception as e:
    print("Nao deu pra conectar no Redis")

@app.route('/')
def home():
    try:
        total_visitas = cache.incr('visitas')
    except:
        return "Erro: O Banco de dados (Redis) nao esta respondendo."

    id_container = socket.gethostname()
    
    return f"Ola! Pagina visualizada {total_visitas} vezes.\n(Respondido pelo container: {id_container})\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)