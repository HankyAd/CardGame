from Card import Card

class Player:
    playerNumber = 0
    hand = []
    boardValue = 0
    playerName = ""


    def __init__(self, playerNo):
        self.playerNumber = playerNo
        self.playerName = input("Player " + str(self.playerNumber+1) + ", Please Enter Your Name:   ")

    def dealCard(self, card):
        self.hand.append(card)

    def getBoardValue(self):
        value = 0
        for i in range (len(self.hand)):
            value += self.hand[i]