from datetime import datetime
from .card import card_number, account_number, pin, choose_type

def create_user(data):
    print("\n" + "=" * 50)
    print("             NEW USER REGISTRATION")
    print("=" * 50)

    name = input("Enter full name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    card_type, limit = choose_type()

    while True:
        try:
            balance = int(input("Enter initial deposit (Rs.): "))
            if balance < 0 or balance % 100 != 0:
                print("Enter a non-negative multiple of Rs. 100.")
                continue
            break
        except ValueError:
            print("Enter a valid whole number.")

    card = card_number(data["users"])
    account = account_number(data["users"])
    user_pin = pin()

    user = {
        "name": name,
        "account": account,
        "card_type": card_type,
        "pin": user_pin,
        "balance": balance,
        "daily_limit": limit,
        "withdrawn_today": 0,
        "withdraw_date": datetime.now().strftime("%d-%m-%Y"),
        "blocked": False,
        "transactions": [{
            "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "type": "Account Opening",
            "amount": balance,
            "balance": balance
        }]
    }

    data["users"][card] = user

    print("\nACCOUNT CREATED SUCCESSFULLY")
    print("-" * 50)
    print("Name           :", name)
    print("Account Number :", account)
    print("Card Number    :", card)
    print("Card Type      :", card_type)
    print("Daily Limit    : Rs.", f"{limit:,}")
    print("Balance        : Rs.", f"{balance:,}")
    print("ATM PIN        :", user_pin)
    print("-" * 50)
    return card

def find_by_account(data, account):
    return next((u for u in data["users"].values() if u["account"] == account), None)
