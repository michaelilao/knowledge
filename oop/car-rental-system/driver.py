from datetime import date
from RentalSystem import RentalSystem
from Car import Car, CarMake, CarType
from Customer import Customer
rs = RentalSystem()
mazda3 = Car(CarMake.Mazda, CarType.Sedan, "AFEA044", 99)
fordEscape = Car(CarMake.Ford, CarType.SUV, "BCED041", 50)

michael = Customer("Michael Ilao", "michaelilao@live.com")

rs.addCar(mazda3)
rs.addCar(fordEscape)


# Get available Cars
startDate = date(2025, 1, 1)
endDate = date(2025, 2, 1)
availableCars = rs.searchCars(
    startDate, endDate, CarMake.Ford, CarType.Sedan, 0, 200)
car = availableCars[0]


reservation = rs.createReservation(car.id, startDate, endDate, michael)
