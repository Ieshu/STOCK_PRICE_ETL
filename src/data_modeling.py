import psycopg2

def create_data_model():
    conn = psycopg2.connect(
        host="localhost", 
        port= 5432,
        database="stock_warehouse", 
        user="postgres", 
        password="ies123@IES123"
    )
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock_prices (
            id SERIAL PRIMARY KEY,
            symbol VARCHAR(10),
            price FLOAT,
            timestamp TIMESTAMP
        );
    """)
    
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_data_model()
