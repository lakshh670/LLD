from location import Location
from vehicle import Vehicle

class Driver:
    def __init__(self,name:str,location:Location,vehicle:Vehicle):
        self.name = name
        self.vehicle = vehicle
        self.location = location
        self.is_booked = False