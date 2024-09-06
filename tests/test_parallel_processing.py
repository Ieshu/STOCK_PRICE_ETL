import unittest
from src.parallel_processing import parallel_extract

class TestParallelProcessing(unittest.TestCase):
    def test_parallel_extract(self):
        api_list = ["AAPL", "GOOGL"]
        results = parallel_extract(api_list)
        self.assertGreater(len(results), 0)

if __name__ == '__main__':
    unittest.main()
