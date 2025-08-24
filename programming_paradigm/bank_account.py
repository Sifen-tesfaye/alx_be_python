class BankAccount:
    def __init__(self, initial_balance=0):
        # account_balance is private (encapsulation)
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the balance"""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if funds are sufficient"""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Show current balance"""
        print(f"Current Balance: ${self.__account_balance}")
