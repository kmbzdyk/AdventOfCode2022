inputFile = open('aoc4input.txt', 'r')
inputLines = inputFile.readlines()

def part1(input):
    containedPairs = 0

    for line in input:
        firstPair,secondPair = line.split(",")
        firstPairStart, firstPairEnd = firstPair.split("-")
        secondPairStart, secondPairEnd = secondPair.strip().split("-")
        firstPairStart, firstPairEnd, secondPairStart, secondPairEnd = [int(x) for x in [firstPairStart, firstPairEnd, secondPairStart, secondPairEnd]]

        if ((firstPairStart >= secondPairStart and firstPairEnd <= secondPairEnd) or 
            (secondPairStart >= firstPairStart and secondPairEnd <= firstPairEnd)):
            containedPairs += 1

    return containedPairs

def part2(input):
    containedPairs = 0

    for line in input:
        firstPair,secondPair = line.split(",")
        firstPairStart, firstPairEnd = firstPair.split("-")
        secondPairStart, secondPairEnd = secondPair.strip().split("-")
        firstPairStart, firstPairEnd, secondPairStart, secondPairEnd = [int(x) for x in [firstPairStart, firstPairEnd, secondPairStart, secondPairEnd]]

        if ((firstPairStart >= secondPairStart and firstPairStart <= secondPairEnd) or 
            (firstPairEnd >= secondPairStart and firstPairEnd <= secondPairEnd) or
            (secondPairStart >= firstPairStart and secondPairStart <= firstPairEnd) or
            (secondPairEnd >= firstPairStart and secondPairEnd <= firstPairEnd)):
            containedPairs += 1

    return containedPairs

    
print(part1(inputLines))
print(part2(inputLines))