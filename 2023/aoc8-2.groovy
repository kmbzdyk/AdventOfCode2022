#!/usr/local/bin/groovy
BigInteger totalSteps = 0
List<String> currentNodes = []
List<BigInteger> nodeSteps = []
boolean allNodesDone = false

List<String> instructions = []
Map<String,List<String>> nodes = [:]

new File("input8.txt").eachLine { line ->
    if (line.contains("=")) {
        List<String> lineParts = line.split("=")
        lineParts[1] = lineParts[1].replaceAll("\\(", "").replaceAll("\\)", "").replaceAll(" ", "")
        List<String> destinations = lineParts[1].split(",")
        nodes[lineParts[0].trim()] = [destinations[0], destinations[1]]

        if (lineParts[0].trim().split("")[2] == 'A') {
            currentNodes.add(lineParts[0].trim())
        }
    } else if (line != "") {
        instructions = line.split("")
    }
}

// println(currentNodes)
for (int j = 0; j < currentNodes.size(); j++) {
    nodeSteps[j] = 0
    while(currentNodes[j].split("")[2] != 'Z') {
        for (int i = 0; i < instructions.size(); i++) {
            if (instructions[i] == 'L') {
                currentNodes[j] = nodes[currentNodes[j]][0]
            } else if (instructions[i] == 'R') {
                currentNodes[j] = nodes[currentNodes[j]][1]
            }
            nodeSteps[j]++
            if (currentNodes[j].split("")[2] == 'Z') { break }
        }
    }
}

BigInteger result = nodeSteps[0]
for(int i = 0; i < nodeSteps.size(); i++) {
    BigInteger currentStep = nodeSteps[i]
    result = lcm2(result, currentStep)
}

for (int j = 0; j < nodeSteps.size(); j++) {
    totalSteps += nodeSteps[j] * result.divide(nodeSteps[j])
}

println(totalSteps / currentNodes.size())

def gcd(BigInteger a, BigInteger b) {
    while (b > 0) {
        BigInteger temp = b
        b = a % b
        a = temp
    }
    return a;
}

def lcm2(BigInteger a, BigInteger b) {
    return a * (b / gcd(a, b));
}

// 13289612809129
