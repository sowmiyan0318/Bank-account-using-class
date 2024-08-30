class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

# Create a new bank account
account = BankAccount("123456789", 1000)

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(200)

# Check balance
account.check_balance()
