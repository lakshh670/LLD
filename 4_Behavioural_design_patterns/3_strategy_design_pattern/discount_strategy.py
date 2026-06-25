from abc import ABC, abstractmethod
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self):
        pass