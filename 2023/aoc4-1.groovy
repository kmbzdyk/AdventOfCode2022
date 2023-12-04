#!/usr/local/bin/groovy
int pointsSum = 0

int rowNumber = 1
new File("input4.txt").eachLine { line ->
    line = line.minus("Card " + rowNumber + ": ")
    List<String> numberSet = line.split(" ")
    List<String> winningNumbers = []
    List<String> elfNumbers = []

    boolean winning = true
    for (int i = 0; i < numberSet.size(); i++) {
        if (numberSet[i].trim().isNumber()) {
            if (winning) {
                winningNumbers.add(numberSet[i].trim())
            } else {
                elfNumbers.add(numberSet[i].trim())
            }
        } else if (numberSet[i].trim() == "|") {
            winning = false
        }
    }

    int linePoints = 0

    for (int i = 0; i < elfNumbers.size(); i++) { // for each Elf's numbers
        if (winningNumbers.contains(elfNumbers[i])) {
            if (linePoints == 0) {
                linePoints = 1
            } else {
                linePoints *= 2
            }
        }
    }

    rowNumber++
    pointsSum += linePoints
}


println(pointsSum)
// 24733
