import unittest
from src.validator import validate_amount, validate_choice

class TestTracker(unittest.TestCase):
    def test_val(self):
        self.assertTrue(validate_amount("100")[0])
        self.assertFalse(validate_amount("-10")[0])
        self.assertTrue(validate_choice("2", 5)[0])

if __name__ == "__main__":
    unittest.main()