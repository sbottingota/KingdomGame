class Player:
    def __init__(self, name, color, colorCode):
        self.name = name
        self.color = color
        self.colorCode = colorCode

        self.isDead = False

        self.stats = {
            "money": 50,
            "resources": 50,
            "population": 50,
            "happiness": 50
        }

    # adds to a stat. addValue can be negative. stat is a string ("money"/"resources"/"population"/"happiness").
    def addToStat(self, addValue, stat):
        if str(addValue)[0] != "-":
            print(stat, " +", addValue, " to ", self.name, sep="")

        else:
            print(stat, addValue, "from", self.name)

        self.stats[stat] += addValue
        if self.stats[stat] > 100:
            self.stats[stat] = 100
            self.hasWon = True

        elif self.stats[stat] <=0:
            self.stats[stat] = 0
            self.isDead = True