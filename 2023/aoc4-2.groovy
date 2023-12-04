#!/usr/local/bin/groovy
Integer cardsSum = 0

List<Integer> cardCopies = []

int rowNumber = 1
new File("input4.txt").eachLine { line ->
    if (cardCopies[rowNumber] == null || cardCopies[rowNumber] == 0) {
        cardCopies[rowNumber] = 1 
    } else {
        cardCopies[rowNumber]++
    }

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

    //--------------------------

    for (int j = 0; j < cardCopies[rowNumber]; j++) {
        int cardToCopy = rowNumber + 1

        for (int i = 0; i < elfNumbers.size(); i++) { // for each Elf's numbers
            if (winningNumbers.contains(elfNumbers[i])) {
                if (cardCopies[cardToCopy] == null) { cardCopies[cardToCopy] = 0 }
                cardCopies[cardToCopy] += 1
                cardToCopy++
            }
        }
    }

    rowNumber++
}

for (int i = 1; i < rowNumber; i++) {
    cardsSum = cardsSum + cardCopies[i]
}


println(cardsSum)
// 5422730
