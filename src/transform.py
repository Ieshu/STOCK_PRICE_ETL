import json
import os

def transform_stock_data():
    """
    Perform data transformation on the extracted stock data.
    """
    try:
        # Ensure the file exists before trying to open it
        raw_data_path = os.path.join("data", "raw", "stock_data.json")
        if not os.path.exists(raw_data_path):
            raise FileNotFoundError(f"{raw_data_path} not found")

        with open(raw_data_path, 'r') as f:
            raw_data = json.load(f)

        # Placeholder transformation logic
        transformed_data = []
        for timestamp, data in raw_data.get("Time Series (5min)", {}).items():
            transformed_data.append({
                "timestamp": timestamp,
                "open": float(data["1. open"]),
                "high": float(data["2. high"]),
                "low": float(data["3. low"]),
                "close": float(data["4. close"]),
                "volume": int(data["5. volume"])
            })

        # Ensure the processed data directory exists
        os.makedirs(os.path.dirname("data/processed/"), exist_ok=True)

        # Save the transformed data to a file
        processed_data_path = os.path.join("data", "processed", "stock_data_processed.json")
        with open(processed_data_path, 'w') as f:
            json.dump(transformed_data, f)

        print("Data transformed and saved successfully.")
        return transformed_data

    except FileNotFoundError as fnf_err:
        print(f"File not found: {fnf_err}")
    except Exception as err:
        print(f"Error during transformation: {err}")
