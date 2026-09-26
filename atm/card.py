import random

CARD_TYPES = {
    "1": ("Classic", 25000),
    "2": ("Gold", 50000),
    "3": ("Platinum", 100000)
}

def card_number(users):
    while True:
        number = str(random.randint(100000000000, 999999999999))
        if number not in users:
            return number

def account_number(users):
    used = {u["account"] for u in users.values()}
    while True:
        number = "SB" + str(random.randint(100000, 999999))
        if number not in used:
            return number

def pin():
    return str(random.randint(1000, 9999))

def choose_type():
    print("\n1. Classic   - Rs. 25,000 daily limit")
    print("2. Gold      - Rs. 50,000 daily limit")
    print("3. Platinum  - Rs. 1,00,000 daily limit")
    while True:
        choice = input("Choose card type: ").strip()
        if choice in CARD_TYPES:
            return CARD_TYPES[choice]
        print("Please enter 1, 2 or 3.")
