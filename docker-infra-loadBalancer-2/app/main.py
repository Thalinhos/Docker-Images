from flask import Flask
import socket
from psycopg2 import pool

app = Flask(__name__)

# Criando o pool na inicialização do app
db_pool = pool.SimpleConnectionPool(
    1, 20,  # minconn, maxconn
    host="db",
    database="meubanco",
    user="meuuser",
    password="minhasenha"
)

@app.route("/")
def hello():
    conn = db_pool.getconn()
    try:
        # Aqui você faria sua lógica com o banco
        # Exemplo: cursor = conn.cursor() ...
        return f"Hello from Flask with PostgreSQL! ->  {socket.gethostname()}"
    finally:
        db_pool.putconn(conn)  # devolve a conexão ao pool

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
