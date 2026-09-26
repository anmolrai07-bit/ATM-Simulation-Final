import unittest
from unittest.mock import patch
from atm.auth import verify_pin

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.data = {"users": {}, "atm_cash": 500000}
        self.user = {"name": "Test", "account": "SB1", "pin": "1234", "blocked": False}

    @patch("builtins.input", return_value="1234")
    def test_correct_pin(self, _):
        self.assertTrue(verify_pin(self.data, self.user))

    @patch("builtins.input", side_effect=["1", "2", "3"])
    def test_three_wrong_pins(self, _):
        self.assertFalse(verify_pin(self.data, self.user))
        self.assertTrue(self.user["blocked"])

if __name__ == "__main__":
    unittest.main()
