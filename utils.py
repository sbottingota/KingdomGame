COLORS = ["red", "green", "blue", "purple"]

COLOR_CODES = ["\u001b[31m", "\u001b[32m", "\u001b[34m", "\u001b[35m"]
RESET = "\u001b[0m"

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

def checkIfIsInt(checkValue):
    try:
        int(checkValue)
    except ValueError:
        return False

    else:
        return True

def getInt(message, min, max):
    output = input(message)

    if checkIfIsInt(output) == False:
        output = getInt("Not a number, please try again: ", min, max)

    output = int(output)
    if output > max or output < min:
        output = getInt("Number is out of bounds, please put a number between "
                        + str(min) + " and " + str(max) + ": ", min, max)

    return output

def getNotEmptyString(message):
    output = input(message)
    #output = output.strip()

    if output.strip() == "":
        output = getNotEmptyString("String can't be just whitespace. Please input a string with more than whitespace. ")

    return output
