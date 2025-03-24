import os

AWS_S3_BUCKET_NAME="wafer-fault"
MONGO_DATABASE_NAME="waferfaultprediction"
MONGO_COLLECTION_NAME="waferfault"
TARGET_COLUMN="quality"
#change username and pass 
MONGO_DB_URL="mongodb+srv://username:pass@cluster0.6woqi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MODEL_FILE_NAME="model"


MODEL_FILE_EXTENSION=".pkl"


artifact_folder="artifacts"