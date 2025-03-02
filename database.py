from pymongo import MongoClient

client = MongoClient("mongodb+srv://ananya:prLAAe1ShvdCa1uN@cluster0.iv5xn.mongodb.net")
db = client["globetrotter_db"]
questions_collection = db["questions"]
users_collection = db["users"]
