import gameMechanics
from player import Player

#isInt = True
#nOfPlayers = input("How many players will there be? ")

# checks if checkValue is an integer
def checkIfIsInt(checkValue):
    try:
        int(checkValue)
    except ValueError:
        return False

    else:
        return True

def getInt(message, min, max):
    output = input(message)

    while checkIfIsInt(output) == False:
       output = getInt("Not a number, please try again: ", min, max)

    output = int(output)
    while output > max or output < min:
        output = getInt("Number is out of bounds, please put a number between",
                        + min + " and " + max + ": ", min, max)

    return output


nOfPlayers = getInt("How many players will there be? ", 2, 4)

ordinalNums = ["1st", "2nd", "3rd", "4th", "5th"]
colors = ["red", "green", "blue", "yellow", "purple"]

players = []

for i in range(nOfPlayers):
    name = input("What is the " + ordinalNums[i] + " player's name? ")
    players.append(Player(name, colors[i]))


gameMechanics.play(players)