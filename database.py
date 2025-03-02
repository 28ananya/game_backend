from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

MONGO_URI = "mongodb+srv://ananya:prLAAe1ShvdCa1uN@cluster0.iv5xn.mongodb.net/globetrotter_db?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client["globetrotter_db"]
questions_collection = db["questions"]
users_collection = db["users"]
