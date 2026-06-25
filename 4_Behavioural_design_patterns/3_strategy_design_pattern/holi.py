from discount_strategy import DiscountStrategy
from abc import ABC, abstractmethod
class Holi(DiscountStrategy):

    def apply_discount(self):
        print("Holi discount of 30% has been applied.")
