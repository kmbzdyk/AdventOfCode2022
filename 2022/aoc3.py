inputFile = open('aoc3input.txt', 'r')
inputLines = inputFile.readlines()
itemPriorities = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def part1(input):
    sumOfItemPriorities = 0

    for line in input:
        firstCompartment = line[0:int(len(line)/2)]
        secondCompartment = line[int(len(line)/2):len(line)]

        wrongItemType = ''.join(set(firstCompartment).intersection(secondCompartment))

        sumOfItemPriorities += itemPriorities.index(wrongItemType) + 1
    return sumOfItemPriorities

def part2(input):
    sumOfBadgePriorities = 0

    for group in range(1, int(len(input)/3)+1):
        badgeItemType = ''.join(set(
                ''.join(set(input[(group*3)-3]).intersection(input[(group*3)-2]))
            ).intersection(input[(group*3)-1]))

        sumOfBadgePriorities += itemPriorities.index(badgeItemType.strip()) + 1
    return sumOfBadgePriorities
    
print(part1(inputLines))
print(part2(inputLines))