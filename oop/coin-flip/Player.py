import random


class Player:
    def __init__(self, name):
        self.name = name
        self.coinOption = ""

    def setCoinOption(self, coinOption):
        self.coinOption = coinOption

    def getCoinOption(self):
        return self.coinOption

    def getRandCoinOption(self):
        option = "heads"
        if random.randint(0, 1) == 1:
            option = "tails"

        self.setCoinOption(option)
        print(self.name + " chose " + option)
        return option

    def didPlayerWin(self, winningFlip):
        if winningFlip == self.getCoinOption():
            print(self.name + " won!")
            return True
        else:
            print(self.name + " lost!")
            return False
