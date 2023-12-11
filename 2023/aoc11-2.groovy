#!/usr/local/bin/groovy
List<List<String>> map = []
List<List<Long>> galaxyLocations = []
List<List<List<Long>>> galaxyPairs = []
List<Long> extendedRows = []
List<Long> extendedColumns = []
Long sumOfLengths = 0

// read the input
new File("input11.txt").eachLine { line ->
    map.add(line.split(""))
}

// add extensions - rows
for (int i = 0; i < map.size(); i++) {
    List<String> tmp = map[i]
    if (rowEmpty(tmp)) {
        extendedRows.add(i)
    }
}

// add extensions - columns
for (int i = 0; i < map[0].size(); i++) {
    if (columnEmpty(i, map)) {
        extendedColumns.add(i)
    }
}

// find locations of galaxies
for (int i = 0; i < map.size(); i++) {
    for (int j = 0; j < map[i].size(); j++) {
        if (map[i][j] == "#") {
            galaxyLocations.add([i, j])
        }
    }
}

// find all pairs of galaxies
for (int i = 0; i < galaxyLocations.size(); i++) {
    for (int j = 0; j < galaxyLocations.size(); j++) {
        if (galaxyLocations[i] != galaxyLocations[j]) {
            if (!galaxyPairs.contains([galaxyLocations[i], galaxyLocations[j]]) &&
                !galaxyPairs.contains([galaxyLocations[j], galaxyLocations[i]])) {
                    Long shortestDistance = getShortestDistance(galaxyLocations[i], galaxyLocations[j], extendedRows, extendedColumns)
                    sumOfLengths += shortestDistance
            }
            
        }
    }
}

def getShortestDistance(List<Long> galaxyA, List<Long> galaxyB, List<Long> extendedRows, List<Long> extendedColumns) {
    Long rowsBetween = 0
    Long columnsBetween = 0

    for (int i = 0; i < extendedRows.size(); i++) {
        if (extendedRows[i] > [galaxyA[0], galaxyB[0]].min() && extendedRows[i] < [galaxyA[0], galaxyB[0]].max()) {
            rowsBetween++
        }
    }

    for (int i = 0; i < extendedColumns.size(); i++) {
        if (extendedColumns[i] > [galaxyA[1], galaxyB[1]].min() && extendedColumns[i] < [galaxyA[1], galaxyB[1]].max()) {
            columnsBetween++
        }
    }

    Long extendedRowsToAdd = (rowsBetween * 1000000) - rowsBetween
    Long extendedColumnsToAdd = (columnsBetween * 1000000) - columnsBetween

    Long distance = Math.abs(galaxyA[0] - galaxyB[0]) + extendedRowsToAdd + Math.abs(galaxyA[1] - galaxyB[1]) + extendedColumnsToAdd

    return distance
}

def rowEmpty(List<String> row) {
    boolean isEmpty = true

    for (int i = 0; i < row.size(); i++) {
        if (row[i] != ".") {
            isEmpty = false
        }
    }
    return isEmpty
}

def columnEmpty(int colIndex, List<List<String>> map) {
    boolean isEmpty = true

    for (int i = 0; i < map.size(); i++) {
        if (map[i][colIndex] != ".") {
            isEmpty = false
        }
    }
    return isEmpty
}

println((sumOfLengths/2))

// 692506533832
