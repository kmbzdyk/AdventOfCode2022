inputFile = open('aoc1input.txt', 'r')
inputLines = inputFile.readlines()

listOfCaloriesSum = []
currentElfCalories = 0

for line in inputLines:
    if any(char.isdigit() for char in line):
        currentElfCalories = currentElfCalories + int(line)
    else :
        listOfCaloriesSum.append(currentElfCalories)
        currentElfCalories = 0

sortedCaloriesList = sorted(frozenset(listOfCaloriesSum), reverse=True)
print(sortedCaloriesList[0] + sortedCaloriesList[1] + sortedCaloriesList[2])