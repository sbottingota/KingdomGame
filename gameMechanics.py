import random
import json
import matplotlib
import matplotlib.pyplot as plt

def getBinaryInput():
    binaryInput = input("y(es) or n(o): ")

    inputIsInvalid = True

    while inputIsInvalid:
        if binaryInput == "y":
            output = True
            inputIsInvalid = False

        elif binaryInput == "n":
            output = False
            inputIsInvalid = False

        else:
            binaryInput = input("Invalid input, please try again: ")

    return output


# returns if the question needs to be presented to the next person
def parseAnswerConsequences(actions, currentPlayer, players):
    if actions == "n":
        return True

    for stat in actions:
        # take from each player
        if actions[stat][0] == "p":
            addValue = int(actions[stat][1:])

            currentPlayer.addToStat(len(players) * addValue, stat)

            for player in players:
                if players.index(player) != -1:
                    player.addToStat(-addValue, stat)


        # add or subtract
        else:
            currentPlayer.addToStat(int(actions[stat]), stat)

    return False


def getRandomQuestionSet():
    with open("questions.json", "r") as questions:
        return random.choice(json.load(questions))

def updateBarChart(players):
    plt.cla()
    figure, axis = plt.subplots(len(players), 1)
    #plt.ylim(top=100)
    plt.ylim(bottom=100)
    for player in players:
        player.updateBarChart(axis[players.index(player)])
    plt.ion()
    plt.pause(0.01)

def play(players):
    matplotlib.use("TkAgg")

    questionSet = prevQuestionSet = {"question": None}
    needsToRepeatQuestion = False

    playerIndex = 0

    updateBarChart(players)
    plt.show(block=False)

    while True:

        # current player
        currentPlayer = players[playerIndex]

        # preventing duplicates
        if not needsToRepeatQuestion:
            while questionSet["question"] == prevQuestionSet["question"]:
                questionSet = getRandomQuestionSet()

        input("Press enter to continue")  # wait for user to press enter

        print(questionSet["question"])

        answerIsYes = getBinaryInput()
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

        #graph
        updateBarChart(players)

