# In this we will see how can we make the attributes and methods private. To make a method or an attribute private we can add double underscore(__) before their name.
class Bank:
    def __init__(self, name: str, balance: int):
        self.name: str = name
        # Private attribute
        self.__balance: int = balance

    # Getter
    def get_balance(self): # getter, used to fetch the values of private attributes
        print(f"Current balance = {self.__balance}")

    # Setter
    def set_balance(self, new_amount):
        self.__balance = new_amount

    def __isServerLive(self):
        return True

    def deposit(self, amount: int):
        if self.__isServerLive() == True: # We can accessing a private method within the class
            self.__balance += amount
            print(f"Amount deposited, current balance = {self.__balance}\n")
        else:
            print("Server is down")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enought money in bank\n")
        else:
            self.__balance -= amount
            print(f"Amount withdrawn, current balance = {self.__balance}\n")


acc = Bank("Anirudh", 1000)
acc.deposit(1000)
acc.get_balance()
acc.withdraw(500)
acc.__isServerLive() # as this is a private method we can't access it through the object. We can only access it within the class.