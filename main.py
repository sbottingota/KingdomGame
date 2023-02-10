from utils import *
import gameMechanics
from player import Player

#isInt = True
#nOfPlayers = input("How many players will there be? ")

# checks if checkValue is an integer


nOfPlayers = getInt("How many players will there be? ", 2, 4)

ORDINAL_NUMS = ["1st", "2nd", "3rd", "4th"]

players = []

for i in range(nOfPlayers):
    name = getNotEmptyString("What is the " + ORDINAL_NUMS[i] + " player's name? ")

    players.append(Player(name, COLORS[i], COLOR_CODES[i]))


gameMechanics.play(players)
