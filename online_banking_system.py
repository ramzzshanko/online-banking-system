# Our main Object is an Account
# An account is described by: account number, account holder name, account type, balance
# Operations that can be performed on an account: deposit, withdraw, check balance, transfer funds

class Account:

    bank_charge = 0.50  # Class variable representing a fixed bank charge
    number_of_accounts = 0

    # This function initializes the account with given details
    # The __init__ method is called or executed when the object is created from the class
    def __init__(self, account_number, account_holder_name, account_type):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = 20.0 # Initial balance set to $20.00
        Account.number_of_accounts += 1
        print("Account created successfully!")

    # This function displays the current state of the account
    def display_account(self):
        print("======Account Details======")
        print("Account Number:", self.account_number)
        print("Account Holder Name:", self.account_holder_name)
        print("Account Type:", self.account_type)
        print("Balance: $", self.balance)
        print("===========================")

    # This function allows depositing money into the account
    # The deposit method takes an amount as input and adds it to the balance
    def deposit(self, amount):
        if amount > 0:            
            self.balance += amount # self.balance = self.balance + amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print(f"Deposit amount must be positive. The balance is still ${self.balance}.")

    # This function allows withdrawing money from the account
    # The withdraw method takes an amount as input and subtracts it from the balance 
    # Withdraws attracts a fee of $0.50 plus 2% of the amount withdrawn
    def withdraw(self, amount):
        if amount <= self.balance:
            total_amount = amount + Account.bank_charge + (amount * 0.02) # Adding withdrawal fee of $0.50 plus 2% of the amount withdrawn
            self.balance -= total_amount # self.balance = self.balance - total_amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print(f"Insufficient funds. The balance is still ${self.balance}.")

    # This function returns the current balance of the account
    def check_balance(self):
        # There is a charge of $0.50 for checking balance
        self.balance -= Account.bank_charge
        print(f"Current balance is ${self.balance}.")

    # Static method to display the number of accounts opened
    @staticmethod
    def get_number_of_accounts():
        print(f"There are {Account.number_of_accounts} accounts opened.")

    # This function transfers funds from one account to another
    def transfer_funds(self, target_account, amount):
        transfer_charge = 0.03 * amount  # 3% transfer fee
        total_deduction = amount + transfer_charge
        if total_deduction <= self.balance:            
            self.balance -= total_deduction
            target_account.balance += amount
            print(f"Transferred ${amount} to account {target_account.account_number}. New balance is ${self.balance}.")
        else:
            print(f"Insufficient funds to transfer. The balance is still ${self.balance}.")


# # Let's create an instance of the Account class and display its details
# account1 = Account("100001", "John Doe", "Savings")
# account1.display_account()

# # Let's deposit some money into the account
# account1.deposit(40.0)
# # Display account details again to see the updated balance
# account1.display_account()

# # Let's withdraw some money from the account
# account1.withdraw(30.0)
# # Display account details again to see the updated balance
# account1.display_account()

# # Let's check the current balance
# account1.check_balance()


# faith_account = Account("100002", "Faith John", "Current")

# faith_account.display_account()

# faith_account.check_balance()

# faith_account.withdraw(10)

# faith_account.display_account()

# print(Account.number_of_accounts)

# Account.get_number_of_accounts()