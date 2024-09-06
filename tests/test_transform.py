import unittest
import json
import os
from src.transform import transform_stock_data

class TestTransform(unittest.TestCase):
    
    def setUp(self):
        # Mock raw data for testing that matches the expected structure in transform_stock_data
        self.mock_data = {
            "Meta Data": {
                "1. Information": "Intraday (5min) open, high, low, close prices and volume",
                "2. Symbol": "AAPL"
            },
            "Time Series (5min)": {
                "2024-09-04 09:30:00": {
                    "1. open": "150.00",
                    "2. high": "151.00",
                    "3. low": "149.50",
                    "4. close": "150.50",
                    "5. volume": "1000000"
                },
                "2024-09-04 09:35:00": {
                    "1. open": "150.60",
                    "2. high": "152.00",
                    "3. low": "150.00",
                    "4. close": "151.50",
                    "5. volume": "500000"
                }
            }
        }

        # Ensure the raw data directory exists
        os.makedirs("data/raw", exist_ok=True)
        
        # Save mock data to the file
        with open("data/raw/stock_data.json", 'w') as f:
            json.dump(self.mock_data, f)

    def test_transform_stock_data(self):
        # Call the function to transform the data
        transformed_data = transform_stock_data()

        # Expected transformed data based on mock_data
        expected_data = [
            {
                "timestamp": "2024-09-04 09:30:00",
                "open": 150.00,
                "high": 151.00,
                "low": 149.50,
                "close": 150.50,
                "volume": 1000000
            },
            {
                "timestamp": "2024-09-04 09:35:00",
                "open": 150.60,
                "high": 152.00,
                "low": 150.00,
                "close": 151.50,
                "volume": 500000
            }
        ]
        
        # Assert that the transformed data matches the expected data
        self.assertEqual(transformed_data, expected_data)

    def tearDown(self):
        # Clean up the mock data file after tests
        if os.path.exists("data/raw/stock_data.json"):
            os.remove("data/raw/stock_data.json")

if __name__ == '__main__':
    unittest.main()
