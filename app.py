from flask import Flask, request, jsonify
from flask_cors import CORS
from database import questions_collection, users_collection
import random

app = Flask(__name__)
CORS(app)

# Get Random Question
@app.route("/question", methods=["GET"])
def get_question():
    question = questions_collection.aggregate([{ "$sample": { "size": 1 } }]).next()
    del question["_id"]  # Remove MongoDB ID field
    return jsonify(question)

# Check Answer
@app.route("/answer", methods=["POST"])
def check_answer():
    data = request.json
    user_answer = data.get("user_answer")
    destination = data.get("destination")

    question = questions_collection.find_one({"destination": destination})
    
    if question and user_answer == question["correct_answer"]:
        return jsonify({"correct": True, "fun_fact": question["fun_fact"]})
    return jsonify({"correct": False, "fun_fact": question["fun_fact"]})

# Register User
@app.route("/register", methods=["POST"])
def register_user():
    data = request.json
    username = data.get("username")

    if users_collection.find_one({"username": username}):
        return jsonify({"message": "Username already taken!"}), 400
    
    users_collection.insert_one({"username": username, "score": 0})
    return jsonify({"message": "User registered successfully!"})

# Get User Score
@app.route("/score/<username>", methods=["GET"])
def get_score(username):
    user = users_collection.find_one({"username": username})
    if user:
        return jsonify({"username": username, "score": user["score"]})
    return jsonify({"message": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
