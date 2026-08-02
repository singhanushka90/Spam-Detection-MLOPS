from pymongo import MongoClient
from api.core.config import DATABASE_NAME , MONGODB_URI

client=MongoClient(MONGODB_URI)
db=client[DATABASE_NAME]

users_collection=db["users"]
prediction_collection=db["predictions"]