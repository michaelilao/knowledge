from Reservation import Reservation
from datetime import date


class ReservationSystem():
    _instance = None

    def __init__(self):
        if ReservationSystem._instance is not None:
            raise Exception("Class is singleton")
        else:
            ReservationSystem._instance = self
            self.reservations = []

    def get_instance():
        if ReservationSystem._instance is None:
            ReservationSystem()
        return ReservationSystem._instance

    def isCarAvailable(self, carId, startDate, endDate) -> bool:

        # get all reservations for a car
        reservationsByCarId = filter(
            lambda c: c.id == carId, self.reservations)

        for res in reservationsByCarId:
            if startDate <= res.endDate and endDate >= res.startDate:
                return False

        return True

    def createReservation(self, carId: int, startDate: date, endDate: date, customer, price) -> Reservation:

        reservation = Reservation(carId, startDate, endDate, customer, price)
        self.reservations.append(reservation)
        return reservation
