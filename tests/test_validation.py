import unittest
import json
from src.validation import validate_data

class TestValidation(unittest.TestCase):
    def setUp(self):
        # Mock transformed data for validation
        self.mock_data = [
            {"symbol": "AAPL", "price": 145.30, "timestamp": "2024-09-01T00:00:00Z"}
        ]
        with open("data/processed/stock_data_processed.json", 'w') as f:
            json.dump(self.mock_data, f)

    def test_validate_data(self):
        self.assertTrue(validate_data())

if __name__ == '__main__':
    unittest.main()
