from abc import ABC,abstractmethod
from typing import List
class AirTrafficControl(ABC):
    @abstractmethod
    def register_airplane(self):
        pass
    @abstractmethod
    def send_message(self):
        pass


class ControlTower(AirTrafficControl):
    def __init__(self):
        self.__airplanes:List[Airplane]=[]
    def register_airplane(self,plane:"Airplane"):
        self.__airplanes.append(plane)
    def send_message(self,source:"Airplane",message:str):
        for plane in self.__airplanes:
            if plane!=source:
                plane.receive_message(message,source)



class Airplane():
    def __init__(self, flight_number:str,tower:ControlTower):
        self.__flight_number:str = flight_number
        self.__tower:ControlTower = tower
        self.__tower.register_airplane(self)


    def get_flight_number(self):
        return self.__flight_number

    def receive_message(self,message:str,source:"Airplane"):
        print(f"{self.__flight_number} recieved message: {message}\n from {source.get_flight_number()}")

tower=ControlTower()
indigo=Airplane("indigo123",tower)
spicejet=Airplane("spicejet123",tower)
tower.send_message(spicejet,"We are about to land.")
