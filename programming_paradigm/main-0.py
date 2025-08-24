from bank_account import BankAccount

# Create a bank account
my_account = BankAccount("00123456789", "Sifen Tesfaye", 1000.0)

# Display initial balance
my_account.display_balance()

# Deposit money
my_account.deposit(500.0)

# Withdraw money
my_account.withdraw(200.0)

# Try to withdraw more than available
my_account.withdraw(2000.0)

# Display final balance
my_account.display_balance()
