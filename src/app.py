from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({ "message": "Hello World" })

@app.route("/<string:name>")
def get(name):
    name = "Obteniendo "+ name
    return jsonify({ "name": name })

@app.route("/", methods=["POST"])
def post():
    name = request.json["name"]
    return jsonify({ "name": name })

@app.route("/<string:name>", methods=["DELETE"])
def delete(name):
    name = "Eliminando "+ name
    return jsonify({"name": name})

@app.route("/<string:name>", methods=["PUT"])
def put(name):
    name = "Editando "+ name
    return jsonify({"name": name})

if __name__ == "__main__":
    app.run(debug=True, port=3000)
