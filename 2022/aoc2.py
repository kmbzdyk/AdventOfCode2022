inputFile = open('aoc2input.txt', 'r')
inputLines = inputFile.readlines()

def part1(input):
    totalScore = 0

    for line in input:
        if line[2] == "X":
            totalScore += 1
            if line[0] == "C": totalScore += 6 # win
            elif line[0] == "A": totalScore += 3 # draw
        elif line[2] == "Y":
            totalScore += 2
            if line[0] == "A": totalScore += 6 # win
            elif line[0] == "B": totalScore += 3 # draw
        elif line[2] == "Z":
            totalScore += 3
            if line[0] == "B": totalScore += 6 # win
            elif line[0] == "C": totalScore += 3 # draw
    return totalScore

def part2(input):
    totalScore = 0

    for line in input:
        if line[2] == "X": # loose
            if line[0] == "A": totalScore += 3
            elif line[0] == "B": totalScore += 1
            elif line[0] == "C": totalScore += 2
        elif line[2] == "Y": # draw
            totalScore += 3
            if line[0] == "A": totalScore += 1
            elif line[0] == "B": totalScore += 2
            elif line[0] == "C": totalScore += 3 
        elif line[2] == "Z": # win
            totalScore += 6
            if line[0] == "A": totalScore += 2
            elif line[0] == "B": totalScore += 3
            elif line[0] == "C": totalScore += 1
    return totalScore

print(part1(inputLines))
print(part2(inputLines))
