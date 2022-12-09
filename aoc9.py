from array import *
inputFile = open('aoc9input.txt', 'r')
inputLines = inputFile.readlines()

def part1(input):
    tailLocations = [[0,0]] # assume x:0 y:0 is a starting point
    currentHeadLocation = [0,0]
    currentTailLocation = [0,0]

    for line in input: # for each instruction
        direction, steps = line.strip().split(" ")
            
        for step in range(int(steps)):
            # first move head
            if direction == "R": currentHeadLocation[0] += 1
            elif direction == "L": currentHeadLocation[0] -= 1
            elif direction == "U": currentHeadLocation[1] += 1
            elif direction == "D": currentHeadLocation[1] -= 1

            # move the tail
            currentHeadLocation, currentTailLocation, tailLocations = moveTail(direction, currentHeadLocation, currentTailLocation, tailLocations, True)

    return len(tailLocations)

def part2(input):
    tailLocations = [[0,0]] # assume x:0 y:0 is a starting point
    currentKnotsLocations = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

    for line in input: # for each instruction
        direction, steps = line.strip().split(" ")
        
        for step in range(int(steps)):
            # first move head
            if direction == "R": currentKnotsLocations[0][0] += 1
            elif direction == "L": currentKnotsLocations[0][0] -= 1
            elif direction == "U": currentKnotsLocations[0][1] += 1
            elif direction == "D": currentKnotsLocations[0][1] -= 1

            # move all the tails
            for knotIndex in range(len(currentKnotsLocations)-1):
                if knotIndex is not 8:
                    currentKnotsLocations[knotIndex], currentKnotsLocations[knotIndex+1], tailLocations = moveTail(direction, currentKnotsLocations[knotIndex], currentKnotsLocations[knotIndex+1], tailLocations, False)
                else:
                    currentKnotsLocations[knotIndex], currentKnotsLocations[knotIndex+1], tailLocations = moveTail(direction, currentKnotsLocations[knotIndex], currentKnotsLocations[knotIndex+1], tailLocations, True)

    return len(tailLocations)

def moveTail(direction, currentHeadLocation, currentTailLocation, tailLocations, countTailLocations):
    if direction == "R":
        if (currentTailLocation[0] > currentHeadLocation[0]+1 or currentTailLocation[0] < currentHeadLocation[0]-1 or
            currentTailLocation[1] > currentHeadLocation[1]+1 or currentTailLocation[1] < currentHeadLocation[1]-1):
            if currentTailLocation[0] > currentHeadLocation[0]+1:
                currentTailLocation[0] -= 1

                if currentTailLocation[0] != currentHeadLocation[0]:
                    if currentTailLocation[1] > currentHeadLocation[1]:
                        currentTailLocation[1] -= 1
                    elif currentTailLocation[1] < currentHeadLocation[1]:
                        currentTailLocation[1] += 1
                else:
                    if currentTailLocation[1] > currentHeadLocation[1]+1:
                        currentTailLocation[1] -= 1
                    elif currentTailLocation[1] < currentHeadLocation[1]-1:
                        currentTailLocation[1] += 1
            elif currentTailLocation[0] < currentHeadLocation[0]-1:
                currentTailLocation[0] += 1

                if currentTailLocation[0] != currentHeadLocation[0]:
                    if currentTailLocation[1] > currentHeadLocation[1]:
                        currentTailLocation[1] -= 1
                    elif currentTailLocation[1] < currentHeadLocation[1]:
                        currentTailLocation[1] += 1
                else:
                    if currentTailLocation[1] > currentHeadLocation[1]+1:
                        currentTailLocation[1] -= 1
                    elif currentTailLocation[1] < currentHeadLocation[1]-1:
                        currentTailLocation[1] += 1

            elif currentTailLocation[1] > currentHeadLocation[1]+1:
                currentTailLocation[1] -= 1

                if currentTailLocation[1] != currentHeadLocation[1]:
                    if currentTailLocation[0] > currentHeadLocation[0]:
                        currentTailLocation[0] -= 1
                    elif currentTailLocation[0] < currentHeadLocation[0]:
                        currentTailLocation[0] += 1
                else:
                    if currentTailLocation[0] > currentHeadLocation[0]+1:
                        currentTailLocation[0] -= 1
                    elif currentTailLocation[0] < currentHeadLocation[0]-1:
                        currentTailLocation[0] += 1
            elif currentTailLocation[1] < currentHeadLocation[1]-1:
                currentTailLocation[1] += 1

                if currentTailLocation[1] != currentHeadLocation[1]:
                    if currentTailLocation[0] > currentHeadLocation[0]:
                        currentTailLocation[0] -= 1
                    elif currentTailLocation[0] < currentHeadLocation[0]:
                        currentTailLocation[0] += 1
                else:
                    if currentTailLocation[0] > currentHeadLocation[0]+1:
                        currentTailLocation[0] -= 1
                    elif currentTailLocation[0] < currentHeadLocation[0]-1:
                        currentTailLocation[0] += 1

            if countTailLocations and currentTailLocation not in tailLocations:
                stack = []
                stack = stack[:] + currentTailLocation
                tailLocations.append(stack)

    elif direction == "L":
        if (currentTailLocation[0] > currentHeadLocation[0]+1 or currentTailLocation[0] < currentHeadLocation[0]-1 or
            currentTailLocation[1] > currentHeadLocation[1]+1 or currentTailLocation[1] < currentHeadLocation[1]-1):
            if currentTailLocation[0] > currentHeadLocation[0]+1:
                currentTailLocation[0] -= 1

                if currentTailLocation[0] != currentHeadLocation[0]:
                    if currentTailLocation[1] > currentHeadLocation[1]:
                        currentTailLocation[1] -= 1
                    elif currentTailLocation[1] < currentHeadLocation[1]:
                        currentTailLocation[1] += 1
                else:
                    if currentTailLocation[1] > currentHeadLocation[1]+1:
                        currentTailLocation[1] -= 1
                    elif currentTailLocation[1] < currentHeadLocation[1]-1:
                        currentTailLocation[1] += 1

            elif currentTailLocation[0] < currentHeadLocation[0]-1:
                currentTailLocation[0] += 1

                if currentTailLocation[0] != currentHeadLocation[0]:
                    if currentTailLocation[1] > currentHeadLocation[1]:
                        currentTailLocation[1] -= 1
                    elif currentTailLocation[1] < currentHeadLocation[1]:
                        currentTailLocation[1] += 1
                else:
                    if currentTailLocation[1] > currentHeadLocation[1]+1:
                        currentTailLocation[1] -= 1
                    elif currentTailLocation[1] < currentHeadLocation[1]-1:
                        currentTailLocation[1] += 1

            elif currentTailLocation[1] > currentHeadLocation[1]+1:
                currentTailLocation[1] -= 1

                if currentTailLocation[1] != currentHeadLocation[1]:
                    if currentTailLocation[0] > currentHeadLocation[0]:
                        currentTailLocation[0] -= 1
                    elif currentTailLocation[0] < currentHeadLocation[0]:
                        currentTailLocation[0] += 1
                else:
                    if currentTailLocation[0] > currentHeadLocation[0]+1:
                        currentTailLocation[0] -= 1
                    elif currentTailLocation[0] < currentHeadLocation[0]-1:
                        currentTailLocation[0] += 1


            elif currentTailLocation[1] < currentHeadLocation[1]-1:
                currentTailLocation[1] += 1

                if currentTailLocation[1] != currentHeadLocation[1]:
                    if currentTailLocation[0] > currentHeadLocation[0]:
                        currentTailLocation[0] -= 1
                    elif currentTailLocation[0] < currentHeadLocation[0]:
                        currentTailLocation[0] += 1
                else:
                    if currentTailLocation[0] > currentHeadLocation[0]+1:
                        currentTailLocation[0] -= 1
                    elif currentTailLocation[0] < currentHeadLocation[0]-1:
                        currentTailLocation[0] += 1

            if countTailLocations and currentTailLocation not in tailLocations:
                stack = []
                stack = stack[:] + currentTailLocation
                tailLocations.append(stack)
    elif direction == "U":
        if (currentTailLocation[0] > currentHeadLocation[0]+1 or currentTailLocation[0] < currentHeadLocation[0]-1 or
            currentTailLocation[1] > currentHeadLocation[1]+1 or currentTailLocation[1] < currentHeadLocation[1]-1):
            if currentTailLocation[0] > currentHeadLocation[0]+1:
                currentTailLocation[0] -= 1

                if currentTailLocation[0] != currentHeadLocation[0]:
                    if currentTailLocation[1] > currentHeadLocation[1]:
                        currentTailLocation[1] -= 1
                    elif currentTailLocation[1] < currentHeadLocation[1]:
                        currentTailLocation[1] += 1
                else:
                    if currentTailLocation[1] > currentHeadLocation[1]+1:
                        currentTailLocation[1] -= 1
                    elif currentTailLocation[1] < currentHeadLocation[1]-1:
                        currentTailLocation[1] += 1
            elif currentTailLocation[0] < currentHeadLocation[0]-1:
                currentTailLocation[0] += 1

                if currentTailLocation[0] != currentHeadLocation[0]:
                    if currentTailLocation[1] > currentHeadLocation[1]:
                        currentTailLocation[1] -= 1
                    elif currentTailLocation[1] < currentHeadLocation[1]:
                        currentTailLocation[1] += 1
                else:
                    if currentTailLocation[1] > currentHeadLocation[1]+1:
                        currentTailLocation[1] -= 1
                    elif currentTailLocation[1] < currentHeadLocation[1]-1:
                        currentTailLocation[1] += 1

            elif currentTailLocation[1] > currentHeadLocation[1]+1:
                currentTailLocation[1] -= 1

                if currentTailLocation[1] != currentHeadLocation[1]:
                    if currentTailLocation[0] > currentHeadLocation[0]:
                        currentTailLocation[0] -= 1
                    elif currentTailLocation[0] < currentHeadLocation[0]:
                        currentTailLocation[0] += 1
                else:
                    if currentTailLocation[0] > currentHeadLocation[0]+1:
                        currentTailLocation[0] -= 1
                    elif currentTailLocation[0] < currentHeadLocation[0]-1:
                        currentTailLocation[0] += 1
            elif currentTailLocation[1] < currentHeadLocation[1]-1:
                currentTailLocation[1] += 1

                if currentTailLocation[1] != currentHeadLocation[1]:
                    if currentTailLocation[0] > currentHeadLocation[0]:
                        currentTailLocation[0] -= 1
                    elif currentTailLocation[0] < currentHeadLocation[0]:
                        currentTailLocation[0] += 1
                else:
                    if currentTailLocation[0] > currentHeadLocation[0]+1:
                        currentTailLocation[0] -= 1
                    elif currentTailLocation[0] < currentHeadLocation[0]-1:
                        currentTailLocation[0] += 1

            if countTailLocations and currentTailLocation not in tailLocations:
                stack = []
                stack = stack[:] + currentTailLocation
                tailLocations.append(stack)
    elif direction == "D":
        if (currentTailLocation[0] > currentHeadLocation[0]+1 or currentTailLocation[0] < currentHeadLocation[0]-1 or
            currentTailLocation[1] > currentHeadLocation[1]+1 or currentTailLocation[1] < currentHeadLocation[1]-1):

            if currentTailLocation[0] > currentHeadLocation[0]+1:
                currentTailLocation[0] -= 1

                if currentTailLocation[0] != currentHeadLocation[0]:
                    if currentTailLocation[1] > currentHeadLocation[1]:
                        currentTailLocation[1] -= 1
                    elif currentTailLocation[1] < currentHeadLocation[1]:
                        currentTailLocation[1] += 1
                else:
                    if currentTailLocation[1] > currentHeadLocation[1]+1:
                        currentTailLocation[1] -= 1
                    elif currentTailLocation[1] < currentHeadLocation[1]-1:
                        currentTailLocation[1] += 1

            elif currentTailLocation[0] < currentHeadLocation[0]-1:
                currentTailLocation[0] += 1

                if currentTailLocation[0] != currentHeadLocation[0]:
                    if currentTailLocation[1] > currentHeadLocation[1]:
                        currentTailLocation[1] -= 1
                    elif currentTailLocation[1] < currentHeadLocation[1]:
                        currentTailLocation[1] += 1
                else:
                    if currentTailLocation[1] > currentHeadLocation[1]+1:
                        currentTailLocation[1] -= 1
                    elif currentTailLocation[1] < currentHeadLocation[1]-1:
                        currentTailLocation[1] += 1

            elif currentTailLocation[1] > currentHeadLocation[1]+1:
                currentTailLocation[1] -= 1

                if currentTailLocation[1] != currentHeadLocation[1]:
                    if currentTailLocation[0] > currentHeadLocation[0]:
                        currentTailLocation[0] -= 1
                    elif currentTailLocation[0] < currentHeadLocation[0]:
                        currentTailLocation[0] += 1
                else:
                    if currentTailLocation[0] > currentHeadLocation[0]+1:
                        currentTailLocation[0] -= 1
                    elif currentTailLocation[0] < currentHeadLocation[0]-1:
                        currentTailLocation[0] += 1

            elif currentTailLocation[1] < currentHeadLocation[1]-1:
                currentTailLocation[1] += 1

                if currentTailLocation[1] != currentHeadLocation[1]:
                    if currentTailLocation[0] > currentHeadLocation[0]:
                        currentTailLocation[0] -= 1
                    elif currentTailLocation[0] < currentHeadLocation[0]:
                        currentTailLocation[0] += 1
                else:
                    if currentTailLocation[0] > currentHeadLocation[0]+1:
                        currentTailLocation[0] -= 1
                    elif currentTailLocation[0] < currentHeadLocation[0]-1:
                        currentTailLocation[0] += 1

            if countTailLocations and currentTailLocation not in tailLocations:
                stack = []
                stack = stack[:] + currentTailLocation
                tailLocations.append(stack)
    return currentHeadLocation, currentTailLocation, tailLocations
    
print(part1(inputLines))
print(part2(inputLines))