#!/usr/local/bin/groovy
Long totalSteps = 0
String currentNode = 'AAA'

List<String> instructions = []
Map<String,List<String>> nodes = [:]

new File("input8.txt").eachLine { line ->
    if (line.contains("=")) {
        List<String> lineParts = line.split("=")
        lineParts[1] = lineParts[1].replaceAll("\\(", "").replaceAll("\\)", "").replaceAll(" ", "")
        List<String> destinations = lineParts[1].split(",")
        nodes[lineParts[0].trim()] = [destinations[0], destinations[1]]
    } else if (line != "") {
        instructions = line.split("")
    }
}

while(currentNode != 'ZZZ') {
    for (int i = 0; i < instructions.size(); i++) {
        if (instructions[i] == 'L') {
            currentNode = nodes[currentNode][0]
        } else if (instructions[i] == 'R') {
            currentNode = nodes[currentNode][1]
        }
        totalSteps++
        if (currentNode == 'ZZZ') { break }
    }
}

println(totalSteps)

// 20777
