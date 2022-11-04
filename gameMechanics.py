import random
import json

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

def getRandomQuestionSet():
    with open("questions.json", "r") as questions:
        return random.choice(json.load(questions))

def play(players):
    questionSet = prevQuestionSet = {"question": None}

    while True:
        # preventing duplicates
        while questionSet["question"] == prevQuestionSet["question"]:
            questionSet = getRandomQuestionSet()

        input("Press enter to continue")  # wait for user to press enter

        print(questionSet["question"])

        answerIsYes = getBinaryInput()
        if answerIsYes:
            print("\n", questionSet["yes"])

        else:
            print("\n", questionSet["no"])

        print("\n" * 3)  # whitespace

        prevQuestionSet = questionSet  # previous question set, to avoid duplicates

