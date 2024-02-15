import os
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
import sys
from dataclasses import dataclass

from src.logger import logging as log
from src.exception import CustomException

@dataclass
class DataIngestionConfig:
    os.makedirs('Artifacts', exist_ok=True)
    train_data_path: str = os.path.join('Artifacts', 'train_data.csv')
    test_data_path: str = os.path.join('Artifacts', 'test_data.csv')
    mongo_data_path = 'data/data_from_mongodb.csv'

class DataIngestion:

    def __init__(self):

        self.dataIngetsionConfigInstance = DataIngestionConfig()
    
    def initiate_data_ingestion(self):

        train_data_path = self.dataIngetsionConfigInstance.train_data_path
        test_data_path = self.dataIngetsionConfigInstance.test_data_path

        mongo_data_path = self.dataIngetsionConfigInstance.mongo_data_path
        source_df = pd.read_csv(mongo_data_path)

        train_df, test_df = train_test_split(source_df, test_size=0.3, random_state=42)
        train_df.to_csv(train_data_path)
        test_df.to_csv(test_data_path)

        return (train_data_path, test_data_path)















