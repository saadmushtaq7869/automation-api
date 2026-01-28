from pymongo import MongoClient
import os
import certifi

MONGO_URL = os.getenv("MONGO_URL")

if not MONGO_URL:
    raise Exception("MONGO_URL is NOT SET")

client = MongoClient(
    MONGO_URL,
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=5000
)

# ✅ DATABASE NAME (IMPORTANT)
db = client["automation"]

# ✅ THIS MUST EXIST
companies_collection = db["companies"]
