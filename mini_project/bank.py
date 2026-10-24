balance = 1000
correct_pin = "1234"
transactions = 0

attempts = 0
pin_correct = False

while attempts < 3:
    entered_pin = input("Enter your PIN: ")

    if entered_pin == correct_pin:
        print("PIN correct!")
        print("Welcome to Akiba Bank.")
        pin_correct = True
        break
    else:
        attempts = attempts + 1
        print("Incorrect PIN.")
        print("Attempts remaining:", 3 - attempts)

if pin_correct == False:
    print("Too many incorrect attempts.")
    print("Your account is locked.")

if pin_correct == True:

    while True:
        print("\n===== AKIBA BANK =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Your current balance is:", balance, "Birr")

        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))

                if amount > 0:
                    balance = balance + amount
                    transactions = transactions + 1
                    print("Deposit successful!")
                    print("Your new balance is:", balance, "Birr")
                else:
                    print("Invalid amount. Enter a positive amount.")

            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    print("Invalid amount. Enter a positive amount.")

                elif amount > balance:
                    print("Insufficient balance!")

                else:
                    balance = balance - amount
                    transactions = transactions + 1
                    print("Withdrawal successful!")
                    print("Your new balance is:", balance, "Birr")

            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "4":
            print("Transactions made:", transactions)
            print("Thank you for using Akiba Bank!")
            print("Goodbye!")
            break

        else:
            print("Invalid option.")
            print("Please choose a valid option.")

# Akiba Bank System

# Starting account information
balance = 1000
correct_pin = "1234"
transactions = 0

# PIN verification
attempts = 0
pin_correct = False

while attempts < 3:
    entered_pin = input("Enter your PIN: ")

    if entered_pin == correct_pin:
        print("PIN correct!")
        print("Welcome to Akiba Bank.")
        pin_correct = True
        break
    else:
        attempts = attempts + 1
        print("Incorrect PIN.")
        print("Attempts remaining:", 3 - attempts)

# Stop access if the PIN is incorrect three times
if pin_correct == False:
    print("Too many incorrect attempts.")
    print("Your account is locked.")

# Bank menu
if pin_correct == True:

    while True:
        print("\n===== AKIBA BANK =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option: ")

        # Check balance
        if choice == "1":
            print("Your current balance is:", balance, "Birr")

        # Deposit money
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))

                if amount > 0:
                    balance = balance + amount
                    transactions = transactions + 1
                    print("Deposit successful!")
                    print("Your new balance is:", balance, "Birr")
                else:
                    print("Invalid amount. Enter a positive amount.")

            except ValueError:
                print("Invalid input. Please enter a number.")

        # Withdraw money
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    print("Invalid amount. Enter a positive amount.")

                elif amount > balance:
                    print("Insufficient balance!")

                else:
                    balance = balance - amount
                    transactions = transactions + 1
                    print("Withdrawal successful!")
                    print("Your new balance is:", balance, "Birr")

            except ValueError:
                print("Invalid input. Please enter a number.")

        # Exit the bank
        elif choice == "4":
            print("Transactions made:", transactions)
            print("Thank you for using Akiba Bank!")
            print("Goodbye!")
            break

        # Handle invalid menu options
        else:
            print("Invalid option.")
            print("Please choose a valid option.")
