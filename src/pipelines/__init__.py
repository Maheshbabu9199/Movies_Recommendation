import os
import sys
from src.utils.logger import logging


if __name__ == "__main__":
    try:
        logging.info("Pipeline Started")
        config = Configuration()
        data_ingestion = DataIngestion(config=config)
    except Exception as e:
        logging.error(e)
        raise e 