from enum import Enum
from typing import List

from Restaurant import Restaurant
from User import User, DeliveryAgent, RestaurantAdmin, Customer
from Item import Item


class OrderStatus(Enum):
    PENDING = 0
    ORDERED = 1
    COOKING = 2
    ENROUTE = 3
    DELIVERED = 4


class Order():
    def __init__(self, restaurant: Restaurant, customer: Customer):
        self.restaurant = restaurant
        self.customer = customer
        self.deliveryAgent = None
        self.items: List[Item] = []
        self.status = OrderStatus.PENDING

    def GetPrice(self) -> int:
        price = 0
        for item in self.items:
            price += item.price

        return price

    def AddItems(self, item: Item):

        # Do a check that the item is from the correct restaurant

        print("Adding " + item.__repr__() + " to order")
        self.items.append(item)

    def SetStatus(self, newStatus: OrderStatus):
        self.status = newStatus

    def __repr__(self):
        return self.customer.__repr__() + " order @ " + self.restaurant.__repr__() + " " + self.status.name
