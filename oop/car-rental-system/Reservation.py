class Reservation():
    def __init__(self, carId, startDate, endDate, customer, price):
        self.carId = carId
        self.startDate = startDate
        self.endDate = endDate
        self.id = hash(str(carId) + str(startDate) + str(endDate))
        self.customer = customer
        self.price = price

    def changeReservation(self, startDate, endDate):
        self.startDate = startDate
        self.endDate = endDate
