import random
import json

import matplotlib.pyplot as plt

from utils import *

# returns if the question needs to be presented to the next person
# key:
# n: ask same question to next person (currently not supported)
# p: take stat from the other people
# %: different outcomes based on weights. (e.g. for 2 weights: {weight1}:{weight2},{outcome1}:{outcome2}
# >: have outcomes later as well as now. (e.g.: {# of turns for future action}:{current action},{future action})
# number: just add that number to the stat

def parseAnswerConsequences(consequences, currentPlayer, players):

    if consequences == "n":
        return None

    futureAction = {}

    for stat in consequences:
        # take from each player
        if consequences[stat][0] == "p":
            action = int(consequences[stat][1:])

            currentPlayer.addToStat(len(players) * action, stat)

            for player in players:
                if currentPlayer != player and player.isDead == False:
                    player.addToStat(-action, stat)

        elif consequences[stat][0] == "%":
            weights = consequences[stat][1:].split(",")[0].split(":")
            weights = [int(weights[i]) for i in range(len(weights))]

            actions = consequences[stat][1:].split(",")[1].split(":")
            actions = [int(actions[i]) for i in range(len(actions))]

            action = random.choices(actions, weights=weights)[0] # [0] because random.choices returns a list of choices

            currentPlayer.addToStat(action, stat)

        elif consequences[stat][0] == ">":
            print(consequences[stat][1:].split("|")[0].split(":"))
            nMoves, currentAction = consequences[stat][1:].split("|")[0].split(":")

            futureAction[stat] = (nMoves, consequences[stat][1:].split("|")[1])

            currentPlayer.addToStat(int(currentAction), stat)

        # add or subtract
        else:
            currentPlayer.addToStat(int(consequences[stat]), stat)

    return None if futureAction == {} else futureAction


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

def playerHasWon(currentPlayer, players):
    currentPlayerHasWon = True

    for player in players:
        if player == currentPlayer:
            continue

        elif not player.isDead:
            currentPlayerHasWon = False
            return False

    return True


def play(players):
    questionSet = prevQuestionSet = None
    #needsToRepeatQuestion = False

    futureActions = dict()

    roundIndex = 0


    updateBarChart(players)

    plt.ion()

    while True:
        plt.cla()

        # current player
        currentPlayer = players[roundIndex % len(players)]
        roundIndex += 1

        # player color
        print(currentPlayer.colorCode)

        # check if the player is alive
        if currentPlayer.isDead:
            print(currentPlayer.name, "is dead and can't play :(")
            continue

        else:
            if playerHasWon(currentPlayer, players):
                print(currentPlayer.name, "has won :)")
                break

        # TODO: add ties.

        # actions from previous rounds
        if roundIndex in futureActions:
            print("From a few moves ago:")
            parseAnswerConsequences(futureActions[roundIndex], currentPlayer, players)
            del futureActions[roundIndex]

            print("\n")


        # preventing duplicates
        questionSet = getRandomQuestionSet()
        while questionSet == prevQuestionSet:
            questionSet = getRandomQuestionSet()

        input("Press enter to continue, " + currentPlayer.name)  # wait for user to press enter

        print(questionSet["question"])

        answerIsYes = getBinaryInput()

        consequences = questionSet["yes" if answerIsYes else "no"]
        futureAction = parseAnswerConsequences(consequences, currentPlayer, players)

        if futureAction is not None:
            for stat, action in futureAction.items():
                if not action[0] in futureActions:
                    executeRoundIndex = int(action[0]) * len(players) + roundIndex

                    futureActions[executeRoundIndex] = {}
                    futureActions[executeRoundIndex][stat] = action[1]


        print("\n" * 2)  # whitespace

        prevQuestionSet = questionSet  # previous question set, to avoid duplicates


        # this works better when you run it multiple times. idk why though.
        # TODO: find how to make this work while running it only once.
        for i in range(3):
            updateBarChart(players)


        if currentPlayer.isDead:
            print(currentPlayer.name, "has died and can't play :(")
            continue


        if roundIndex > 10 * len(players):
            print(RESET + "Game has gone on for too long. All surviving players draw.")
            break
