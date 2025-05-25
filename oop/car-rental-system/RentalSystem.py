from Car import Car, CarMake, CarType
from Reservation import Reservation
from ReservationSystem import ReservationSystem
from PaymentProcessor import StripePaymentProcessor
from datetime import date


class RentalSystem():
    _instance = None

    def __init__(self):
        if RentalSystem._instance is not None:
            raise Exception("Class is singleton")
        else:
            RentalSystem._instance = self
            self.cars = []
            self.reservationSys = ReservationSystem()
            self.paymentProc = StripePaymentProcessor()

    def get_instance():
        if RentalSystem._instance is None:
            RentalSystem()
        return RentalSystem._instance

    def addCar(self, car: Car):
        self.cars.append(car)

    def getCar(self, carId) -> Car:
        return next((c for c in self.cars if c.id == carId), None)

    def removeCar(self, carId: int):
        filteredCars = filter(lambda c: c.carId == carId, self.cars)
        self.cars = filteredCars

    def searchCars(self, startDate: date, endDate: date, carMake, carType, priceLow, priceHigh) -> list[Car]:
        return self.cars

    def createReservation(self, carId, startDate: date, endDate: date, customer):
        # Get car
        car = self.getCar(carId)
        if car is None:
            raise Exception("Car does not exist in system")

        if not self.reservationSys.isCarAvailable(carId, startDate, endDate):
            raise Exception("Car is not available")

        price = car.pricePerDay

        if not self.paymentProc.processPayment(price):
            raise Exception("Payment not processed")
        # Ensure car is available
        reservation = self.reservationSys.createReservation(
            carId, startDate, endDate, customer, price)

        return reservation
