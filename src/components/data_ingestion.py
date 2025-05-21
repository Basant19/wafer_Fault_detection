import pandas as pd
import numpy as np
import os
import sys 
from pymongo import MongoClient
from zipfile import Path
from src.constant import *
from src.exception import CustomException
from src.logger import logging
from src.utils.main_utils import MainUtils
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    """
    Configuration class for Data Ingestion.
    This class holds the configuration for storing ingested data.
    """
    artifact_folder: str = os.path.join(artifact_folder)
    
class DataIngestion:
    """
    This class is responsible for data ingestion from MongoDB.
    It exports the collection as a DataFrame and saves it to a CSV file.
    """
    def __init__(self) -> None:
        """
        Initializes the DataIngestion class with configuration and utility functions.
        """
        self.data_ingestion_config = DataIngestionConfig()
        self.utils = MainUtils()
    
    def export_collection_as_dataframe(self, collection_name: str, db_name: str) -> pd.DataFrame:
        """
        Fetches data from MongoDB and converts it into a Pandas DataFrame.
        
        Parameters:
            collection_name (str): Name of the collection to fetch data from.
            db_name (str): Name of the database.
            
        Returns:
            pd.DataFrame: DataFrame containing the exported data.
        """
        try:
            # Connect to MongoDB
            mongo_client = MONGO_DB_URL
            collection = mongo_client[db_name][collection_name]
            
            # Convert collection to DataFrame
            df = pd.DataFrame(list(collection.find()))
            
            # Drop MongoDB default '_id' column
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            
            # Replace "na" values with NaN
            df.replace({"na": np.nan}, inplace=True)
            
            return df
        except Exception as e:
            raise CustomException(e, sys)
        
    def export_data_into_feature_store_file_path(self) -> str:
        """
        Exports the fetched data into a CSV file and stores it in a specified location.
        
        Returns:
            str: File path of the stored CSV file.
        """
        try:
            logging.info("Exporting data from MongoDB")
            
            # Create directory if not exists
            raw_file_path = self.data_ingestion_config.artifact_folder
            os.makedirs(raw_file_path, exist_ok=True)
            
            # Fetch data from MongoDB
            sensor_data = self.export_collection_as_dataframe(
                collection_name=MONGO_COLLECTION_NAME,
                db_name=MONGO_DATABASE_NAME
            )
            
            # Define file path for CSV
            feature_store_file_path = os.path.join(raw_file_path, "wafer_fault.csv")
            
            # Save data to CSV
            sensor_data.to_csv(feature_store_file_path, index=False)
            
            logging.info(f"Saved exported data into feature store file path: {feature_store_file_path}")
            
            return feature_store_file_path
        except Exception as e:
            raise CustomException(e, sys)
    
    def initiate_data_ingestion(self) -> Path:
        """
        Initiates the data ingestion process by fetching and storing the data.
        
        Returns:
            Path: File path of the stored CSV file.
        """
        logging.info("Entered initiate_data_ingestion method of DataIngestion class")
        try:
            # Fetch and store data
            feature_store_file_path = self.export_data_into_feature_store_file_path()
            logging.info("Successfully retrieved data from MongoDB")
            logging.info(f"Stored CSV file in the following path: {feature_store_file_path}")
            
            return feature_store_file_path
        except Exception as e:
            raise CustomException(e, sys)
