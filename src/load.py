import psycopg2
import json
from src.utils import log

def load_data_to_warehouse():
    conn = psycopg2.connect(
        host="localhost", 
        port= 5432,
        database="stock_warehouse", 
        user="postgres", 
        password="ies123@IES123"
    )
    cursor = conn.cursor()
    
    with open("data/processed/stock_data_processed.json", 'r') as f:
        processed_data = json.load(f)

    # Print processed data before loading into DB
    print(f"Processed Data Before Insertion: {processed_data}")
    
    for record in processed_data:
        print(f"Record Keys: {record.keys()}")  # Print keys to confirm structure
        print(f"Inserting record: {record}")

        cursor.execute("""
            INSERT INTO stock_prices (symbol, price, timestamp)
            VALUES (%s, %s, %s)
        """, (record['symbol'], record['price'], record['timestamp']))
    
    conn.commit()
    cursor.close()
    conn.close()
    log("Data loaded to warehouse successfully.")

    conn = psycopg2.connect(
        host="localhost", 
        port= 5432,
        database="stock_warehouse", 
        user="postgres", 
        password="ies123@IES123"
    )
    cursor = conn.cursor()
    
    with open("data/processed/stock_data_processed.json", 'r') as f:
        processed_data = json.load(f)
    
    # Print the processed data to ensure it's being read correctly
    print("Processed Data: ", processed_data)

    for record in processed_data:
        print(f"Inserting record: {record}")  # Debug output before inserting
        
        cursor.execute("""
            INSERT INTO stock_prices (symbol, price, timestamp)
            VALUES (%s, %s, %s)
        """, (record['symbol'], record['price'], record['timestamp']))
    
    conn.commit()
    cursor.close()
    conn.close()
    log("Data loaded to warehouse successfully.")
