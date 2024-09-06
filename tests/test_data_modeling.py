import unittest
from src.data_modeling import create_data_model
import psycopg2

class TestDataModeling(unittest.TestCase):
    def test_create_data_model(self):
        create_data_model()
        
        conn = psycopg2.connect(
            host="localhost", 
            port= 5432,
            database="stock_warehouse", 
            user="postgres", 
            password="ies123@IES123"
        )
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT EXISTS (
                SELECT 1 
                FROM information_schema.tables 
                WHERE table_schema = 'public' 
                AND table_name = 'stock_prices'
            );
        """)
        exists = cursor.fetchone()[0]
        self.assertTrue(exists)
        
        cursor.close()
        conn.close()

if __name__ == '__main__':
    unittest.main()
