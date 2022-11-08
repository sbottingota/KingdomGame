import matplotlib.pyplot as plt

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

        self.isDead = False
        self.hasWon = False

        self.stats = {
            "money": 50,
            "resources": 50,
            "population": 50,
            "happiness": 50
        }



        #self.bars = plt.bar(["money", "resources", "population", "happiness"], [50, 50, 50, 50])

        #self.barChart =
        #self.barChart.show()
        #plt.show()

    # adds to a stat. addValue can be negative. stat is a string ("money"/"resources"/"population"/"happiness").
    def addToStat(self, addValue, stat):
        self.stats[stat] += addValue
        if self.stats[stat] > 100:
            self.stats[stat] = 100
            self.hasWon = True

        elif self.stats[stat] <=0:
            self.stats[stat] = 0
            self.isDead = True

    def updateBarChart(self):
        for stat in self.stats:
            plt.bar([stat],
                [self.stats[stat]],
                color=self.color)

        #for bar in bars:

        #    print(bar.get_height())