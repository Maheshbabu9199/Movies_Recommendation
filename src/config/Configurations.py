import os
import sys
from src.utils.logger import logging
from src.entity_config.entity_config import DataIngestionConfig, DataPreparationConfig, DataTransformationConfig, RecommendationsConfig
import yaml

class Configuration:
    def __init__(self):
        with open("src\config\config.yaml") as file:
            self.config = yaml.safe_load(file)


    def get_data_ingestion_config(self):
        config = self.config["data_ingestion"]
        logging.critical('inside get_data_ingestion_config')
        return DataIngestionConfig(movies_dataset_path = config['movies_dataset_path'], reviews_dataset_path = config['reviews_dataset_path'])

    
    def get_data_preparation_config(self):
        config = self.config["data_preparation"]
        logging.critical('inside get_data_preparation_config')
        return DataPreparationConfig(movies_data_path = config['movies_data_path'], reviews_data_path = config['reviews_data_path'])


    def get_data_transformation_config(self):
        config = self.config["data_transformation"]
        logging.critical('inside get_data_transformation_config')
        return DataTransformationConfig(final_dataset_path = config['final_data_path'])


    def get_recommendations_config(self):
        config = self.config["recommendations"]
        logging.critical('inside get_recommendations_config')
        print('get _recommendations _config')
        return RecommendationsConfig(top_K = config['top_n'], similarity_path = config['similarity_data_path'], movies_content_path = config['movies_content_path'])
