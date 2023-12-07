#!/usr/local/bin/groovy
BigInteger time = 0
BigInteger distance = 0
BigInteger countWins = 0

new File("input6.txt").eachLine { line ->
    if (line.contains("Time")) {
        time = new BigInteger(line.minus("Time:      ").replaceAll(" ", ""))
    } else if (line.contains("Distance")) {
        distance = new BigInteger(line.minus("Distance:  ").replaceAll(" ", ""))
    }
}

List<BigInteger> possibleDistances = []

for (BigInteger j = 1; j < time; j++) {
    BigInteger distanceTemp = (time - j) * j
    if (distanceTemp > distance) {
        countWins++
    }
}

println(countWins)

// 40651271
