import unittest
from atm.account import find_by_account

class TestAccount(unittest.TestCase):
    def test_find_account(self):
        data = {"users": {"1": {"account": "SB123", "name": "Test"}}}
        self.assertEqual(find_by_account(data, "SB123")["name"], "Test")

    def test_missing_account(self):
        self.assertIsNone(find_by_account({"users": {}}, "SB999"))

if __name__ == "__main__":
    unittest.main()
