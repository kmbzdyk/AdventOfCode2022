inputFile = open('aoc5input.txt', 'r')
inputLines = inputFile.readlines()

def part1(input):
    movingInstructions = [] # [x, y, z]
    stackToPosition = {} # {stack number: position in line}
    stackState = [] # contains list where each represents stack and contains its elements

    for line in input:
        if "move" in line: # instructions
            instruction = []
            for char in line:
                if char.isdigit():
                    instruction.append(int(char))
            if len(instruction) is not 3: # a bit nasty - handles 2 digit numbers
                moves = ""
                for x in range(len(instruction)-2):
                    moves += str(instruction[x])
                instruction = [int(moves),instruction[len(instruction)-2],instruction[len(instruction)-1]]
            movingInstructions.append(instruction)

        elif any(char.isdigit() for char in line): # stack number to position
            for char in line:
                if char.isdigit():
                    stackToPosition[int(char)] = line.find(char)

    for x in range(len(stackToPosition)): # create empty list for each stack
        stackState.append([])

    for line in input:
        if "[" in line: # stack elements
            for key in stackToPosition:
                if (line[stackToPosition[key]] is not ' '):
                    stackState[key-1].append(line[stackToPosition[key]])

    for stack in stackState: # revers each stack order
        stack.reverse()

    for instruction in movingInstructions: # proceed with instructions
        for x in range(instruction[0]):
            currentStack = stackState[instruction[1]-1][len(stackState[instruction[1]-1])-1] # what there is to move
        
            stackState[instruction[1]-1].pop(len(stackState[instruction[1]-1])-1) # deleting from
            stackState[instruction[2]-1].append(currentStack) # moving to

    result = ""

    for stack in stackState:
        result += stack[len(stack)-1]

    return result

def part2(input):
    movingInstructions = [] # [x, y, z]
    stackToPosition = {} # {stack number: position in line}
    stackState = [] # contains list where each represents stack and contains its elements

    for line in input:
        if "move" in line: # instructions
            instruction = []
            for char in line:
                if char.isdigit():
                    instruction.append(int(char))
            if len(instruction) is not 3: # naaaasty
                moves = ""
                for x in range(len(instruction)-2):
                    moves += str(instruction[x])
                instruction = [int(moves),instruction[len(instruction)-2],instruction[len(instruction)-1]]
            movingInstructions.append(instruction)

        elif any(char.isdigit() for char in line): # stack number to position
            for char in line:
                if char.isdigit():
                    stackToPosition[int(char)] = line.find(char)

    for x in range(len(stackToPosition)): # create empty list for each stack
        stackState.append([])

    for line in input:
        if "[" in line: # stack elements
            for key in stackToPosition:
                if (line[stackToPosition[key]] is not ' '):
                    stackState[key-1].append(line[stackToPosition[key]])

    for stack in stackState: # revers each stack order
        stack.reverse()

    for instruction in movingInstructions: # proceed with instructions
        currentStack = []

        for x in range(instruction[0]):
            currentStack.append(stackState[instruction[1]-1][len(stackState[instruction[1]-1])-1])
            stackState[instruction[1]-1].pop(len(stackState[instruction[1]-1])-1) # delete from
        currentStack.reverse() # what there is to move - reversed

        for stack in currentStack:
            stackState[instruction[2]-1].append(stack) # moving to

    result = ""
    for stack in stackState:
        result += stack[len(stack)-1]

    return result

print(part1(inputLines))
print(part2(inputLines))