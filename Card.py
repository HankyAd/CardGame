class Card:
    maxHealth = 0
    health = 0
    played = False

    def __init__(self, maxhlth):
        self.maxHealth = maxhlth
        self.health = self.maxHealth

    def getHealth(self):
        return self.health

    def applyDmg(self, dmg):
        self.health -= dmg

    def setPlayed(self):
        self.played = True

