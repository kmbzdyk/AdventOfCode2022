inputFile = open('aoc6input.txt', 'r')
inputLines = inputFile.readlines()

def part1(input):
    currentStream = []
    completedPacket = []

    for x in range(3):
        completedPacket.append(input[0][x])
        currentStream.append(input[0][x])

    for charIndex in range(len(input[0])):
        currentStream.append(input[0][charIndex+3]) # update current stream

        presentChars = set()
        duplicates = [x for x in currentStream if x in presentChars or presentChars.add(x)] # find duplicates

        completedPacket.append(input[0][charIndex+3])
        if len(duplicates) is 0: # detect start-of-packet marker
            return len(completedPacket)
        currentStream.pop(0)

def part2(input):
    currentStream = []
    completedPacket = []

    for x in range(13):
        completedPacket.append(input[0][x])
        currentStream.append(input[0][x])

    for charIndex in range(len(input[0])):
        currentStream.append(input[0][charIndex+13]) # update current stream

        presentChars = set()
        duplicates = [x for x in currentStream if x in presentChars or presentChars.add(x)] # find duplicates

        completedPacket.append(input[0][charIndex+3])
        if len(duplicates) is 0: # detect start-of-message marker
            return len(completedPacket)
        currentStream.pop(0)

print(part1(inputLines))
print(part2(inputLines))