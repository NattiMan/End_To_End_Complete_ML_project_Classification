#  1. TESTING LOGGER MODULE

# from src.logger import logging

# logging.info("This is a test if logger is really working well.")

# LOGGER MODULE IS WORKING PERFECT




#  2. DATA INGESTION TESTING

from src.logger import logging as log
from src.components.data_ingestion import DataIngestion


data_ingestor = DataIngestion()
data_ingestor.initiate_data_ingestion()
