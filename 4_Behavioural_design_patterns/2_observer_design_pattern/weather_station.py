from observer import Observer
from typing import List

class WeatherStation:
    def __init__(self):
        self.__temperature = 0
        self.__observers: List[Observer] = []

    def add_observer(self, observer: Observer):
        self.__observers.append(observer)
    def remove_observer(self, observer: Observer):
        self.__observers.remove(observer)
    def update_temp(self, temp: float):
        self.__temperature = temp
        for observer in self.__observers:
            observer.update_temp(self.__temperature)
            