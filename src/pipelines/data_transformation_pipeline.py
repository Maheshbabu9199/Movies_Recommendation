import os
import sys
from src.utils.logger import logging
from src.config.Configurations import Configuration 
from src.components.data_transformation import DataTransformation


if __name__ == '__main__':
    try:
        logging.info('data transformation has started..')
        config = Configuration()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.initiate_data_transformation()
    except Exception as e:
        logging.error(e)
        raise e 