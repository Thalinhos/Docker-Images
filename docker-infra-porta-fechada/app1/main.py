from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    try:
        resp = requests.get("http://app2:5000/secret")
        data = resp.json()
    except Exception as e:
        data = {"error": str(e)}

    return jsonify({
        "message": "Olá do app1",
        "app2_response": data
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
