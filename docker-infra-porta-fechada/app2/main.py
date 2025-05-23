from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/secret")
def secret():
    return jsonify({"message": "Essa rota é só interna!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
