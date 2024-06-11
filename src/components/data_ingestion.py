import os
import sys
from src.utils.logger import logging
import pandas as pd
from src.utils.utils import save_artifacts

class DataIngestion:
    def __init__(self, config):
        try:
            self.config = config
            logging.info("Data Ingestion Configured")
        except Exception as e:
            raise e 

    def initiate_data_ingestion(self):
        try:
            logging.info("Entered the data ingestion method or component")
            # read the csv file
            movies_data = pd.read_csv(self.config.movies_dataset_path)
            reviews_data = pd.read_csv(self.config.reviews_dataset_path)
            print(movies_data.shape)
            print(reviews_data.shape)
            save_artifacts(data=movies_data, name="movies")
            save_artifacts(data=reviews_data, name="reviews")
            return "Data Ingestion Completed"
        except Exception as e:
            raise e