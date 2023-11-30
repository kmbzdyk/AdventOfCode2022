from array import *
inputFile = open('aoc10input.txt', 'r')
inputLines = inputFile.readlines()

def part1(input):
    cyclesToReport = [20,60,100,140,180,220]
    currentRegister = 1
    currentCycle = 0
    signalStrengthSum = 0

    for line in input: # for each instruction
        if "noop" in line: # takes one cycle, no change to register
            currentCycle += 1
            if currentCycle in cyclesToReport: signalStrengthSum += currentCycle * currentRegister
        else: # takes two cycles, update register
            currentCycle += 1
            if currentCycle in cyclesToReport: signalStrengthSum += currentCycle * currentRegister

            currentCycle += 1
            if currentCycle in cyclesToReport: signalStrengthSum += currentCycle * currentRegister

            addixValue = int(line.strip().split(" ")[1])
            currentRegister += addixValue

    return signalStrengthSum

def part2(input):
    currentRegister = 1
    currentCycle = 0
    currentCRTPosition = 0
    drawnImage = []

    for x in range(240): # fill image with dark spaces
        drawnImage.append(".")

    for line in input: # for each instruction
        if "noop" in line: # takes one cycle, no change to register
            currentCycle += 1
            if currentCRTPosition in getRegisterLocations(currentRegister):
                drawnImage[currentCRTPosition] = "#"
            currentCRTPosition +=1

        else: # takes two cycles, update register
            currentCycle += 1
            if currentCRTPosition in getRegisterLocations(currentRegister):
                drawnImage[currentCRTPosition] = "#"
            currentCRTPosition +=1

            currentCycle += 1
            if currentCRTPosition in getRegisterLocations(currentRegister):
                drawnImage[currentCRTPosition] = "#"
            currentCRTPosition +=1

            addixValue = int(line.strip().split(" ")[1])
            currentRegister += addixValue

    return drawnImage

def getRegisterLocations(currentRegister): # get possible register locations vertically
    registerLocations = [currentRegister, currentRegister-1, currentRegister+1]

    for x in range(5):
        currentRegister = currentRegister + 40
        registerLocations.append(currentRegister)
        registerLocations.append(currentRegister-1)
        registerLocations.append(currentRegister+1)
    return registerLocations

def printImage(drawnImage): # printing out the image on the screen
    for x in range(6):
        for y in range(((x+1) * 40) - 40, (x+1) * 40):
            print(drawnImage[y], end = '')
        print('')
    
print(part1(inputLines))
printImage(part2(inputLines))