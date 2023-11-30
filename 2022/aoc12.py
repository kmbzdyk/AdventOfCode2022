from array import *
inputFile = open('aoc12input.txt', 'r')
inputLines = inputFile.readlines()
elevations = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def part1(input):
    elevationGrid = []

    currentPosition = []
    destination = []

    lineCounter = 0
    for line in input:
        line = line.strip()

        elevationGrid.append([])

        charCounter = 0
        for char in line:
            if char == "S":
                elevationGrid[lineCounter].append(["a"])
                currentPosition = [lineCounter, charCounter]
            elif char == "E":
                elevationGrid[lineCounter].append(["z"])
                destination = [lineCounter, charCounter]
            else:
                elevationGrid[lineCounter].append([char])
            charCounter += 1
        print(elevationGrid[lineCounter])
        lineCounter += 1

    path = [currentPosition]
    run = 0
    pathToDestination = findPath(currentPosition, destination, elevationGrid, path, run)

        # check which directions are available for move
        # check directions you should move towards to
        # gotta need function for calculating possible paths to the destination and picking the shortest one

    return pathToDestination

def findPath(currentPosition, destination, elevationGrid, path, run):
    run += 1
    print("--------------------------")
    print("It's a run:")
    print(run)
    # iterate through 4 possible moves: 1,1 -> 0,1 2,1 1,2 1,0
    
    leftPath = []
    rightPath = []
    upPath = []
    downPath = []

    print("Current position")
    print([currentPosition[0],currentPosition[1]])

    if ([currentPosition[0], currentPosition[1]-1] == destination or [currentPosition[0], currentPosition[1]+1] == destination or 
        [currentPosition[0]+1, currentPosition[1]] == destination or [currentPosition[0]-1, currentPosition[1]+1] == destination):
        print("Woohoo! We got to the destination!")
        path.append(destination)
        return path
    else:
        # check left
        if currentPosition[1] > 0 and (len(path)==1 or [currentPosition[0],currentPosition[1]-1] not in path):
            print("It's a run:")
            print(run)
            print("Check left")
            print([currentPosition[0],currentPosition[1]-1])
            if elevations.index(elevationGrid[currentPosition[0]][currentPosition[1]-1][0]) <= elevations.index(elevationGrid[currentPosition[0]][currentPosition[1]][0])+1: # check if we can move there
                print("Going left")
                leftPath = path
                leftPath.append([currentPosition[0], currentPosition[1]-1]) # add position to the path
                if [currentPosition[0], currentPosition[1]-1] != destination: # check if not destination - gotta keep looking
                    # print("gonna check left")
                    # return
                    leftPath = findPath([currentPosition[0], currentPosition[1]-1], destination, elevationGrid, leftPath, run)
        # check right
        if currentPosition[1] < len(elevationGrid[0])-1 and (len(path)==1 or [currentPosition[0],currentPosition[1]+1] not in path):
            print("It's a run:")
            print(run)
            print("Check right")
            print([currentPosition[0],currentPosition[1]+1])
            # print(elevationGrid[currentPosition[0]][currentPosition[1]+1][0])
            # print(elevationGrid[currentPosition[0]][currentPosition[1]][0])
            # print(elevations.index(elevationGrid[currentPosition[0]][currentPosition[1]+1][0]))
            # print(elevations.index(elevationGrid[currentPosition[0]][currentPosition[1]][0])+1)
            if elevations.index(elevationGrid[currentPosition[0]][currentPosition[1]+1][0]) <= elevations.index(elevationGrid[currentPosition[0]][currentPosition[1]][0])+1: # check if we can move there
                print("Going right")
                rightPath = path
                rightPath.append([currentPosition[0], currentPosition[1]+1]) # add position to the path
                if [currentPosition[0], currentPosition[1]+1] != destination: # check if not destination - gotta keep looking
                    # print("gonna check right")
                    # return
                    rightPath = findPath([currentPosition[0], currentPosition[1]+1], destination, elevationGrid, rightPath, run)
        # check up
        if currentPosition[0] > 0 and (len(path)==1 or  [currentPosition[0]-1,currentPosition[1]] not in path):
            print("It's a run:")
            print(run)
            print("Check up")
            print([currentPosition[0]-1,currentPosition[1]])
            if elevations.index(elevationGrid[currentPosition[0]-1][currentPosition[1]][0]) <= elevations.index(elevationGrid[currentPosition[0]][currentPosition[1]][0])+1: # check if we can move there
                print("Going up")
                upPath = path
                upPath.append([currentPosition[0]-1, currentPosition[1]]) # add position to the path
                if [currentPosition[0]-1, currentPosition[1]] != destination: # check if not destination - gotta keep looking
                    # print("gonna check up")
                    # return
                    upPath = findPath([currentPosition[0]-1, currentPosition[1]], destination, elevationGrid, upPath, run)
        # check down
        if currentPosition[0] < len(elevationGrid) - 1 and (len(path)==1 or  [currentPosition[0]+1,currentPosition[1]] not in path):
            print("It's a run:")
            print(run)
            print("Check down")
            print([currentPosition[0]+1,currentPosition[1]])
            if elevations.index(elevationGrid[currentPosition[0]+1][currentPosition[1]][0]) <= elevations.index(elevationGrid[currentPosition[0]][currentPosition[1]][0])+1: # check if we can move there
                print("Going down")
                downPath = path
                downPath.append([currentPosition[0]+1, currentPosition[1]]) # add position to the path
                if [currentPosition[0]+1, currentPosition[1]] != destination: # check if not destination - gotta keep looking
                    # print("gonna check down")
                    # return
                    downPath = findPath([currentPosition[0]+1, currentPosition[1]], destination, elevationGrid, downPath, run)
    
        # find shortest path
        availablePaths = []
        if len(leftPath) != 0: availablePaths.append(leftPath)
        if len(rightPath) != 0: availablePaths.append(rightPath)
        if len(upPath) != 0: availablePaths.append(upPath)
        if len(downPath) != 0: availablePaths.append(downPath)

        if len(availablePaths) == 0: 
            print("Dead End here!")
        # print("Left path:")
        # print(leftPath)
        # print("Right path:")
        # print(rightPath)
        # print("Up path:")
        # print(upPath)
        # print("Down path:")
        # print(downPath)

        # print("Available paths!")
        # print(availablePaths)

        if len(availablePaths) == 0:
            return []
        else:
            shortestPath = availablePaths[0]
            for path in availablePaths:
                if len(path) < len(shortestPath):
                    shortestPath = path
            return shortestPath


def part2(input):
    currentCycle = 0
    drawnImage = []

    for x in range(240): # fill image with dark spaces
        drawnImage.append(".")

    for line in input: # for each instruction
        if "noop" in line: # takes one cycle, no change to register
            currentCycle += 1

    return drawnImage
    
print(part1(inputLines))
# print(part2(inputLines))