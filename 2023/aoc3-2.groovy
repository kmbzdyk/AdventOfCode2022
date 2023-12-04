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

    for (int j = 0; j < schematic[i].size(); j++) { // for each char

        if (schematic[i][j] == "*") {
            int adjacentNumbers = 0
            Integer firstNumber = null
            Integer secondNumber = null

            for (int k = (i-1); k < (i+2); k++) { // column
                boolean numberRegisteredAlready = false
                for (int l = (j-1); l < (j+2); l++) { // row
                    if (k >= 0 && l >= 0 && k < schematic.size() && l < schematic[k].size()) {

                        if (schematic[k][l].isNumber() && !numberRegisteredAlready) {
                            adjacentNumbers++
                            numberRegisteredAlready = true
                            String buildNumber = schematic[k][l]
                            int rightCharPos = l+1

                            while (rightCharPos < schematic[k].size() && schematic[k][rightCharPos].isNumber()) {
                                buildNumber = buildNumber + schematic[k][rightCharPos]
                                rightCharPos += 1
                            }

                            int leftCharPos = l-1

                            while (leftCharPos >= 0 && schematic[k][leftCharPos].isNumber()) {
                                buildNumber = schematic[k][leftCharPos] + buildNumber
                                leftCharPos -= 1
                            }

                            if (firstNumber == null) {
                                firstNumber = buildNumber.toInteger()
                            } else if (secondNumber == null) {
                                secondNumber = buildNumber.toInteger()
                            }
                        } else if (!schematic[k][l].isNumber() && numberRegisteredAlready) {
                            numberRegisteredAlready = false
                        }
                    }
                }
            }

            if (adjacentNumbers == 2) {
                partsSum += firstNumber * secondNumber
            }
        }
    }
}

println(partsSum)
// 75519888
