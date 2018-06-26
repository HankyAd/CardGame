import random
from Card import Card
from Player import Player


class Game:
    noOfPlayers = 0
    deck = []
    gameOver = False
    round = 0

    def __init__(self):
        players = []
        self.noOfPlayers = int(input("Number of Players? (Game requires 2 or more players): "))
        for i in range(self.noOfPlayers):
            player = Player(i)
            players.append(player)

        self.initDeck()

        for i in range(len(self.deck)):
            print(self.deck[i].health)

        print("Dealing Cards")

        while not (self.gameOver or self.round == 9):
            print("Round" + str(self.round))
            for i in range(self.noOfPlayers):
                print(players[i].playerName + "'s turn")
            self.round += 1

    def initDeck(self):
        for i in range(self.noOfPlayers * 10):
            if i < self.noOfPlayers * 7:
                card = Card(random.randint(1, 3))
            else:
                card = Card(random.randint(-3, -1))
            self.deck.append(card)
        random.shuffle(self.deck)


game = Game();
