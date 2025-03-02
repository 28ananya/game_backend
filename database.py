from pymongo import MongoClient
import os
import ssl
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://ananya:prLAAe1ShvdCa1uN@cluster0.iv5xn.mongodb.net/globetrotter_db?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true")

def get_db():
    client = MongoClient(MONGO_URI)
    return client.get_database("globetrotter_db")  # Replace with actual DB name

def get_questions_collection():
    return get_db()["questions"]

def get_users_collection():
    return get_db()["users"]

