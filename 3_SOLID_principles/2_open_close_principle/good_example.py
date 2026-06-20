from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} through UPI")

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} through credit card")

class NetBankingPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} through net banking.")

class ProcessPayment:
    def process_payment(self, amount:int,method:PaymentMethod):
        method.pay(amount)

credit_card = CreditCardPayment()
net_banking = NetBankingPayment()
process_payment = ProcessPayment()
process_payment.process_payment(5000, net_banking) # We can see in this if we want to add a new payment method then we can create another class, so we dont need to modify the existing code we are just extending it.
