from atm.machine import ATMMachine
from atm.storage import load_data

def main():
    data = load_data()
    atm = ATMMachine(data)

    while True:
        print("\n" + "=" * 50)
        print("                 WELCOME TO ATM")
        print("=" * 50)
        print("1. Insert Card")
        print("2. Register New User")
        print("3. ATM Information")
        print("4. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            atm.insert_card()
        elif choice == "2":
            atm.register_user()
        elif choice == "3":
            atm.information()
        elif choice == "4":
            print("\nThank you for using our ATM. Have a nice day!")
            break
        else:
            print("Please choose 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()
