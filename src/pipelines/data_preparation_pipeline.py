import os
import sys
from src.utils.logger import logging
from src.components.data_preparation import DataPreparation
from src.config.Configurations import Configuration

if __name__ == '__main__':
    try:
        logging.info('logging has started..')
        config = Configuration()
        data_preparation_config = config.get_data_preparation_config()
        data_preparation = DataPreparation(config=data_preparation_config)
        data_preparation.initiate_data_preparation()
    except Exception as e:
        logging.error(e)
        raise e