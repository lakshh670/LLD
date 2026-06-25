from holi import Holi
from diwali import Diwali
from discount_service import DiscountService

holi = Holi()
diwali = Diwali()
ds=DiscountService(holi)
ds.process()