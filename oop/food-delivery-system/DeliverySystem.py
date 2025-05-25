from typing import List

from Restaurant import Restaurant
from OrderService import OrderService


class DeliverySystem():
    _instance = None

    def __init__(self):
        if DeliverySystem._instance is not None:
            raise Exception("Class is singleton")
        else:
            DeliverySystem._instance = self
            self.restaurants: List[Restaurant] = []
            self.orderService = OrderService()

    def GetInstance():
        if DeliverySystem._instance is None:
            DeliverySystem()
        return DeliverySystem._instance

    def AddRestaurant(self, restaurant: Restaurant):
        self.restaurants.append(restaurant)

    def GetOpenRestaurants(self) -> List[Restaurant]:
        openRestaurants = []

        for rest in self.restaurants:
            if rest.isOpen():
                openRestaurants.append(rest)

        return openRestaurants
