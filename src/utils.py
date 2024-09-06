import json
import logging
import os

def setup_logging():
    logging.basicConfig(filename='logs/etl.log', level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

def log(message):
    logging.info(message)

def save_raw_data(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f)

def save_processed_data(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f)
