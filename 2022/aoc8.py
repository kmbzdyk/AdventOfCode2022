from array import *
inputFile = open('aoc8input.txt', 'r')
inputLines = inputFile.readlines()

def part1(input):
    treeGrid = []
    visibleTrees = 0

    lineCounter = 0
    for line in input:
        line.strip()

        if any(char.isdigit() for char in line):
            treeGrid.append([])

        for char in line:
            if char.isdigit(): treeGrid[lineCounter].append([int(char.strip())])
        lineCounter += 1

    # iterate through all trees
    for row in range(len(treeGrid)):
        for column in range(len(treeGrid[row])):
            if row == 0 or row == len(treeGrid) - 1 or column == 0 or column == len(treeGrid[row]) -1:
                visibleTrees += 1
            else:
                # left
                leftVisible = True
                for sameRowTreeLeft in range(column):
                    if treeGrid[row][sameRowTreeLeft][0] >= treeGrid[row][column][0]:
                        leftVisible = False
                        break
                # right
                rightVisible = True
                for sameRowTreeLeft in range(column+1, len(treeGrid[row])):
                    if treeGrid[row][sameRowTreeLeft][0] >= treeGrid[row][column][0]:
                        rightVisible = False
                        break

                # top
                topVisible = True
                for sameColumnTree in range(row):
                    if treeGrid[sameColumnTree][column][0] >= treeGrid[row][column][0]:
                        topVisible = False
                        break

                # bottom
                bottomVisible = True
                for sameColumnTree in range(row+1, len(treeGrid)):
                    if treeGrid[sameColumnTree][column][0] >= treeGrid[row][column][0]:
                        bottomVisible = False
                        break

                if leftVisible or rightVisible or topVisible or bottomVisible: 
                    visibleTrees += 1

    return visibleTrees

def part2(input):
    treeGrid = []
    bestVisibility = 0

    lineCounter = 0
    for line in input:
        line.strip()

        if any(char.isdigit() for char in line):
            treeGrid.append([])

        for char in line:
            if char.isdigit(): treeGrid[lineCounter].append([int(char.strip())])
        lineCounter += 1

    # iterate through all trees
    for row in range(len(treeGrid)):
        for column in range(len(treeGrid[row])):
            if row != 0 and row != len(treeGrid) - 1 and column != 0 and column != len(treeGrid[row]) -1:
                # left
                leftVisibility = 0
                for sameRowTreeLeft in range(column-1, -1, -1):
                    if treeGrid[row][sameRowTreeLeft][0] >= treeGrid[row][column][0]:
                        leftVisibility += 1
                        break
                    else:
                        leftVisibility += 1
                # right
                rightVisibility = 0
                for sameRowTreeLeft in range(column+1, len(treeGrid[row])):
                    if treeGrid[row][sameRowTreeLeft][0] >= treeGrid[row][column][0]:
                        rightVisibility += 1
                        break
                    else:
                        rightVisibility += 1

                # top
                topVisibility = 0
                for sameColumnTree in range(row-1, -1, -1):
                    if treeGrid[sameColumnTree][column][0] >= treeGrid[row][column][0]:
                        topVisibility += 1
                        break
                    else:
                        topVisibility += 1

                # bottom
                bottomVisibility = 0
                for sameColumnTree in range(row+1, len(treeGrid)):
                    if treeGrid[sameColumnTree][column][0] >= treeGrid[row][column][0]:
                        bottomVisibility += 1
                        break
                    else:
                        bottomVisibility += 1

                currentVisibility = leftVisibility * rightVisibility * topVisibility * bottomVisibility
                if currentVisibility > bestVisibility: bestVisibility = currentVisibility

    return bestVisibility
    
print(part1(inputLines))
print(part2(inputLines))