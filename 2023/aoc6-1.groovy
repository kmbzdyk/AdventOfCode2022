#!/usr/local/bin/groovy
Long waysToWinMultiplied = 1
List<String> times = []
List<String> distances = []

new File("input6.txt").eachLine { line ->
    if (line.contains("Time")) {
        times = line.minus("Time:      ").split("   ")
    } else if (line.contains("Distance")) {
        distances = line.minus("Distance:  ").split("   ")
    }
}

for (int i = 0; i < times.size(); i++) {
    List<Integer> possibleDistances = []

    for (int j = 1; j < times[i].trim().toInteger(); j++) {
        int distance = (times[i].trim().toInteger() - j) * j
        if (distance > distances[i].trim().toInteger()) {
            possibleDistances.add(distance)
        }
    }
    waysToWinMultiplied *= possibleDistances.size()

}

println(waysToWinMultiplied)
// 5133600
