import unittest
from atm.transactions import withdraw, deposit, transfer

def user(account="SB100001", balance=10000):
    return {
        "name": "Test",
        "account": account,
        "pin": "1234",
        "balance": balance,
        "daily_limit": 25000,
        "withdrawn_today": 0,
        "withdraw_date": "26-09-2026",
        "blocked": False,
        "transactions": []
    }

class TestTransactions(unittest.TestCase):
    def test_withdraw(self):
        data = {"users": {}, "atm_cash": 50000}
        u = user()
        ok, _ = withdraw(data, u, 1000)
        self.assertTrue(ok)
        self.assertEqual(u["balance"], 9000)

    def test_insufficient_balance(self):
        data = {"users": {}, "atm_cash": 50000}
        u = user(balance=500)
        ok, _ = withdraw(data, u, 1000)
        self.assertFalse(ok)

    def test_deposit(self):
        data = {"users": {}, "atm_cash": 50000}
        u = user()
        ok, _ = deposit(data, u, 1000)
        self.assertTrue(ok)
        self.assertEqual(u["balance"], 11000)

    def test_transfer(self):
        sender = user("SB100001", 10000)
        receiver = user("SB100002", 5000)
        data = {"users": {"a": sender, "b": receiver}, "atm_cash": 50000}
        ok, _ = transfer(data, sender, "SB100002", 2000)
        self.assertTrue(ok)
        self.assertEqual(sender["balance"], 8000)
        self.assertEqual(receiver["balance"], 7000)

if __name__ == "__main__":
    unittest.main()
