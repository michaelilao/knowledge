from enum import Enum


class CarType(Enum):
    All = 0
    SUV = 1
    Sedan = 2
    Truck = 3


class CarMake(Enum):
    All = 0
    Ford = 1
    Mazda = 2
    BMW = 3


class Car():
    def __init__(self, carMake: CarMake, carType: CarType, licensePlate: str, pricePerDay: int):
        self.carMake = carMake
        self.carType = carType
        self.licensePlate = licensePlate
        self.pricePerDay = pricePerDay
        self.id = "CAR" + str(carMake.name)+str(carType.name) + licensePlate


if __name__ == "__main__":
    car = Car(CarMake.Mazda, CarType.Sedan, "AFEA", 499)
