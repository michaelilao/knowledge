from typing import List
from Item import Item


class Menu():
    def __init__(self):
        self.items: List[Item] = []

    def AddItemToMenu(self, item: Item):
        # Check if it already exists on menu
        self.items.append(item)

    def RemoveItemFromMenu(self, item):
        pass

    def __repr__(self):
        s = ""
        for item in self.items:
            s += item.__repr__() + "\n"
        return s

    def __str__(self):
        return self.__repr__()
