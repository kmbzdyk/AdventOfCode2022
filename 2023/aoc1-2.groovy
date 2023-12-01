#!/usr/local/bin/groovy
int calibrationSum = 0
Map<String, String> wordToNumber = [one:"1", two:"2", three:"3", four:"4", five:"5", six:"6", seven:"7", eight:"8", nine:"9"]

new File("input1.txt").eachLine { line ->
    String firstDigit = null
    String lastDigit = null

    for (int i = 0; i < line.length(); i++) {
        if (line.substring(i,i+1).isNumber()) {
            if (firstDigit == null) {
                firstDigit = line.substring(i,i+1)
            }

            lastDigit = line.substring(i,i+1)
        } else {
            wordToNumber.each { key, value ->
                if (line.length() >= i + key.length() && line.substring(i,i+key.length()) == key) {
                    if (firstDigit == null) {
                        firstDigit = wordToNumber[key]
                    }

                    lastDigit = wordToNumber[key]
                } 
            }
        }
    }

    String finalNumber = firstDigit + lastDigit

    calibrationSum += finalNumber.toInteger()
}

println(calibrationSum)
// 54845
