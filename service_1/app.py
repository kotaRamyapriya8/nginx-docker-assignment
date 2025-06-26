from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/service1")
def hello():
    return jsonify({"message": "Hello from Service 1"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

