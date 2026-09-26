from datetime import datetime
from .storage import save_data
from .account import find_by_account

def reset_limit(data, user):
    today = datetime.now().strftime("%d-%m-%Y")
    if user["withdraw_date"] != today:
        user["withdraw_date"] = today
        user["withdrawn_today"] = 0
        save_data(data)

def record(user, kind, amount):
    user["transactions"].append({
        "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "type": kind,
        "amount": amount,
        "balance": user["balance"]
    })

def withdraw(data, user, amount):
    reset_limit(data, user)
    if amount <= 0:
        return False, "Amount must be greater than zero."
    if amount % 100:
        return False, "Amount must be a multiple of Rs. 100."
    if amount > user["balance"]:
        return False, "Insufficient account balance."
    if amount > user["daily_limit"] - user["withdrawn_today"]:
        return False, "Daily withdrawal limit exceeded."
    if amount > data["atm_cash"]:
        return False, "ATM does not have enough cash."

    user["balance"] -= amount
    user["withdrawn_today"] += amount
    data["atm_cash"] -= amount
    record(user, "Cash Withdrawal", amount)
    save_data(data)
    return True, "Cash withdrawal successful."

def deposit(data, user, amount):
    if amount <= 0 or amount % 100:
        return False, "Deposit must be a positive multiple of Rs. 100."
    user["balance"] += amount
    data["atm_cash"] += amount
    record(user, "Cash Deposit", amount)
    save_data(data)
    return True, "Cash deposit successful."

def transfer(data, sender, account, amount):
    receiver = find_by_account(data, account)
    if receiver is None:
        return False, "Beneficiary account not found."
    if receiver["account"] == sender["account"]:
        return False, "You cannot transfer money to yourself."
    if amount <= 0:
        return False, "Amount must be greater than zero."
    if amount > sender["balance"]:
        return False, "Insufficient account balance."

    sender["balance"] -= amount
    receiver["balance"] += amount
    record(sender, "Fund Transfer", amount)
    record(receiver, "Money Received", amount)
    save_data(data)
    return True, "Transfer successful."
