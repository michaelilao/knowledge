class Item():
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __repr__(self):
        return self.name + " $" + str(self.price)

    def __str__(self):
        return self.__repr__()
