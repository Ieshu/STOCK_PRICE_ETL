import requests
import yaml
import os
from src.utils import save_raw_data, setup_logging, log

def extract_stock_data(config):
    """
    Extract stock data from the provided API endpoint.
    
    Parameters:
    config (dict): Configuration dictionary containing API details.
    
    Returns:
    dict: The stock data in JSON format.
    """
    setup_logging()
    
    try:
        url = config['api']['stock_data_api']['url']
        token = config['api']['stock_data_api']['token']
        headers = {'Authorization': f'Bearer {token}'}
        
        # Log the extraction process
        log(f"Starting stock data extraction from {url}")
        
        # Make the API request
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Log successful API response
        log("Stock data API request successful.")
        
        # Get the data and save it to a file
        data = response.json()
        save_raw_data(data, os.path.join("data", "raw", "stock_data.json"))
        
        # Log successful data saving
        log(f"Raw stock data saved successfully to data/raw/stock_data.json")
        
        return data
    
    except requests.exceptions.HTTPError as http_err:
        log(f"HTTP error occurred: {http_err}")
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        log(f"Other error occurred: {err}")
        print(f"Other error occurred: {err}")

if __name__ == "__main__":
    # Construct config path dynamically
    config_path = os.path.join('config', 'config.yaml')
    
    # Load configuration
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    # Extract stock data
    extract_stock_data(config)
