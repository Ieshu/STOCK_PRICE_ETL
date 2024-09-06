import unittest
from src.warehouse_loader import load_warehouse

class TestWarehouseLoader(unittest.TestCase):
    def test_load_warehouse(self):
        # Assuming you have test data already loaded
        load_warehouse()
        # You could verify data in the warehouse if needed

if __name__ == '__main__':
    unittest.main()
