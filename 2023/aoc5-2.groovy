#!/usr/local/bin/groovy
Long closestLocation = 0

List<List<Long>> seeds = []

int mappingIndex = -1

List<List<List<String>>> mappings = []

new File("input5.txt").eachLine { line ->
    if (line.contains("seeds")) {
        List<String> seedsRanges = line.minus("seeds: ").split(" ")

        for (int i = 0; i < seedsRanges.size()-1; i=i+2) {
            seeds.add([Long.valueOf(seedsRanges[i]), Long.valueOf(seedsRanges[i]) + Long.valueOf(seedsRanges[i + 1])])
        }
    } else if (line != "" && line[0].isNumber()) {
        mappings[mappingIndex].add(line.split(" "))
    } else if (line.contains("map:")) {
        mappingIndex++
        mappings[mappingIndex] = []
    }
}

for (int i = 0; i < mappings.size(); i++) { // for each mapping
    List<List<Long>> newSeeds = []

    while (seeds.size() > 0) {
        List<Long> currentRange = seeds.pop()

        // here check if any range in the mapping covers this seed range
        boolean foundMapping = false
        for (int j = 0; j < mappings[i].size(); j++) {
            if (currentRange[0] >= Long.valueOf(mappings[i][j][1]) && currentRange[0] < Long.valueOf(mappings[i][j][1]) + Long.valueOf(mappings[i][j][2])) {
                if (currentRange[1] <= Long.valueOf(mappings[i][j][1]) + Long.valueOf(mappings[i][j][2])) {
                    Long differenceStart = Long.valueOf(mappings[i][j][1]) + Long.valueOf(mappings[i][j][2]) - currentRange[0]
                    Long mappedStart = Long.valueOf(mappings[i][j][0]) + Long.valueOf(mappings[i][j][2]) - differenceStart
                    Long differenceEnd = Long.valueOf(mappings[i][j][1]) + Long.valueOf(mappings[i][j][2]) - currentRange[1]//14
                    Long mappedEnd = Long.valueOf(mappings[i][j][0]) + Long.valueOf(mappings[i][j][2]) - differenceEnd

                    newSeeds.add([mappedStart , mappedEnd])
                    foundMapping = true
                    break
                } else {
                    Long differenceStart = Long.valueOf(mappings[i][j][1]) + Long.valueOf(mappings[i][j][2]) - currentRange[0]
                    Long mappedStart = Long.valueOf(mappings[i][j][0]) + Long.valueOf(mappings[i][j][2]) - differenceStart

                    newSeeds.add([mappedStart,Long.valueOf(mappings[i][j][0]) + Long.valueOf(mappings[i][j][2])])
                    seeds.add([Long.valueOf(mappings[i][j][1]) + Long.valueOf(mappings[i][j][2]), currentRange[1]])
                    foundMapping = true
                    break
                }
            } else if (currentRange[1] <= Long.valueOf(mappings[i][j][1]) + Long.valueOf(mappings[i][j][2]) && currentRange[1] > Long.valueOf(mappings[i][j][1])) {
                Long differenceEnd = Long.valueOf(mappings[i][j][1]) + Long.valueOf(mappings[i][j][2]) - currentRange[1]
                Long mappedEnd = Long.valueOf(mappings[i][j][0]) + Long.valueOf(mappings[i][j][2]) - differenceEnd

                newSeeds.add([Long.valueOf(mappings[i][j][0]), mappedEnd])
                seeds.add([currentRange[0], Long.valueOf(mappings[i][j][1])])
                foundMapping = true
                break
            }
        }

        if (!foundMapping) {
            newSeeds.add(currentRange)
        }
    }

    seeds = newSeeds
}

closestLocation = seeds[0][0]
for (int i = 0; i < seeds.size(); i++) {
    if (seeds[i][0] < closestLocation) {
        closestLocation = seeds[i][0]
    }
}

println(closestLocation)
// 20191102
