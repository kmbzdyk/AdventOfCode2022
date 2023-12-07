#!/usr/local/bin/groovy
BigInteger totalWinning = 0

List<List<String>> hands = []
List<List<String>> processedHands = []

new File("input7.txt").eachLine { line ->
    hands.add(line.split(" "))
}

while(hands.size() > 0) {
    // find the least strength
    int currentHandIndex = 0
    List<String> currentHand = hands[0]
    for (int i = 0; i < hands.size(); i++) {
        if (currentHand[0] != hands[i][0]) {
            if (getStrength(currentHand[0]) > getStrength(hands[i][0])) {
                currentHand = hands[i]
                currentHandIndex = i
            } else if (getStrength(currentHand[0]) == getStrength(hands[i][0])) {
                if (!compareSameStrength(currentHand[0], hands[i][0])) {
                    currentHand = hands[i]
                    currentHandIndex = i
                }
            }
        }
    }
    processedHands.add(currentHand)
    hands.remove(currentHandIndex)
}

for (int i = 0; i < processedHands.size(); i++) {
    totalWinning += Long.valueOf(processedHands[i][1]) * (i + 1) 
}

println(totalWinning)

def compareSameStrength(hand1, hand2) {
    boolean hand1Weaker = true
    Map<String, Integer> cardToValue = [x2:1, x3:2, x4:3, x5:4, x6:5, x7:6, x8:7, x9:8, xT:9, xJ:10, xQ:11, xK:12, xA:13]
    
    for (int i = 0; i < 5; i++) {
        if (hand1[i] != hand2[i]) {
            if (cardToValue["x" + hand1[i]] > cardToValue["x" + hand2[i]]) {
                hand1Weaker = false
            }
            break
        }
    }

    return hand1Weaker
}

def getStrength(hand) {
    List<String> chars = hand.split("")
    List<String> charsUnique = chars.unique(false)
    List<Integer> appearances = []

    for (int i = 0; i < charsUnique.size(); i++) {
        appearances.add(chars.count(charsUnique[i]))
    }

    if (appearances.size() == 5) {
        return 1
    } else if (appearances.size() == 4) {
        return 2
    } else if (appearances.size() == 3) {
        // three of a kind or two pairs
        if (appearances.contains(2)) {
            return 3
        } else {
            return 4
        }
    } else if (appearances.size() == 2) {
        // four of kind or full house
        if (appearances.contains(4)) {
            return 6
        } else {
            return 5
        }
    } else if (appearances.size() == 1) {
        return 7
    }
}

// 251927063
