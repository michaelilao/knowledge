class User():
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone
        self.type = ""

    def __repr__(self):
        return f"{self.type} - {self.name}"

    def __str__(self):
        return self.__repr__()


class Customer(User):
    def __init__(self, name: str, email: str, phone: str):
        super().__init__(name, email, phone)
        self.type = "Customer"


class DeliveryAgent(User):
    def __init__(self, name: str, email: str, phone: str):
        super().__init__(name, email, phone)
        self.type = "Delivery Agent"


class RestaurantAdmin(User):
    def __init__(self, name: str, email: str, phone: str):
        super().__init__(name, email, phone)
        self.type = "Restaurant Admin"
