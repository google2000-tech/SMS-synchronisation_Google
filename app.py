from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://google2000-tech.github.io/SMS-synchronisation_Google/"])  # Autorise ton site Netlify

@app.route("/")
def home():
    return jsonify({"message": "Serveur Flask en ligne ✅"})

@app.route("/api/test", methods=["POST", "GET"])
def test():
    if request.method == "POST":
        data = request.get_json()
        return jsonify({"message": "Reçu !", "data": data})
    else:  # GET
        return jsonify({"message": "Cette route attend une requête POST avec JSON"})

if __name__ == "__main__":
    app.run()
