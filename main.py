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

ORDINAL_NUMS = ["1st", "2nd", "3rd", "4th"]
COLORS = ["red", "green", "blue", "purple"]

players = []

for i in range(nOfPlayers):
    name = input("What is the " + ORDINAL_NUMS[i] + " player's name? ")
    players.append(Player(name, COLORS[i]))


gameMechanics.play(players)