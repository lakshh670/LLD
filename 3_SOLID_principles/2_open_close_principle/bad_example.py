
# Open Close Principle (OCP)

# Definition: Software entities (classes, modules, functions) should be open for
# extension but closed for modification.

# Simple terms:
# Open for extension = You can add new features easily
# Closed for modification = Don't change existing working code

# Example: Adding new payment methods (Credit Card, UPI, PayPal)
# without modifying the existing payment processing code.

class PaymentProcessor:
    def pay(self, payment_method: str, amount: int):
        if payment_method == "UPI":
            print(f"Starting UPI transaction of Rs.{amount}")
            print("UPI transaction finished")
        elif payment_method == "credit_card":
            print(f"Starting credit card transaction of Rs.{amount}")
            print("Credit card transaction finished")
        elif payment_method == "net_banking":
            print(f"Starting net banking transaction of Rs.{amount}")
            print("Net Banking transaction finished")


pay_p = PaymentProcessor()
pay_p.pay("credit_card", 500) # Now in future if you want to add a new payment method then you need to modify existing payment class
