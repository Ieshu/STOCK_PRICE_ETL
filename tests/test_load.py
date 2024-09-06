import unittest
import psycopg2
from src.load import load_data_to_warehouse

class TestLoad(unittest.TestCase):
    def test_load(self):
        conn = psycopg2.connect(
            host="localhost", 
            port=5432,
            database="stock_warehouse", 
            user="postgres", 
            password="ies123@IES123"
        )
        cursor = conn.cursor()

        try:
            # Load data into the warehouse
            load_data_to_warehouse()

            # Verify data was loaded
            cursor.execute("SELECT COUNT(*) FROM stock_prices")
            count = cursor.fetchone()[0]
            self.assertGreater(count, 0, "Data should be inserted into the stock_prices table")

        except Exception as e:
            self.fail(f"Unexpected error occurred during the test: {e}")

        finally:
            cursor.close()
            conn.close()

if __name__ == '__main__':
    unittest.main()
