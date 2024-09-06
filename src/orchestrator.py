from src.extract import extract_stock_data
from src.transform import transform_stock_data
from src.data_modeling import create_data_model
from src.utils import log
import os
import yaml

def orchestrate_etl():
    try:
        # Step 1: Monitor ETL process
        log("Starting ETL process")
        
        # Step 2: Create data model
        create_data_model()
        log("Data model created successfully")
        
        # Step 3: Extract stock data
        config_path = os.path.join('config', 'config.yaml')
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        data = extract_stock_data(config)
        log("Stock data extracted successfully")
        
        # Step 4: Transform stock data
        if data:  # Only transform if data was extracted successfully
            transformed_data = transform_stock_data()
            log("Stock data transformed successfully")
        else:
            log("No data available to transform.")
    except Exception as e:
        log(f"Error in ETL process: {e}")

