from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    return jsonify({"response": "AI response coming soon!"})

@app.route("/log_symptom", methods=["POST"])
def log_symptom():
    return jsonify({"message": "Symptom logged (placeholder)."})

@app.route("/get_symptoms", methods=["POST"])
def get_symptoms():
    return jsonify({"logged_symptoms": []})

if __name__ == "__main__":
    app.run(debug=True)
