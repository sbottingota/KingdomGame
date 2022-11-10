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
        print("next player")
        return True

    print(actions.keys())
    for stat in actions:
        print(stat)
        # take from each player
        if actions[stat][0] == "p":
            addValue = int(actions[stat][1:])
            print("take", addValue)

            currentPlayer.addToStat(len(players) * addValue, stat)

            for player in players:
                if currentPlayer != player and player.isDead == False:
                    player.addToStat(-addValue, stat)


        # add or subtract
        else:
            currentPlayer.addToStat(int(actions[stat]), stat)
            print("add", actions[stat], "to/from", stat)

    for player in players:
        if player.isDead:
            print(player.name, "has died :(")
    return False


def getRandomQuestionSet():
    with open("questions.json", "r") as questions:
        return random.choice(json.load(questions))

def updateBarChart(players):
    nRows = 2 if len(players) > 3 else 1

    for player in players:
        plt.subplot(round(len(players) / nRows), nRows, players.index(player) + 1)
        plt.cla()
        #plt.title(player.name)
        plt.barh(tuple(player.stats.keys()), player.stats.values(), color=player.color)

    plt.pause(0.01)

def play(players):
    questionSet = prevQuestionSet = {"question": None}
    needsToRepeatQuestion = False

    playerIndex = 0

    plt.ion()
    updateBarChart(players)

    while True:
        # current player
        currentPlayer = players[playerIndex]

        # check if the player is alive
        if currentPlayer.isDead:
            playerIndex += 1
            continue

        # preventing duplicates
        if not needsToRepeatQuestion:
            while questionSet["question"] == prevQuestionSet["question"]:
                questionSet = getRandomQuestionSet()

        input("Press enter to continue, " + currentPlayer.name)  # wait for user to press enter

        print(questionSet["question"])

        answerIsYes = getBinaryInput()

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

        # this works better when you run it twice. idk why though.
        for i in range(2):
            updateBarChart(players)