import os 
import sys
from src.utils.logger import logging
from src.config.Configurations import Configuration
from src.components.data_ingestion import DataIngestion


if __name__ == "__main__":

    try:
        logging.info("Pipeline Started")
        config = Configuration()
        data_ingestion_config  = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.initiate_data_ingestion()
        logging.info("Pipeline Completed")
    except Exception as e:
        logging.error(e)
        raise e 