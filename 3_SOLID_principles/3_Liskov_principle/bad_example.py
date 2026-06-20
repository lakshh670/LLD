# L - Liskov Substitution Principle (LSP)

# Definition: It states that objects of a parent class should be replaceable with
# objects of a child class without breaking the program.

# Simple terms:
# If Child class is-a Parent class, then Child should work exactly like Parent
# • You should be able to use Child class wherever Parent class is expected
# Child class should not break the behavior that Parent class promises
# No class should be forced to implement methods it doesn't use.
# Split large interfaces into smaller, more specific ones.

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

