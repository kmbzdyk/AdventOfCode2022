#!/usr/local/bin/groovy
int partsSum = 0
List<Map <Integer, String>> schematic = []

int rowNumber = 0
new File("input3.txt").eachLine { line ->
    schematic[rowNumber] = []

    for (int i = 0; i < line.length(); i++) { // for each char
        schematic[rowNumber][i] =  line.substring(i,i+1)
    }

    rowNumber += 1
}

for (int i = 0; i < schematic.size(); i++) { // for each line
    String currentNumber = ""
    boolean isPartNumber = false

    for (int j = 0; j < schematic[i].size(); j++) { // for each char
        if (schematic[i][j].isNumber()) {
            currentNumber += schematic[i][j]

            if (!isPartNumber) {
                for (int k = (i-1); k < (i+2); k++) { // column
                    for (int l = (j-1); l < (j+2); l++) { // row
                        if (k >= 0 && l >= 0 && k < schematic.size() && l < schematic[k].size()) {
                            if (!schematic[k][l].isNumber() && schematic[k][l] != ".") {
                                isPartNumber = true
                                break
                            }
                        }
                    }
                }
            }
        } else if (schematic[i][j] == ".") {
            if (currentNumber != "" && isPartNumber) {
                partsSum += currentNumber.toInteger()
            }
            currentNumber = ""
            isPartNumber = false
        } else {
            if (currentNumber != "" && isPartNumber) {
                partsSum += currentNumber.toInteger()
            }
            currentNumber = ""
            isPartNumber = false
        }

        if (j == schematic[i].size() - 1 && currentNumber != "" && isPartNumber) { // in case the line finished with a number
            partsSum += currentNumber.toInteger()
        }
    }
}

println(partsSum)
// 520019
