import unittest
from src.monitoring import monitor_etl_process

class TestMonitoring(unittest.TestCase):
    def test_monitoring(self):
        # This would be more meaningful if you could check log outputs
        monitor_etl_process()
        # Check logs or other monitoring indicators if needed

if __name__ == '__main__':
    unittest.main()
