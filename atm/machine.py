from .account import create_user
from .auth import verify_pin, change_pin
from .storage import save_data
from .transactions import withdraw, deposit, transfer, reset_limit

class ATMMachine:
    FAST_CASH = [500, 1000, 2000, 5000, 10000]

    def __init__(self, data):
        self.data = data

    def register_user(self):
        create_user(self.data)
        save_data(self.data)
        input("\nPress Enter to continue...")

    def insert_card(self):
        card = input("\nEnter card number: ").strip()
        user = self.data["users"].get(card)
        if not user:
            print("Card not found.")
            return
        print("\nWelcome,", user["name"])
        if verify_pin(self.data, user):
            self.menu(user)

    def receipt(self, user, kind, amount=0):
        print("\n" + "-" * 44)
        print("                ATM RECEIPT")
        print("-" * 44)
        print("Name       :", user["name"])
        print("Account    :", user["account"])
        print("Transaction:", kind)
        if amount:
            print("Amount     : Rs.", f"{amount:,}")
        print("Balance    : Rs.", f"{user['balance']:,}")
        print("-" * 44)

    def menu(self, user):
        while True:
            reset_limit(self.data, user)
            print("\n" + "=" * 50)
            print("                 ATM MENU")
            print("=" * 50)
            print("1. Cash Withdrawal")
            print("2. Fast Cash")
            print("3. Cash Deposit")
            print("4. Balance Enquiry")
            print("5. Fund Transfer")
            print("6. Mini Statement")
            print("7. Change PIN")
            print("8. Card Services")
            print("9. Eject Card")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.withdraw_menu(user)
            elif choice == "2":
                self.fast_cash(user)
            elif choice == "3":
                self.deposit_menu(user)
            elif choice == "4":
                print("Available balance: Rs.", f"{user['balance']:,}")
                self.receipt(user, "Balance Enquiry")
            elif choice == "5":
                self.transfer_menu(user)
            elif choice == "6":
                print("\n----------- MINI STATEMENT -----------")
                for t in user["transactions"][-5:]:
                    print(t["date"], "|", t["type"], "| Rs.", f"{t['amount']:,}", "| Balance:", f"Rs. {t['balance']:,}")
            elif choice == "7":
                change_pin(self.data, user)
            elif choice == "8":
                self.card_services(user)
            elif choice == "9":
                print("Please take your card.")
                return
            else:
                print("Invalid choice.")

    def withdraw_menu(self, user):
        try:
            amount = int(input("Enter amount to withdraw: Rs. "))
        except ValueError:
            print("Enter a valid amount.")
            return
        ok, msg = withdraw(self.data, user, amount)
        print(msg)
        if ok:
            print("Please collect your cash.")
            self.receipt(user, "Cash Withdrawal", amount)

    def fast_cash(self, user):
        print("\n1. Rs. 500\n2. Rs. 1,000\n3. Rs. 2,000\n4. Rs. 5,000\n5. Rs. 10,000\n6. Other Amount\n7. Cancel")
        choice = input("Choose an option: ").strip()
        if choice == "7":
            return
        if choice == "6":
            self.withdraw_menu(user)
            return
        if choice not in "12345":
            print("Invalid choice.")
            return
        amount = self.FAST_CASH[int(choice) - 1]
        ok, msg = withdraw(self.data, user, amount)
        print(msg)
        if ok:
            print("Please collect your cash.")
            self.receipt(user, "Fast Cash", amount)

    def deposit_menu(self, user):
        try:
            amount = int(input("Enter amount to deposit: Rs. "))
        except ValueError:
            print("Enter a valid amount.")
            return
        ok, msg = deposit(self.data, user, amount)
        print(msg)
        if ok:
            self.receipt(user, "Cash Deposit", amount)

    def transfer_menu(self, user):
        account = input("Enter beneficiary account number: ").strip()
        try:
            amount = int(input("Enter transfer amount: Rs. "))
        except ValueError:
            print("Enter a valid amount.")
            return
        receiver = next((u for u in self.data["users"].values() if u["account"] == account), None)
        if receiver:
            print("Receiver:", receiver["name"])
            if input("Confirm transfer? (Y/N): ").upper() != "Y":
                print("Transfer cancelled.")
                return
        ok, msg = transfer(self.data, user, account, amount)
        print(msg)
        if ok:
            self.receipt(user, "Fund Transfer", amount)

    def card_services(self, user):
        while True:
            print("\n1. Change PIN\n2. Block Card\n3. Unblock Card\n4. Card Details\n5. Back")
            choice = input("Choose an option: ").strip()
            if choice == "1":
                change_pin(self.data, user)
            elif choice == "2":
                user["blocked"] = True
                save_data(self.data)
                print("Card blocked.")
                return
            elif choice == "3":
                if input("Enter PIN: ").strip() == user["pin"]:
                    user["blocked"] = False
                    save_data(self.data)
                    print("Card unblocked.")
                else:
                    print("Incorrect PIN.")
            elif choice == "4":
                print("Name:", user["name"])
                print("Account:", user["account"])
                print("Card Type:", user["card_type"])
                print("Daily Limit: Rs.", f"{user['daily_limit']:,}")
                print("Status:", "Blocked" if user["blocked"] else "Active")
            elif choice == "5":
                return
            else:
                print("Invalid choice.")

    def information(self):
        print("\nATM cash available: Rs.", f"{self.data['atm_cash']:,}")
        print("Minimum withdrawal: Rs. 100")
        print("Maximum PIN attempts: 3")
        print("Fast Cash: Rs. 500, 1,000, 2,000, 5,000, 10,000")
        input("\nPress Enter to continue...")
