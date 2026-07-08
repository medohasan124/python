from abc import ABC , abstractmethod

class Vehicle(ABC):
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    @abstractmethod
    def move(self):
        print(f"{self.brand} is moving at {self.speed} km/h")

class Car(Vehicle):
    def __init__(self, brand, speed , doors_count):
        super().__init__(brand, speed)
        self.doors_count = doors_count
    
    def move(self):
        super().move()
        print(f"It has {self.doors_count} doors")

class Motorcycle(Vehicle):
    def __init__(self, brand, speed , has_side_car):
        super().__init__(brand, speed)
        self.has_side_car = has_side_car

    def move(self):
        super().move()
        print(f"Has side car: {self.has_side_car}")


car = Car("Toyota", 120, 4)
moto = Motorcycle("Harley", 100, False)

car.move()
print("---")
moto.move()


class bmw(Car):
    def __init__(self, brand, speed, doors_count , color):
        super().__init__(brand, speed, doors_count)
        self.color = color
    
    def move(self):
        super().move()
        print(f"my color is {self.color}")

my_bmw = bmw("bmw", 120, 4,"black")

my_bmw.move()
