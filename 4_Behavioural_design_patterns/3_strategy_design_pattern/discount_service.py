from discount_strategy import DiscountStrategy
class DiscountService():
    def __init__(self,discount_strategy:DiscountStrategy):
        self.__strategy = discount_strategy

    def change_type(self,discount_strategy:DiscountStrategy):
        self.__strategy = discount_strategy
    def process(self):
        self.__strategy.apply_discount()