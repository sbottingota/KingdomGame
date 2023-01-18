import random
import json

import matplotlib.pyplot as plt

import utils


# returns if the question needs to be presented to the next person
def parseAnswerConsequences(actions, currentPlayer, players):
    if actions == "n":
        return True

    elif actions == "w":
        wageWar(currentPlayer, random.choice(players))
        return False

    for stat in actions:
        # take from each player
        if actions[stat][0] == "p":
            addValue = int(actions[stat][1:])

            currentPlayer.addToStat(len(players) * addValue, stat)

            for player in players:
                if currentPlayer != player and player.isDead == False:
                    player.addToStat(-addValue, stat)


        # add or subtract
        else:
            currentPlayer.addToStat(int(actions[stat]), stat)

    return False


def wageWar(side1, side2):
    for side in (side1, side2):
        print(side.colorCode)
        armyPopulation = utils.getInt(side.name +
                ", how many people would you like to subscript to the army? (Max 50% of you population)",
                                      1, side.stats["population"] // 2)

        armyFunding = utils.getInt(side.name +
                                   ", how much funding (money & resources) would you like to give the army?"
                                   " (Max 50% of the lowest stat out of the two)",
                                   1, min(side.stats["money"], side.stats["resources"]) // 2)
        parseAnswerConsequences({
            "money": str(-armyFunding),
            "resources": str(-armyFunding),
            "population": str(-armyPopulation)
        }, side, (side1, side2))



def getRandomQuestionSet():
    with open("questions.json", "r") as questions:
        return random.choice(json.load(questions))


def updateBarChart(players):
    nRows = 2 if len(players) > 3 else 1

    for player in players:
        plt.subplot(round(len(players) / nRows), nRows, players.index(player) + 1)
        plt.cla()
        plt.barh(tuple(player.stats.keys()), player.stats.values(), color=player.color)
        plt.xlim(0, 100)

    plt.pause(0.01)


def play(players):
    questionSet = prevQuestionSet = {"question": None}
    needsToRepeatQuestion = False

    playerIndex = 0

    updateBarChart(players)

    plt.ion()

    while True:
        plt.cla()

        # current player
        currentPlayer = players[playerIndex]

        # player color
        print(currentPlayer.colorCode)

        # check if the player is alive
        if currentPlayer.isDead:
            print(currentPlayer.name, "is dead and can't play :(")
            playerIndex += 1
            continue


        else:
            currentPlayerHasWon = True
            for player in players:
                if player == currentPlayer:
                    continue

                elif not player.isDead:
                    currentPlayerHasWon = False
                    break

            if currentPlayerHasWon:
                print(currentPlayer.name, "has won :)")
                break

        # TODO: add ties.

        # preventing duplicates
        if not needsToRepeatQuestion:
            while questionSet["question"] == prevQuestionSet["question"]:
                questionSet = getRandomQuestionSet()

        input("Press enter to continue, " + currentPlayer.name)  # wait for user to press enter

        print(questionSet["question"])

        answerIsYes = utils.getBinaryInput()

        # TODO: find a more concise way of doing this
        if answerIsYes:
            if not needsToRepeatQuestion:
                needsToRepeatQuestion = parseAnswerConsequences(questionSet["yes"], currentPlayer, players)
            else:
                needsToRepeatQuestion = False
                parseAnswerConsequences(questionSet["yes"], currentPlayer, players)

            print("\n", questionSet["yes"])

        else:
            if not needsToRepeatQuestion:
                needsToRepeatQuestion = parseAnswerConsequences(questionSet["no"], currentPlayer, players)

            else:
                needsToRepeatQuestion = False
                parseAnswerConsequences(questionSet["no"], currentPlayer, players)
            parseAnswerConsequences(questionSet["no"], currentPlayer, players)

            print("\n", questionSet["no"])

        print("\n" * 3)  # whitespace

        prevQuestionSet = questionSet  # previous question set, to avoid duplicates

        playerIndex += 1
        if playerIndex == len(players):
            playerIndex = 0

        # this works better when you run it multiple times. idk why though.
        # TODO: find how to make this work while running it only once.
        for i in range(3):
            updateBarChart(players)

        print(utils.RESET)
