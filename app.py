from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

feedbacks = []

@app.route('/feedback', methods=['POST'])
def add_feedback():
    data = request.json
    feedback = {
        "id": len(feedbacks) + 1,
        "name": data.get("name"),
        "email": data.get("email"),
        "message": data.get("message"),
        "timestamp": datetime.utcnow().isoformat()
    }
    feedbacks.append(feedback)
    return jsonify({"message": "Feedback added successfully"}), 201
feedbacks = [
    {
        "id": 1,
        "name": "Test User",
        "email": "test@example.com",
        "message": "This is test feedback",
        "timestamp": "2025-06-08T12:00:00"
    }
]

@app.route('/feedback', methods=['GET'])
def get_feedback():
    return jsonify(feedbacks)

if __name__ == '__main__':
    app.run(debug=True)
