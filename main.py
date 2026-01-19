from online_banking_system import Account # Importing a class Account from module online_banking_system


print("=====Welcome to Faith John Banking Services======")

account_number = input("Please enter the account number:  ")
account_holder_name = input("Enter the account holder's fullname:  ")

def account_type_menu():
    print("===Select the Account type===")
    print("1. Savings Account")
    print("2. Current Account")

while True:
    account_type_menu()

    #Exception handling uses try-except block
    try:
        selected_account_type = int(input())
    except Exception:
        print("Invalid input!!! Please try again")
        continue

    if selected_account_type == 1:
        account_type = "Savings"
        break
    elif selected_account_type == 2:
        account_type = "Current"
        break
    else:
        print("You have entered an invalid option. Please try again")

acc = Account(account_number, account_holder_name, account_type)

acc.display_account()