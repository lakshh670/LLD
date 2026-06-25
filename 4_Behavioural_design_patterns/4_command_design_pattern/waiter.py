from order import Order
class Waiter:
    def take_order(self,order_type:Order):
        order_type.execute()