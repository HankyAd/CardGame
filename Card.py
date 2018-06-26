class Card:
    maxHealth = 5
    health = 5

    def __init__(self, maxhlth):
        self.maxHealth = maxhlth
        self.health = self.maxHealth

    def getHealth(self):
        return self.health

    def applyDmg(self, dmg):
        self.health -= dmg