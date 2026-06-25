from waiter import Waiter
from pizza import Pizza
from chef import Chef
from burger import Burger
wt=Waiter()
chef=Chef()

wt.take_order(Burger(chef))