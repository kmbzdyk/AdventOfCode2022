#!/usr/local/bin/groovy
List<List<String>> currentPattern = []

Long sumOfMirrors = 0

// read the input
new File("input13.txt").eachLine { line ->
    boolean mirrorFound = false
    if (line != '') {
        currentPattern.add(line.split(''))
    } else {
        println('Analysing pattern!')
        // check if there are identical rows
        for (int i = 0; i < currentPattern.size()-1; i++) {
            // println(currentPattern[i] == currentPattern[i+1])
            // println("comparing " + currentPattern[i] + " and " + currentPattern[i+1])
            if (currentPattern[i] == currentPattern[i+1]) {
                int mirrorRows = checkIfRowsMirror(i, currentPattern)
                if (mirrorRows > -1) {
                    sumOfMirrors += mirrorRows
                    println("Adding " + mirrorRows + " rows")
                    break
                }
            }
        }

        if (!mirrorFound) {
            println("Not found rows mirror, so analysing columns")

            for (int i = 0; i < currentPattern[0].size()-1; i++) {
                boolean columnsSame = true
                for (int j = 0; j < currentPattern.size()-1; j++) {
                    if (currentPattern[j][i] != currentPattern[j][i+1]) {
                        columnsSame = false
                        break
                    }
                }

                if (columnsSame) {
                    int mirrorColumns = checkIfColumnsMirror(i, currentPattern)
                    if (mirrorColumns > -1) {
                        sumOfMirrors += mirrorColumns
                        println("Adding " + mirrorColumns + " columns")
                        break
                    }
                }
            }
        }

        currentPattern = []
    }
}

def checkIfRowsMirror(int matchedRowIndex, List<List<String>> currentPattern) { // recursive
    int matchedRowIndex2 = matchedRowIndex + 2
    matchedRowIndex -= 1 

    boolean atTheEdge = false
    boolean mirror = true
    int rowsAbove = 0

    while(!atTheEdge) {
        println("check " + currentPattern[matchedRowIndex] + " and " + currentPattern[matchedRowIndex2])
        if (matchedRowIndex < 0 || matchedRowIndex2 == currentPattern.size()) {
            // println("AT THE EDGE")
            atTheEdge = true
        } else if (currentPattern[matchedRowIndex] == currentPattern[matchedRowIndex2]) {
            // println("same")
            matchedRowIndex = matchedRowIndex - 1
            matchedRowIndex2 = matchedRowIndex2 + 1
            rowsAbove++
        } else {
            // println("not a mirror")
            mirror = false
            break
        }
    }

    if (matchedRowIndex >= 0) {
        rowsAbove += matchedRowIndex + 1
    }

    if (mirror) {
        return rowsAbove
    } else {
        return -1
    }
}

def checkIfColumnsMirror(int matchedColumnIndex, List<List<String>> currentPattern) {
    int matchedColumnIndex2 = matchedColumnIndex + 2
    matchedColumnIndex -= 1 

    boolean atTheEdge = false
    boolean mirror = true
    int columnsLeft = 0

    while(!atTheEdge) {
        if (matchedColumnIndex < 0 || matchedColumnIndex2 == currentPattern[0].size()) {
            atTheEdge = true
        } else {
            boolean columnsSame = true
            for (int j = 0; j < currentPattern.size()-1; j++) {
                if (currentPattern[j][matchedColumnIndex] != currentPattern[j][matchedColumnIndex2]) {
                    columnsSame = false
                    break
                }
            }

            if (columnsSame) {
                matchedColumnIndex = matchedColumnIndex - 1
                matchedColumnIndex2 = matchedColumnIndex2 + 1
                columnsLeft++
            } else {
                mirror = false
                break
            }
        }
    }

    if (matchedColumnIndex >= 0) {
        columnsLeft += matchedColumnIndex + 1
    }

    if (mirror) {
        return columnsLeft
    } else {
        return -1
    }
}

println(sumOfMirrors)

// 4 + 3
