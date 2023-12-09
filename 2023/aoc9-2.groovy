#!/usr/local/bin/groovy
Long sumOfValues = 0
List<List<Long>> input = []

new File("input9.txt").eachLine { line ->
    List<String> numbersToConvert = line.split(" ")
    List<Long> numbersConverted = []

    for (int i = 0; i < numbersToConvert.size(); i++) {
        numbersConverted.add(Long.valueOf(numbersToConvert[i]))
    }
    input.add(numbersConverted)
}

for (int i = 0; i < input.size(); i++) {
    List<List<Long>> numbersTransformed = []
    List<Long> numbersAnalysed = input[i]

    while(!checkAllZeros(numbersAnalysed)) {
        List<Long> numberDifferences = []

        for (int j = 0; j < numbersAnalysed.size()-1; j++) {
            numberDifferences.add(numbersAnalysed[j+1] - numbersAnalysed[j])
        }

        numbersAnalysed = numberDifferences
        numbersTransformed.add(numberDifferences)
    }

    Long numToSubtract = 0
    for (int j = numbersTransformed.size()-2; j >= 0 ; j--) {
        numToSubtract = numbersTransformed[j][0] - numToSubtract
    }

    sumOfValues += input[i][0] - numToSubtract
}

def checkAllZeros(List<Long> toCheck) {
    boolean allZeros = true
    for (int i = 0; i < toCheck.size(); i++) {
        if (toCheck[i] != 0) {
            allZeros = false
            break
        }
    }
    return allZeros
}

println(sumOfValues)

// 1089
