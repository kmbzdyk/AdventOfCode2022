#!/usr/local/bin/groovy
int powerSum = 0

new File("input2.txt").eachLine { line ->
    List<String> lineParts = line.split(":")

    int gameId = lineParts[0].minus("Game ").toInteger()

    Map<String, Integer> minCubes = [red:0, green:0, blue:0]

    List<String> gameSets = lineParts[1].replaceAll(" ", "").split(";")

    gameSets.each { set -> // for each set
        List<String> cubeNumber = set.split(",")
        cubeNumber.each { cube -> // for each cube type in a set
            minCubes.each{ key, value ->
                if (cube.contains(key) && cube.minus(key).toInteger() > value) {
                    minCubes[key] = cube.minus(key).toInteger()
                }
            }
        }

    }

    powerSum += minCubes["red"] * minCubes["green"] * minCubes["blue"]
}

println(powerSum)
// 
