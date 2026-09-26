from .storage import save_data

def verify_pin(data, user):
    if user["blocked"]:
        print("This card is blocked.")
        return False

    for attempt in range(3):
        entered = input("Enter your PIN: ").strip()
        if entered == user["pin"]:
            print("PIN verified successfully.")
            return True
        print("Incorrect PIN.")
        if attempt < 2:
            print("Attempts remaining:", 2 - attempt)

    user["blocked"] = True
    save_data(data)
    print("Too many incorrect attempts. Your card has been blocked.")
    return False

def change_pin(data, user):
    if input("Enter current PIN: ").strip() != user["pin"]:
        print("Incorrect PIN.")
        return
    new = input("Enter new 4-digit PIN: ").strip()
    if len(new) != 4 or not new.isdigit():
        print("PIN must contain exactly 4 digits.")
        return
    if input("Confirm new PIN: ").strip() != new:
        print("PINs do not match.")
        return
    user["pin"] = new
    save_data(data)
    print("PIN changed successfully.")
