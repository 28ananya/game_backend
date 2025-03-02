import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = client = MongoClient("mongodb+srv://ananya:prLAAe1ShvdCa1uN@cluster0.iv5xn.mongodb.net")

db = client["globetrotter_db"]
collection = db["questions"]

# Load CSV file
df = pd.read_csv("destinations.csv")

# Convert dataframe to JSON-like structure
data = []
for _, row in df.iterrows():
    record = {
        "city": row["city"],
        "country": row["country"],
        "clues": row["clues"].split(";"),  # Convert clues into a list
        "funfact": row["fun_fact"],
        "trivia": row["trivia"]
    }
    data.append(record)

# Insert data into MongoDB
collection.insert_many(data)

print("✅ Data successfully imported into MongoDB!")
