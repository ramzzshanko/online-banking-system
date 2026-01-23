class Account: # This is a class definition for Account
        
        number_of_accounts = 0  # Class variable to keep track of number of accounts

        def __init__(self, account_name): # Constructor method to initialize account object
            self.account_name = account_name
            print(self.account_name)

            if account_name == "John Doe":
                print("Welcome back, John!")
            else:
                            print("Welcome, new account holder!")
                            print("Account created successfully.")

        if number_of_accounts == 0:
            number_of_accounts += 1
            print(f"We have added a placeholder account.")
        

        def diplay_account(self):
            print(f"Account Name: {self.account_name}")


object1 = Account("John Doe")