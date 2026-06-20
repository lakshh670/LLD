# I - Interface Segregation Principle

# Definition: The Interface Segregation Principle ensures that classes are not forced
# to implement methods they don't need.

# Simple terms:
# • Break large, general-purpose interfaces into smaller, more specific ones.

# Benefits:
# Maintainability - Code is easier to maintain and update
# Flexibility - Classes can pick and choose what they need
# Testability - Easier to test because classes have only

# what they need
# Key Rule: Classes should only depend on the methods
# they actually use.

from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self,amount):
        self.balance = amount
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
class SavingsAccount(BankAccount):
    def __init__(self,amount):
        super().__init__(amount)
    def deposit(self,amount):
        self.balance+=amount
        print(f"Amount deposited. New balance: {self.balance}")
    def withdraw(self,amount):
        if amount > self.balance:
            print("You cannot withdraw more than you have")
            return
        self.balance-=amount
        print(f"Amount withdrawn. New balance: {self.balance}")

class FixedDepositAccount(BankAccount):
    def __init__(self,amount):
        super().__init__(amount)
    def deposit(self,amount):
        self.balance+=amount
        print(f"Amount deposited. New balance: {self.balance}")
    def withdraw(self,amount):
        raise Exception("You cannot withdraw from fixed deposit account.")

