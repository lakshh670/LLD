


from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self,amount):
        self.balance = amount
    @abstractmethod
    def deposit(self,amount):
        pass

class WithdrawableAccount(BankAccount):
    @abstractmethod
    def withdraw(self,amount):
        pass

class SavingsAccount(WithdrawableAccount):
    def __init__(self,amount):
        super().__init__(amount)
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("You cannot withdraw more than you have")
            return
        self.balance -= amount
        print(f"Amount withdrawn. New balance: {self.balance}")

class FixedDepositAccount(BankAccount):
    def __init__(self,amount):
        super().__init__(amount)
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited. New balance: {self.balance}")

acc1=SavingsAccount(5000)
acc2=FixedDepositAccount(5000)
acc1.deposit(5000)
acc2.deposit(5000)
acc1.withdraw(2500)