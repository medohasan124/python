
#يمكن اضافه ال class داخل method وكأنه attribute وايضا داخل  list 

from abc import ABC , abstractmethod

class Property(ABC):
    def __init__(self,location,price):
        self.location = location
        self.price = price

    
    def basic_info(self):
        print(f"Location: {self.location} | Price: {self.price}")

    @abstractmethod
    def describe(self):
        pass

class Apartment(Property):
    def __init__(self, location, price,floor_number):
        super().__init__(location, price)
        self.floor_number = floor_number
    
    def describe(self):
        print(f"Apartment on floor {self.floor_number}")

class Villa(Property):
    def __init__(self, location, price,garden_size):
        super().__init__(location, price)
        self.garden_size = garden_size

    def describe(self):
        print(f"Villa with garden size {self.garden_size} sqm")





class PropertyManager:
    def __init__(self):
        self.properties = []

    def add_property(self,prop):
        self.properties.append(prop)

    def show_all(self):
        for x in self.properties:
            x.basic_info()
            x.describe()

manager = PropertyManager()
apt = Apartment("Riyadh", 300000, 5)
villa = Villa("Jeddah", 800000, 400)

manager.add_property(apt)
manager.add_property(villa)

manager.show_all()