#!/usr/local/bin/groovy
List<List<String>> map = []
List<List<String>> mapExtended = []
List<List<Long>> galaxyLocations = []
List<List<List<Long>>> galaxyPairs = []
Long sumOfLengths = 0

// read the input
new File("input11.txt").eachLine { line ->
    map.add(line.split(""))
}

// add extensions - rows
for (int i = 0; i < map.size(); i++) {
    List<String> tmp = map[i]
    if (rowEmpty(tmp)) {
        mapExtended.add(tmp)
    }
    mapExtended.add(tmp)
}

// add extensions - columns
for (int i = 0; i < mapExtended[0].size(); i++) {
    if (columnEmpty(i, mapExtended)) {
        for (int j = 0; j < mapExtended.size(); j++) {
            mapExtended[j] = mapExtended[j].plus(i+1, ".")
        }
        i++
    }
}

// find locations of galaxies
for (int i = 0; i < mapExtended.size(); i++) {
    for (int j = 0; j < mapExtended[i].size(); j++) {
        if (mapExtended[i][j] == "#") {
            galaxyLocations.add([i, j])
        }
    }
}

// find all pairs of galaxies
for (int i = 0; i < galaxyLocations.size(); i++) {
    for (int j = 0; j < galaxyLocations.size(); j++) {
        if (galaxyLocations[i] != galaxyLocations[j]) {
            Long shortestDistance = getShortestDistance(galaxyLocations[i], galaxyLocations[j])
            sumOfLengths += shortestDistance
        }
    }
}

def getShortestDistance(List<Long> galaxyA, List<Long> galaxyB) {
    Long distance = Math.abs(galaxyA[0] - galaxyB[0]) + Math.abs(galaxyA[1] - galaxyB[1])
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

def columnEmpty(int colIndex, List<List<String>> mapExtended) {
    boolean isEmpty = true

    for (int i = 0; i < mapExtended.size(); i++) {
        if (mapExtended[i][colIndex] != ".") {
            isEmpty = false
        }
    }
    return isEmpty
}

println((sumOfLengths/2))

// 9918828
