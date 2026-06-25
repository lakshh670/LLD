from mobile_display import MobileDisplay
from tv_display import TVDisplay
from weather_station import WeatherStation

ws=WeatherStation()

mobile=MobileDisplay()
ws.add_observer(mobile)
ws.update_temp(30)
