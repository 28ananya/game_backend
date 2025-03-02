from flask import Flask, request, jsonify
from flask_cors import CORS
from database import get_questions_collection, get_users_collection

app = Flask(__name__)
CORS(app)

# Get Random Question
@app.route("/question", methods=["GET"])
def get_question():
    collection = get_questions_collection()
    question = collection.aggregate([{ "$sample": { "size": 1 } }]).next()
    del question["_id"]  # Remove MongoDB ID field
    return jsonify(question)

# Check Answer
@app.route("/answer", methods=["POST"])
def check_answer():
    data = request.json
    user_answer = data.get("user_answer")
    destination = data.get("destination")

    collection = get_questions_collection()
    question = collection.find_one({"destination": destination})
    
    if question and user_answer == question["correct_answer"]:
        return jsonify({"correct": True, "fun_fact": question["fun_fact"]})
    return jsonify({"correct": False, "fun_fact": question["fun_fact"]})

# Register User
@app.route("/register", methods=["POST"])
def register_user():
    data = request.json
    username = data.get("username")

    collection = get_users_collection()
    if collection.find_one({"username": username}):
        return jsonify({"message": "Username already taken!"}), 400
    
    collection.insert_one({"username": username, "score": 0})
    return jsonify({"message": "User registered successfully!"})

# Get User Score
@app.route("/score/<username>", methods=["GET"])
def get_score(username):
    collection = get_users_collection()
    user = collection.find_one({"username": username})
    if user:
        return jsonify({"username": username, "score": user["score"]})
    return jsonify({"message": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
