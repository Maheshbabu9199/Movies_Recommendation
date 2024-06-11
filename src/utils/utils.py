import os 
import sys
from src.utils.logger import logging


def save_artifacts(data=None, name=None):
    try:

        if data is None:
            logging.info("No data to save")
            return
        else:
            os.makedirs('Artifacts', exist_ok=True) 
            data.to_csv('Artifacts/'+name+'.csv', index=False)
            logging.warning(f'{name} data saved successfully')
            print(f'{name} data saved successfully')
            return 

    except Exception as e:
        logging.error('error in saving artifacts')
        raise e