inputFile = open('aoc1input.txt', 'r')
inputLines = inputFile.readlines()

def part1(input):
    leftList = []
    rightList = []
    totalDistance = 0

    for line in input:
        currentValues = line.split("   ")
        leftList.append(currentValues[0])
        rightList.append(currentValues[1])

    while (len(leftList) > 0):
        totalDistance = totalDistance + abs(int(min(leftList)) - int(min(rightList)))
        leftList.remove(min(leftList))
        rightList.remove(min(rightList))

    return totalDistance

def part2(input):
    leftList = []
    rightList = []
    similarityScore = 0

    for line in input:
        currentValues = line.split("   ")
        leftList.append(currentValues[0])
        rightList.append(currentValues[1].strip())

    for i in range(len(leftList)):
        similarityScore = similarityScore + (int(leftList[i]) * rightList.count(leftList[i]))

    return similarityScore


# print(part1(inputLines))
print(part2(inputLines))