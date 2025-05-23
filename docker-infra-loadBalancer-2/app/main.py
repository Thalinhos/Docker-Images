import socket
from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route("/")
def hello():
    conn = psycopg2.connect(
        host="db",
        database="meubanco",
        user="meuuser",
        password="minhasenha"
    )
    return f"Hello from Flask with PostgreSQL! ->  {socket.gethostname()}" #added to show the hostname of the container

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
