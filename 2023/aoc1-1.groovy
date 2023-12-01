#!/usr/local/bin/groovy
int calibrationSum = 0

new File("input1.txt").eachLine { line ->
    String firstDigit = null
    String lastDigit = null

    for (int i = 0; i < line.length(); i++) {
        if (line.substring(i,i+1).isNumber()) {
            if (firstDigit == null) {
                firstDigit = line.substring(i,i+1)
            }

            lastDigit = line.substring(i,i+1)
        }
    }

    String finalNumber = firstDigit + lastDigit

    calibrationSum += finalNumber.toInteger()
}

println(calibrationSum)
// 55090
