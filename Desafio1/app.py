from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def index():
    hostname = socket.gethostname()
    return f"Ola do container ID: {hostname}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)