from enum import Enum
from typing import List
from User import User

from OperatingHours import OperatingHours
from Menu import Menu
from Item import Item


class RestaurantType(Enum):
    CHINESE = 1
    INDIAN = 2
    MEXICAN = 3
    GREEK = 4


class Restaurant(User):
    def __init__(self, name: str, restrauntType: RestaurantType, phone: str):
        email = "restaurant" + "@"+name+".com"
        super().__init__(name, email, phone)
        self.restrauntType = restrauntType
        self.menu = Menu()
        self.operatingHours: List[OperatingHours] = []

    def AddItem(self, item: Item):
        self.menu.AddItemToMenu(item)

    def SetOperatingHourse(self, day: int, openTime: int, closeTime: int):
        newHours = OperatingHours(day, openTime, closeTime)
        # Check if conflict/already exists, if so update it
        self.operatingHours.append(newHours)

    def isOpen(self) -> bool:
        # Check if time right now is within operating hours
        return True

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()
