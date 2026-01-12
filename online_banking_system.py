# Our main Object is an Account
# An account is described by: account number, account holder name, account type, balance
# Operations that can be performed on an account: deposit, withdraw, check balance, transfer funds

class Account:

    # This function initializes the account with given details
    # The __init__ method is called or executed when the object is created from the class
    def __init__(self, account_number, account_holder_name, account_type):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = 20.0 # Initial balance set to $20.00
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
            total_amount = amount + 0.50 + (amount * 0.02) # Adding withdrawal fee of $0.50 plus 2% of the amount withdrawn
            self.balance -= total_amount # self.balance = self.balance - total_amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print(f"Insufficient funds. The balance is still ${self.balance}.")

    # This function returns the current balance of the account
    def check_balance(self):
        # There is a charge of $0.50 for checking balance
        self.balance -= 0.50
        print(f"Current balance is ${self.balance}.")

# Let's create an instance of the Account class and display its details
account1 = Account("100001", "John Doe", "Savings")
account1.display_account()

# Let's deposit some money into the account
account1.deposit(40.0)
# Display account details again to see the updated balance
account1.display_account()

# Let's withdraw some money from the account
account1.withdraw(30.0)
# Display account details again to see the updated balance
account1.display_account()

# Let's check the current balance
account1.check_balance()


