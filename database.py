from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["globetrotter_db"]
questions_collection = db["questions"]
users_collection = db["users"]
