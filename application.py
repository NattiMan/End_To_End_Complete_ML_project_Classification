#  1. TESTING LOGGER MODULE

# from src.logger import logging

# logging.info("This is a test if logger is really working well.")

# LOGGER MODULE IS WORKING PERFECT




#  2. DATA INGESTION TESTING

# from src.logger import logging as log
# from src.components.data_ingestion import DataIngestion


# data_ingestor = DataIngestion()
# data_ingestor.initiate_data_ingestion()

# 3. DATA TRANSFORMATION TESTING

from src.components.data_transformation import DataTransformation

train_data_path = 'Artifacts/train_data.csv'
test_data_path = 'Artifacts/test_data.csv'
target_column = 'target'
feature_cols = [f"feat_{i}" for i in range(1,94)]

# data_transformer = DataTransformation(feature_columns=feature_cols, target_column=target_column, num_cols=feature_cols, cat_cols=target_column)
data_transformer = DataTransformation()
train_arr, test_arr,_ = data_transformer.initiate_data_transformation(train_data_path,test_data_path)

# 4. MODEL TRAINING TESTING

from src.components.model_trainer import ModelTrainer

trainer = ModelTrainer()
trainer.initiate_model_trainer(train_arr, test_arr)

# import pandas as pd
# df=pd.read_csv('Artifacts/test_data.csv')
# print(df.columns)