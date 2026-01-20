from online_banking_system import Account # Importing a class Account from module online_banking_system

# This function displays the main menu of the banking system
def display_main_menu():
    print("\n" + "="*50)
    print("BANK MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Create New Account")
    print("2. Select Account")
    print("3. View All Accounts")
    print("4. Display Total Accounts")
    print("5. Exit")
    print("="*50)

# This function displays the account menu for a selected account
def display_account_menu(account_name):
    print(f"\n" + "="*50)
    print(f"ACCOUNT: {account_name}")
    print("="*50)
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Transfer Funds")
    print("5. View Account Details")
    print("6. Return to Main Menu")
    print("="*50)

# This function displays the account type menu
def account_type_menu():
    print("===Select the Account type===")
    print("1. Savings Account")
    print("2. Current Account")

# This is the main function that runs the banking system
def main():
    print("=====Welcome to Faith John Banking Services======")

    accounts = []

    while True:
        display_main_menu()
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            print("===Create New Account===")
            acc_number = input("Enter Account Number: ")
            acc_holder_name = input("Enter Account Holder Name: ")

            while True:
                account_type_menu()
                try:
                    acc_type_choice = int(input("Enter your choice (1-2): "))

                    if acc_type_choice == 1:
                        acc_type = "Savings"
                        break
                    elif acc_type_choice == 2:
                        acc_type = "Current"
                        break
                    else:
                        print("Invalid choice. Please select 1 or 2.")                        
                except ValueError:
                    print("Invalid input. Please enter 1 or 2.")  

            new_account = Account(acc_number, acc_holder_name, acc_type)    
            accounts.append(new_account)
        
        elif choice == 2:
            if not accounts: # Check if there are any accounts available
                print("No accounts available. Please create an account first.")
                continue

            print("===Select Account===")
            for idx, acc in enumerate(accounts): # Displaying list of accounts with index
                print(f"{idx + 1}. {acc.account_holder_name}-{acc.account_number} ({acc.account_type})")
            
            try:
                acc_choice = int(input("Enter the account number to select: "))
                if 1 <= acc_choice <= len(accounts):
                    selected_account = accounts[acc_choice - 1]
                else:
                    print("Invalid choice. Please select a valid account number.")
                    continue

            except ValueError:
                print("Invalid input. Please enter a valid account number.")
                continue

            while True:
                display_account_menu(selected_account.account_holder_name)
                try:
                    acc_menu_choice = int(input("Enter your choice (1-6): "))
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 6.")
                    continue

                if acc_menu_choice == 1: # Deposit Money
                    try:
                        amount = float(input("Enter amo unt to deposit: "))
                        selected_account.deposit(amount)
                    except ValueError:
                        print("Invalid input. Please enter a valid amount.")

                elif acc_menu_choice == 2: # Withdraw Money
                    try:
                        amount = float(input("Enter amount to withdraw: "))
                        selected_account.withdraw(amount)
                    except ValueError:
                        print("Invalid input. Please enter a valid amount.")

                elif acc_menu_choice == 3: # Balance Inquiry
                    selected_account.check_balance()

                elif acc_menu_choice == 4: # Funds Transfer
                    print("===Select Target Account for Transfer===")
                    for idx, acc in enumerate(accounts): # Displaying list of accounts with index
                        if acc != selected_account:
                            print(f"{idx + 1}. {acc.account_holder_name}-{acc.account_number} ({acc.account_type})")
                    
                    try:
                        target_choice = int(input("Enter the account number to transfer funds to: "))
                        if 1 <= target_choice <= len(accounts):
                            target_account = accounts[target_choice - 1]
                            if target_account == selected_account:
                                print("Cannot transfer funds to the same account. Please select a different account.")
                                continue
                        else:
                            print("Invalid choice. Please select a valid account number.")
                            continue

                        amount = float(input("Enter amount to transfer: "))
                        selected_account.transfer_funds(target_account, amount)

                    except ValueError:
                        print("Invalid input. Please enter valid numbers.")

                elif acc_menu_choice == 5: # View Account Details
                    selected_account.display_account()

                elif acc_menu_choice == 6: # Return to Main Menu
                    break

                else:
                    print("Invalid choice. Please select a number between 1 and 6.")

        elif choice == 3: # View All Accounts
            if not accounts:
                print("No accounts available.")
            else:
                print("===All Accounts===")
                for acc in accounts: # Traversing through all accounts
                    acc.display_account() # Displaying account details
                    print("\n")

        elif choice == 4: # Display Total Accounts
            Account.get_number_of_accounts()

        elif choice == 5: # Exit
            print("Thank you for using Faith John Banking Services. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 5.")

# python interpreter entry point
if __name__ == "__main__":    
    main()