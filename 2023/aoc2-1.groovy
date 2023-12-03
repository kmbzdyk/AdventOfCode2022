#!/usr/local/bin/groovy
int idSum = 0

Map<String, Integer> maxCubes = [red:12, green:13, blue:14]

new File("input2.txt").eachLine { line ->
    List<String> lineParts = line.split(":")

    int gameId = lineParts[0].minus("Game ").toInteger()

    boolean gamePossible = true

    List<String> gameSets = lineParts[1].replaceAll(" ", "").split(";")

    gameSets.each { set -> // for each set
        List<String> cubeNumber = set.split(",")
        cubeNumber.each { cube -> // for each cube type in a set
            maxCubes.each{ key, value ->
                if (cube.contains(key) && cube.minus(key).toInteger() > value) {
                    gamePossible = false
                }
            }
        }

    }

    if (gamePossible) { idSum += gameId }
}

println(idSum)
// 
