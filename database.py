from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from pymongo import ASCENDING, TEXT
import os

load_dotenv()

MONGO_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

client = AsyncIOMotorClient(MONGO_URL)

db = client[DATABASE_NAME]

users = db["users"]
users.create_index(
    "email",
    unique = True
)

posts = db["posts"]

posts.create_index(
    [
        ("title",TEXT),
        ("content",TEXT)
    ]
)

comments = db["comments"]

categories = db["categories"]

tags = db["tags"]