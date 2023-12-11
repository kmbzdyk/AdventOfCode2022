#!/usr/local/bin/groovy
List<List<String>> map = []
List<Long> startPosition = []

int rowNum = 0
new File("input10.txt").eachLine { line ->
    map.add(line.split(""))

    if (startPosition == [] && line.contains("S")) {
        startPosition.add(rowNum)
        startPosition.add(line.indexOf('S'))
    }
    rowNum++
}

List<List<Long>> currentPositions = []
List<List<Long>> previousPositions = []
// find 2 positions from S
for (int i = startPosition[0]-1; i <= startPosition[0]+1; i++) {
    if (i == startPosition[0]) {
        if (["-", "L", "F"].contains(map[i][startPosition[1]-1])) {
            currentPositions.add([i, startPosition[1]-1])
        }

        if (["-", "J", "7"].contains(map[i][startPosition[1]+1])) {
            currentPositions.add([i, startPosition[1]+1])
        }
    } else if (i == startPosition[0] - 1) {
        if (["|", "F", "7"].contains(map[i][startPosition[1]])) {
            currentPositions.add([i, startPosition[1]])
        }
    } else if (i == startPosition[0] + 1) {
        if (["|", "L", "J"].contains(map[i][startPosition[1]])) {
            currentPositions.add([i, startPosition[1]])
        }
    }
}
previousPositions.add(startPosition)
previousPositions.add(startPosition)

// for each position find the next position, as long as they don't meet or are next to each other
boolean loopCompleted = false
int stepCount = 0
while(!loopCompleted) {
    if (currentPositions[0] == currentPositions[1]) {
        loopCompleted = true
    } else if (currentPositions[0] == previousPositions[1]) {
        loopCompleted = true
        stepCount--
    }

    for (int i = 0; i < currentPositions.size(); i++) {
        List<Long> tempPrevious = currentPositions[i]
        currentPositions[i] = findNextPos(map[currentPositions[i][0]][currentPositions[i][1]], currentPositions[i], previousPositions[i])
        previousPositions[i] = tempPrevious
    }

    stepCount++
}

def findNextPos(String instruction, List<Long> currentPos, List<Long> previousPos) {
    List<Long> nextPos = []

    if (instruction == "|") {
        if (previousPos == [currentPos[0]-1, currentPos[1]]) {
            nextPos = [currentPos[0]+1, currentPos[1]]
        } else {
            nextPos = [currentPos[0]-1, currentPos[1]]
        }
    } else if (instruction == "-") {
        if (previousPos == [currentPos[0], currentPos[1]-1]) {
            nextPos = [currentPos[0], currentPos[1]+1]
        } else {
            nextPos = [currentPos[0], currentPos[1]-1]
        }
    } else if (instruction == "L") {
        if (previousPos == [currentPos[0]-1, currentPos[1]]) {
            nextPos = [currentPos[0], currentPos[1]+1]
        } else {
            nextPos = [currentPos[0]-1, currentPos[1]]
        }
    } else if (instruction == "J") {
        if (previousPos == [currentPos[0]-1, currentPos[1]]) {
            nextPos = [currentPos[0], currentPos[1]-1]
        } else {
            nextPos = [currentPos[0]-1, currentPos[1]]
        }
    } else if (instruction == "7") {
        if (previousPos == [currentPos[0], currentPos[1]-1]) {
            nextPos = [currentPos[0]+1, currentPos[1]]
        } else {
            nextPos = [currentPos[0], currentPos[1]-1]
        }
    } else if (instruction == "F") {
        if (previousPos == [currentPos[0], currentPos[1]+1]) {
            nextPos = [currentPos[0]+1, currentPos[1]]
        } else {
            nextPos = [currentPos[0], currentPos[1]+1]
        }
    }
    return nextPos
}

println(stepCount)

// 6842
