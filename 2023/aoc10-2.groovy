#!/usr/local/bin/groovy
List<List<String>> map = []
List<Long> startPosition = []
List<List<Long>> loopPositions = []
int insideCount = 0

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

if (currentPositions[0][0] == currentPositions[1][0]) {
    map[startPosition[0]][startPosition[1]] = "-"
} else if (currentPositions[0][1] == currentPositions[1][1]) {
    map[startPosition[0]][startPosition[1]] = "|"
} else if (currentPositions[0][0] == startPosition[0]-1 || currentPositions[1][0] == startPosition[0]-1) { // L J
    if (currentPositions[0][1] == startPosition[1]+1 || currentPositions[1][1] == startPosition[1]+1) { // L
        map[startPosition[0]][startPosition[1]] = "L"
    } else { // J
        map[startPosition[0]][startPosition[1]] = "J"
    }
} else { // 7 F
    if (currentPositions[0][1] == startPosition[1]+1 || currentPositions[1][1] == startPosition[1]+1) { // F
        map[startPosition[0]][startPosition[1]] = "F"
    } else { // 7
        map[startPosition[0]][startPosition[1]] = "7"
    }
}

previousPositions.add(startPosition)
previousPositions.add(startPosition)

loopPositions.add(startPosition)
loopPositions.add(currentPositions[0])
loopPositions.add(currentPositions[1])

// for each position find the next position, as long as they don't meet or are next to each other
boolean loopCompleted = false
int stepCount = 0
while(!loopCompleted) {
    if (currentPositions[0] == currentPositions[1]) {
        loopCompleted = true
    } else if (currentPositions[0] == previousPositions[1]) {
        loopCompleted = true
    }

    for (int i = 0; i < currentPositions.size(); i++) {
        List<Long> tempPrevious = currentPositions[i]
        currentPositions[i] = findNextPos(map[currentPositions[i][0]][currentPositions[i][1]], currentPositions[i], previousPositions[i])
        previousPositions[i] = tempPrevious

        if (!loopPositions.contains(currentPositions[i])) {
             loopPositions.add(currentPositions[i])
        }
    }
}

// mark positions not belonging to the loop
for (int i = 0; i < map.size(); i++) {
    for (int j = 0; j < map[i].size(); j++) {
        if (!loopPositions.contains([i, j])) {
            map[i][j] = "."
        }
    }
}

for (int i = 0; i < map.size(); i++) {
    boolean inside = false
    String lastCorner = ""
    for (int j = 0; j < map[i].size(); j++) {
        if (map[i][j] == ".") {
            if (inside) { 
                map[i][j] = "I"
            } else {
                map[i][j] = "O"
            }
        } else if (map[i][j] == "|") {
            inside = !inside
        } else if (map[i][j] == "L") {
            lastCorner = "L"
        } else if (map[i][j] == "J") { // change
            if (lastCorner == "F") {
                inside = !inside
            }
            lastCorner = "J"
        } else if (map[i][j] == "7") {
            if (lastCorner == "L") {
                inside = !inside
            }
            lastCorner = "7"
        } else if (map[i][j] == "F") {
            lastCorner = "F"
        }
    }
}

for (int i = 0; i < map.size(); i++) {
    for (int j = 0; j < map[i].size(); j++) {
        if (map[i][j] == "I") {
            insideCount++
        }
    }
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

println(insideCount)

// 393
