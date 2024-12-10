inputFile = open('aoc3input.txt', 'r')
inputLines = inputFile.readlines()

def part1(input):
    multiplicationSum = 0
    analyseMode = False
    lastAnalysedChar = ""
    firstNumber = ""
    secondNumber = ""

    for char in ''.join(input):

        if analyseMode:
            if lastAnalysedChar == "m":
                if char != "u":
                    analyseMode = False
                    firstNumber = ""
                    secondNumber = ""
                else:
                    lastAnalysedChar = char
            elif lastAnalysedChar == "u":
                if char != "l":
                    analyseMode = False
                    firstNumber = ""
                    secondNumber = ""
                else:
                    lastAnalysedChar = char
            elif lastAnalysedChar == "l":
                if char != "(":
                    analyseMode = False
                    firstNumber = ""
                    secondNumber = ""
                else:
                    lastAnalysedChar = char
            elif lastAnalysedChar == "(" or lastAnalysedChar == ",":
                if not char.isdigit():
                    analyseMode = False
                    firstNumber = ""
                    secondNumber = ""
                else:
                    lastAnalysedChar = char
            elif lastAnalysedChar.isdigit():
                if char.isdigit():
                    if len(lastAnalysedChar) < 3:
                        lastAnalysedChar = lastAnalysedChar + char
                    else:
                        analyseMode = False
                        firstNumber = ""
                        secondNumber = ""
                elif char == "," and firstNumber == "":
                    firstNumber = lastAnalysedChar
                    lastAnalysedChar = char
                elif char == ")" and firstNumber != "" and secondNumber == "":
                    secondNumber = lastAnalysedChar
                    lastAnalysedChar = char
                    multiplicationSum += int(firstNumber) * int(secondNumber)
                    analyseMode = False
                    firstNumber = ""
                    secondNumber = ""
                else:
                    analyseMode = False
                    firstNumber = ""
                    secondNumber = ""
            else:
                analyseMode = False
                firstNumber = ""
                secondNumber = ""
        else:
            if char == "m":
                analyseMode = True
                lastAnalysedChar = "m"

    return multiplicationSum

def part2(input):
    multiplicationSum = 0
    analyseMode = False
    doDontMode = False
    currentIsDo = True
    lastAnalysedChar = ""
    firstNumber = ""
    secondNumber = ""
    multiplicationEnabled = True

    for char in ''.join(input):

        if analyseMode:
            if lastAnalysedChar == "m":
                if char != "u":
                    analyseMode = False
                    firstNumber = ""
                    secondNumber = ""
                else:
                    lastAnalysedChar = char
            elif lastAnalysedChar == "u":
                if char != "l":
                    analyseMode = False
                    firstNumber = ""
                    secondNumber = ""
                else:
                    lastAnalysedChar = char
            elif lastAnalysedChar == "l":
                if char != "(":
                    analyseMode = False
                    firstNumber = ""
                    secondNumber = ""
                else:
                    lastAnalysedChar = char
            elif lastAnalysedChar == "(" or lastAnalysedChar == ",":
                if not char.isdigit():
                    analyseMode = False
                    firstNumber = ""
                    secondNumber = ""
                else:
                    lastAnalysedChar = char
            elif lastAnalysedChar.isdigit():
                if char.isdigit():
                    if len(lastAnalysedChar) < 3:
                        lastAnalysedChar = lastAnalysedChar + char
                    else:
                        analyseMode = False
                        firstNumber = ""
                        secondNumber = ""
                elif char == "," and firstNumber == "":
                    firstNumber = lastAnalysedChar
                    lastAnalysedChar = char
                elif char == ")" and firstNumber != "" and secondNumber == "":
                    secondNumber = lastAnalysedChar
                    lastAnalysedChar = char
                    multiplicationSum += int(firstNumber) * int(secondNumber)
                    analyseMode = False
                    firstNumber = ""
                    secondNumber = ""
                else:
                    analyseMode = False
                    firstNumber = ""
                    secondNumber = ""
            else:
                analyseMode = False
                firstNumber = ""
                secondNumber = ""
        elif doDontMode:
            if lastAnalysedChar == "d":
                if char != "o":
                    doDontMode = False
                else:
                    lastAnalysedChar = char
            elif lastAnalysedChar == "o":
                if char != "n" and char != "(":
                    doDontMode = False
                else:
                    lastAnalysedChar = char
                    if char == "n":
                        currentIsDo = False
                    else:
                        currentIsDo = True
            elif lastAnalysedChar == "n":
                if char != "'":
                    doDontMode = False
                else:
                    lastAnalysedChar = char
            elif lastAnalysedChar == "'":
                if char != "t":
                    doDontMode = False
                else:
                    lastAnalysedChar = char
            elif lastAnalysedChar == "t":
                if char != "(":
                    doDontMode = False
                else:
                    lastAnalysedChar = char
            elif lastAnalysedChar == "(":
                if char != ")":
                    doDontMode = False
                else:
                    doDontMode = False

                    if currentIsDo:
                        multiplicationEnabled = True
                    else:
                        multiplicationEnabled = False
            else:
                doDontMode = False
        else:
            if char == "m" and multiplicationEnabled:
                analyseMode = True
                lastAnalysedChar = "m"
            if char == "d":
                doDontMode = True
                lastAnalysedChar = "d"

    return multiplicationSum


# print(part1(inputLines))
print(part2(inputLines))