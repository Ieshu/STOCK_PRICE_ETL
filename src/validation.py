import json
from src.utils import log

def validate_data():
    with open("data/processed/stock_data_processed.json", 'r') as f:
        processed_data = json.load(f)
    
    for record in processed_data:
        if not all(key in record for key in ("symbol", "price", "timestamp")):
            log("Validation failed: Missing key in record.")
            return False
        if not isinstance(record['price'], float):
            log("Validation failed: Price is not a float.")
            return False
    
    log("Validation passed.")
    return True

if __name__ == "__main__":
    validate_data()
