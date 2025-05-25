import random
from Coin import Coin
from Player import Player


class CoinGame:
    def __init__(self, ):
        p1 = Player('Player 1')
        p2 = Player('Player 2')
        self.players = [p1, p2]
        self.coin = Coin()

    def startGame(self):
        # Chose player to predict
        chosenPlayerInt = random.randint(0, 1)
        otherPlayerInt = int(not chosenPlayerInt)

        chosenPlayer = self.players[chosenPlayerInt]
        otherPlayer = self.players[otherPlayerInt]

        # Get prediction from Player
        prediction = chosenPlayer.getRandCoinOption()

        # Set other Player to opposite side
        if prediction == "heads":
            otherPlayer.setCoinOption("tails")
        else:
            otherPlayer.setCoinOption("heads")

        # Flip coin and get result
        result = self.coin.getCoinOption()

        # Check player results
        chosenPlayer.didPlayerWin(result)
        otherPlayer.didPlayerWin(result)


if __name__ == "__main__":
    coinGame = CoinGame()
    coinGame.startGame()
