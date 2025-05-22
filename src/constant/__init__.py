import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
load_dotenv()
MONGO_DB_URL =MongoClient(os.getenv('MONGODB_URI'))
AWS_S3_BUCKET_NAME="wafer-fault"
MONGO_DATABASE_NAME="waferfaultprediction"
MONGO_COLLECTION_NAME="waferfault"
TARGET_COLUMN="quality"
#change username and pass 

MODEL_FILE_NAME="model"

MODEL_FILE_EXTENSION=".pkl"
artifact_folder="artifacts"