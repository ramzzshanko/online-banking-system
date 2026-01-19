Here's an interactive version with a menu-driven interface:

```python
class Account:
    bank_charge = 0.50  # Class variable representing a fixed bank charge
    number_of_accounts = 0

    def __init__(self, account_number, account_holder_name, account_type):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = 20.0  # Initial balance set to $20.00
        Account.number_of_accounts += 1
        print(f"Account created successfully for {account_holder_name}!")

    def display_account(self):
        print("\n" + "="*40)
        print("ACCOUNT DETAILS")
        print("="*40)
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: ${self.balance:.2f}")
        print("="*40)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\n✓ Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
            return True
        else:
            print(f"\n✗ Deposit amount must be positive.")
            return False

    def withdraw(self, amount):
        fee = Account.bank_charge + (amount * 0.02)
        total_deduction = amount + fee
        
        if amount > 0 and total_deduction <= self.balance:
            self.balance -= total_deduction
            print(f"\n✓ Withdrew ${amount:.2f}.")
            print(f"  Fee: ${fee:.2f} ($0.50 + 2% of ${amount:.2f})")
            print(f"  New balance: ${self.balance:.2f}")
            return True
        elif amount <= 0:
            print(f"\n✗ Withdrawal amount must be positive.")
            return False
        else:
            print(f"\n✗ Insufficient funds.")
            print(f"  Required: ${total_deduction:.2f} (including ${fee:.2f} fee)")
            print(f"  Available: ${self.balance:.2f}")
            return False

    def check_balance(self):
        if self.balance >= Account.bank_charge:
            self.balance -= Account.bank_charge
            print(f"\nCurrent balance: ${self.balance:.2f}")
            print(f"Note: $0.50 charge applied for balance inquiry")
            return True
        else:
            print(f"\n✗ Insufficient funds for balance inquiry.")
            print(f"  Required: ${Account.bank_charge:.2f}")
            print(f"  Available: ${self.balance:.2f}")
            return False

    def transfer_funds(self, target_account, amount):
        if amount <= 0:
            print(f"\n✗ Transfer amount must be positive.")
            return False
            
        if amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            print(f"\n✓ Transferred ${amount:.2f} to {target_account.account_holder_name}")
            print(f"  Your new balance: ${self.balance:.2f}")
            return True
        else:
            print(f"\n✗ Insufficient funds for transfer.")
            print(f"  Required: ${amount:.2f}")
            print(f"  Available: ${self.balance:.2f}")
            return False

    @staticmethod
    def get_number_of_accounts():
        print(f"\nTotal accounts opened: {Account.number_of_accounts}")


def find_account_by_number(accounts, account_number):
    for account in accounts:
        if account.account_number == account_number:
            return account
    return None


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


def main():
    accounts = []
    current_account = None
    
    # Create some sample accounts
    sample_accounts = [
        ("100001", "John Doe", "Savings"),
        ("100002", "Jane Smith", "Checking"),
        ("100003", "Bob Johnson", "Savings")
    ]
    
    for acc_num, holder, acc_type in sample_accounts:
        accounts.append(Account(acc_num, holder, acc_type))
    
    while True:
        display_main_menu()
        
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":  # Create New Account
                print("\n" + "="*30)
                print("CREATE NEW ACCOUNT")
                print("="*30)
                
                while True:
                    acc_num = input("Enter account number: ").strip()
                    if find_account_by_number(accounts, acc_num):
                        print("✗ Account number already exists. Try again.")
                    else:
                        break
                
                holder_name = input("Enter account holder name: ").strip()
                
                print("\nAccount Types:")
                print("1. Savings")
                print("2. Checking")
                acc_type_choice = input("Select account type (1-2): ").strip()
                acc_type = "Savings" if acc_type_choice == "1" else "Checking"
                
                new_account = Account(acc_num, holder_name, acc_type)
                accounts.append(new_account)
                current_account = new_account
                
                # Go directly to account menu after creation
                while current_account:
                    display_account_menu(current_account.account_holder_name)
                    acc_choice = input("\nEnter your choice (1-6): ").strip()
                    
                    if acc_choice == "1":  # Deposit
                        try:
                            amount = float(input("Enter amount to deposit: $"))
                            current_account.deposit(amount)
                        except ValueError:
                            print("✗ Invalid amount. Please enter a valid number.")
                    
                    elif acc_choice == "2":  # Withdraw
                        try:
                            amount = float(input("Enter amount to withdraw: $"))
                            current_account.withdraw(amount)
                        except ValueError:
                            print("✗ Invalid amount. Please enter a valid number.")
                    
                    elif acc_choice == "3":  # Check Balance
                        current_account.check_balance()
                    
                    elif acc_choice == "4":  # Transfer Funds
                        if len(accounts) < 2:
                            print("\n✗ No other accounts available for transfer.")
                            continue
                        
                        print("\nAvailable accounts for transfer:")
                        for acc in accounts:
                            if acc.account_number != current_account.account_number:
                                print(f"  {acc.account_number}: {acc.account_holder_name}")
                        
                        target_num = input("\nEnter target account number: ").strip()
                        target_account = find_account_by_number(accounts, target_num)
                        
                        if target_account and target_account != current_account:
                            try:
                                amount = float(input("Enter amount to transfer: $"))
                                current_account.transfer_funds(target_account, amount)
                            except ValueError:
                                print("✗ Invalid amount. Please enter a valid number.")
                        else:
                            print("✗ Invalid target account.")
                    
                    elif acc_choice == "5":  # View Account Details
                        current_account.display_account()
                    
                    elif acc_choice == "6":  # Return to Main Menu
                        current_account = None
                        print("\nReturning to main menu...")
                    
                    else:
                        print("✗ Invalid choice. Please enter 1-6.")
            
            elif choice == "2":  # Select Account
                if not accounts:
                    print("\n✗ No accounts exist. Please create an account first.")
                    continue
                
                print("\nAvailable Accounts:")
                for account in accounts:
                    print(f"  {account.account_number}: {account.account_holder_name}")
                
                acc_num = input("\nEnter account number to select: ").strip()
                current_account = find_account_by_number(accounts, acc_num)
                
                if current_account:
                    print(f"\n✓ Selected account: {current_account.account_holder_name}")
                    
                    # Account operations menu
                    while current_account:
                        display_account_menu(current_account.account_holder_name)
                        acc_choice = input("\nEnter your choice (1-6): ").strip()
                        
                        if acc_choice == "1":  # Deposit
                            try:
                                amount = float(input("Enter amount to deposit: $"))
                                current_account.deposit(amount)
                            except ValueError:
                                print("✗ Invalid amount. Please enter a valid number.")
                        
                        elif acc_choice == "2":  # Withdraw
                            try:
                                amount = float(input("Enter amount to withdraw: $"))
                                current_account.withdraw(amount)
                            except ValueError:
                                print("✗ Invalid amount. Please enter a valid number.")
                        
                        elif acc_choice == "3":  # Check Balance
                            current_account.check_balance()
                        
                        elif acc_choice == "4":  # Transfer Funds
                            if len(accounts) < 2:
                                print("\n✗ No other accounts available for transfer.")
                                continue
                            
                            print("\nAvailable accounts for transfer:")
                            for acc in accounts:
                                if acc.account_number != current_account.account_number:
                                    print(f"  {acc.account_number}: {acc.account_holder_name}")
                            
                            target_num = input("\nEnter target account number: ").strip()
                            target_account = find_account_by_number(accounts, target_num)
                            
                            if target_account and target_account != current_account:
                                try:
                                    amount = float(input("Enter amount to transfer: $"))
                                    current_account.transfer_funds(target_account, amount)
                                except ValueError:
                                    print("✗ Invalid amount. Please enter a valid number.")
                            else:
                                print("✗ Invalid target account.")
                        
                        elif acc_choice == "5":  # View Account Details
                            current_account.display_account()
                        
                        elif acc_choice == "6":  # Return to Main Menu
                            current_account = None
                            print("\nReturning to main menu...")
                        
                        else:
                            print("✗ Invalid choice. Please enter 1-6.")
                else:
                    print("✗ Account not found.")
            
            elif choice == "3":  # View All Accounts
                if not accounts:
                    print("\n✗ No accounts exist.")
                else:
                    print(f"\n{'='*60}")
                    print(f"{'ALL ACCOUNTS':^60}")
                    print(f"{'='*60}")
                    for account in accounts:
                        account.display_account()
            
            elif choice == "4":  # Display Total Accounts
                Account.get_number_of_accounts()
            
            elif choice == "5":  # Exit
                print("\n" + "="*50)
                print("Thank you for using the Bank Management System!")
                print("="*50)
                break
            
            else:
                print("✗ Invalid choice. Please enter 1-5.")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"\n✗ An error occurred: {e}")


if __name__ == "__main__":
    main()
```

This interactive version includes:

## **Features:**
1. **Main Menu** with options to:
   - Create new accounts
   - Select existing accounts
   - View all accounts
   - Display total number of accounts
   - Exit the system

2. **Account Menu** (when an account is selected) with options to:
   - Deposit money
   - Withdraw money (with automatic fee calculation)
   - Check balance (with $0.50 charge)
   - Transfer funds to other accounts
   - View account details
   - Return to main menu

3. **Sample Data**: Three pre-created accounts for testing

4. **Error Handling**: 
   - Invalid input validation
   - Insufficient funds checks
   - Duplicate account number prevention
   - Float amount validation

5. **User-Friendly Interface**:
   - Clear menu displays
   - Success/failure messages
   - Formatted output with borders
   - Current account tracking

## **How to Use:**
1. Run the program
2. Use option 1 to create a new account (you'll be taken directly to that account's menu)
3. Use option 2 to select an existing account from the list
4. Perform operations on the selected account
5. Return to main menu when done with an account

The system maintains a list of all accounts and allows transfers between them. All charges (withdrawal fee and balance inquiry fee) are automatically applied as specified in your original code.