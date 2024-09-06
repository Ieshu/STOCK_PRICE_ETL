import unittest
from unittest.mock import patch, MagicMock
from src.extract import extract_stock_data
import os

class TestExtract(unittest.TestCase):

    @patch('src.extract.save_raw_data')
    @patch('src.extract.requests.get')
    @patch('src.extract.setup_logging')  # Mocking logging to avoid creating log files during testing
    @patch('src.extract.log')  # Mocking log to prevent actual logging during testing
    def test_extract(self, mock_log, mock_setup_logging, mock_requests_get, mock_save_raw_data):
        # Mock configuration
        config = {
            'api': {
                'stock_data_api': {
                    'url': 'https://api.example.com/stock',
                    'token': 'test_token'
                }
            }
        }
        
        # Mock response data
        mock_response_data = {
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
                }
            }
        }

        # Mock requests.get to return a mock response
        mock_response = MagicMock()
        mock_response.json.return_value = mock_response_data
        mock_response.raise_for_status = MagicMock()  # To avoid raising any HTTPError in tests
        mock_requests_get.return_value = mock_response

        # Call the function to test
        data = extract_stock_data(config)
        
        # Assertions
        mock_requests_get.assert_called_once_with('https://api.example.com/stock', headers={'Authorization': 'Bearer test_token'})
        mock_save_raw_data.assert_called_once_with(mock_response_data, os.path.join("data", "raw", "stock_data.json"))
        self.assertEqual(data, mock_response_data)
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()
