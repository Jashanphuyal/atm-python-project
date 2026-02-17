print("--------------- Welcome to Jashan's Bank ATM ---------------")

correct_pin = 1498
attempts = 0
current_balance = 0


def balance_check():
    print("\n----------------- Balance -----------------")
    print(f"Current balance: Rs {current_balance}")
    print("-------------------------------------------")


def deposit_money(current_balance):
    amount = int(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Amount must be greater than zero.")
        return current_balance

    current_balance += amount
    print(f"Rs {amount} deposited successfully.\n")
    return current_balance


def withdraw_money(current_balance):
    print(f"\nAvailable balance: Rs {current_balance}\n")
    amount = int(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Enter a valid amount.")
        return current_balance

    if amount > current_balance:
        print(f"Insufficient balance. You need Rs {amount - current_balance} more.")
        return current_balance

    current_balance -= amount
    print(f"Rs {amount} withdrawn successfully.\n")
    return current_balance


def interface():
    global current_balance

    while True:
        print("\n----------- ATM Menu -----------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            balance_check()

        elif choice == "2":
            current_balance = deposit_money(current_balance)
            print(f"Current balance: Rs {current_balance}")

        elif choice == "3":
            current_balance = withdraw_money(current_balance)
            print(f"Current balance: Rs {current_balance}")

        elif choice == "4":
            print("\nThank you for using the ATM.")
            break

        else:
            print("Invalid choice. Please try again.")


while attempts < 3:
    pin = int(input("Enter your PIN: "))

    if pin == correct_pin:
        interface()
        break
    else:
        attempts += 1
        print("Incorrect PIN.")

        if attempts < 3:
            print(f"Attempts remaining: {3 - attempts}")

if attempts == 3:
    print("Card seized. Please contact the bank.")
