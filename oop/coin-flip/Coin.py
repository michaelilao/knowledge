import random


class Coin:
    def __init__(self, ):
        self.coinOption = ""

    def setCoinOption(self, option):
        self.coinOption = option

    def getCoinOption(self):
        option = "heads"
        if random.randint(0, 1) == 1:
            option = "tails"

        self.setCoinOption(option)
        print("Coin landed on " + option)
        return option
