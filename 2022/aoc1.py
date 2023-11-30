inputFile = open('aoc1input.txt', 'r')
inputLines = inputFile.readlines()

def part1(input):
    listOfCaloriesSum = []
    currentElfCalories = 0

    for line in input:
        if any(char.isdigit() for char in line):
            currentElfCalories = currentElfCalories + int(line)
        else :
            listOfCaloriesSum.append(currentElfCalories)
            currentElfCalories = 0
    return (max(listOfCaloriesSum))

def part2(input):
    listOfCaloriesSum = []
    currentElfCalories = 0

    for line in input:
        if any(char.isdigit() for char in line):
            currentElfCalories = currentElfCalories + int(line)
        else :
            listOfCaloriesSum.append(currentElfCalories)
            currentElfCalories = 0

    sortedCaloriesList = sorted(frozenset(listOfCaloriesSum), reverse=True)
    return (sortedCaloriesList[0] + sortedCaloriesList[1] + sortedCaloriesList[2])

print(part1(inputLines))
print(part2(inputLines))