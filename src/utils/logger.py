import os 
import sys
import logging
from datetime import datetime


# get the current folder path
current_directory = os.getcwd()

# print(current_directory)

# creating the logs directory
logs_directory = os.path.join(current_directory, "Logs")

# print(logs_directory)

# create the logs directory if it doesn't exist
if not os.path.exists(logs_directory):
    os.makedirs(logs_directory, exist_ok=True)

# creating file format

LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# print(LOG_FILE_NAME)

LOG_FILE_PATH = os.path.join(logs_directory, LOG_FILE_NAME)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[%(asctime)s] : %(levelname)s : %(name)s : %(module)s : %(message)s"
)

