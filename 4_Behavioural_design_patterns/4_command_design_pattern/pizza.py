from order import Order
from chef import Chef
class Pizza(Order):
    def __init__(self,chef:Chef):
        self.__chef = chef

    def execute(self):
        print("Order taken")
        self.__chef.cook_pizza()
