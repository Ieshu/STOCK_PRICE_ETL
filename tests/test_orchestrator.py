import unittest
from src.orchestrator import orchestrate_etl

class TestOrchestrator(unittest.TestCase):
    def test_orchestrate_etl(self):
        orchestrate_etl()
        # Verify end-to-end processing if needed

if __name__ == '__main__':
    unittest.main()
