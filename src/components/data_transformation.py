
import os
import sys
import numpy 
import pandas as pd
from src.logger import logging as log
from src.exception import CustomException

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler


class DataTransformationConfig:
    transformationProcessor:str = os.path.join('Artifacts', 'transformationPreprocessor.pkl')

class DataTransformation:
    
    def __init__(self):
        pass
    def initiate_data_transformation(self, train_data_path, target_column, num_cols, cat_cols):

        self.DataTransformationConfigInstance = DataTransformationConfig()
        
        preprocessor = self.DataTransformationConfigInstance.transformationProcessor
        
        # The output of this module is an array ready to fit the model and the transformation processor object
        train_df = pd.read_csv(train_data_path)
        features = []
        for i in range (1,94):
           features = [f"feat_{i}" for i in range(1, 94)]

        features_train_data = train_df[features]
        target_train_data = train_df[target_column]

        







        









































