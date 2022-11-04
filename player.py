class Player:
    def __init__(self, name):
        self.name = name

        self.isDead = False

        self.stats = {
            "money": 50,
            "resources": 50,
            "population": 50,
            "happiness": 50
        }

    # adds to a stat. addValue can be negative. stat is a string ("money"/"resources"/"population"/"happiness").
    def addToStat(self, addValue, stat):
        self.stats[stat] += addValue
        if self.stats[stat] > 100:
            self.stats[stat] = 100

        elif self.stats[stat] <= 0:
            self.isDead = True
