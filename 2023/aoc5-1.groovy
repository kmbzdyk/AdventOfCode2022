#!/usr/local/bin/groovy
Long closestLocation = 0

List<String> seeds = []
List<Long> soils = []
List<Long> fertilizers = []
List<Long> waters = []
List<Long> lights = []
List<Long> temperatures = []
List<Long> humidities = []
List<Long> locations = []

String currentCheck = ""

List<List<String>> seedToSoil = []
List<List<String>> soilToFertilizer = []
List<List<String>> fertilizerToWater = []
List<List<String>> waterToLight = []
List<List<String>> lightToTemperature = []
List<List<String>> temperatureToHumidity = []
List<List<String>> humidityToLocation = []

new File("input5.txt").eachLine { line ->
    if (line.contains("seeds")) {
        seeds = line.minus("seeds: ").split(" ")
    } else if (line == "") {
        currentCheck = ""
    } else if (line.contains("seed-to-soil")) {
        currentCheck = "seed-to-soil"
    } else if (line.contains("soil-to-fertilizer")) {
        currentCheck = "soil-to-fertilizer"

        // check seed to soil
        for (int i = 0; i < seeds.size(); i++) {
            // check if any mapping covers it
            Long mappedValue = seeds[i].toLong()
            for (int j = 0; j < seedToSoil.size(); j++) {
                if (Long.valueOf(seeds[i]) >= Long.valueOf(seedToSoil[j][1]) &&
                    Long.valueOf(seeds[i]) <= (Long.valueOf(seedToSoil[j][1]) + Long.valueOf(seedToSoil[j][2]))) {
                    Long difference = Long.valueOf(seedToSoil[j][1]) + Long.valueOf(seedToSoil[j][2]) - Long.valueOf(seeds[i])
                    mappedValue = Long.valueOf(seedToSoil[j][0]) + Long.valueOf(seedToSoil[j][2]) - difference
                }
            }
            soils[i] = mappedValue
        }
    } else if (line.contains("fertilizer-to-water")) {
        currentCheck = "fertilizer-to-water"

        // check seed to soil
        for (int i = 0; i < soils.size(); i++) {
            // check if any mapping covers it
            Long mappedValue = soils[i]
            for (int j = 0; j < soilToFertilizer.size(); j++) {
                if (soils[i] >= Long.valueOf(soilToFertilizer[j][1]) &&
                    soils[i] <= (Long.valueOf(soilToFertilizer[j][1]) + Long.valueOf(soilToFertilizer[j][2]))) {
                    Long difference = Long.valueOf(soilToFertilizer[j][1]) + Long.valueOf(soilToFertilizer[j][2]) - soils[i]
                    mappedValue = Long.valueOf(soilToFertilizer[j][0]) + Long.valueOf(soilToFertilizer[j][2]) - difference
                }
            }
            fertilizers[i] = mappedValue
        }
    } else if (line.contains("water-to-light")) {
        currentCheck = "water-to-light"

        // check seed to soil
        for (int i = 0; i < fertilizers.size(); i++) {
            // check if any mapping covers it
            Long mappedValue = fertilizers[i]
            for (int j = 0; j < fertilizerToWater.size(); j++) {
                if (fertilizers[i] >= Long.valueOf(fertilizerToWater[j][1]) &&
                    fertilizers[i] <= (Long.valueOf(fertilizerToWater[j][1]) + Long.valueOf(fertilizerToWater[j][2]))) {
                    Long difference = Long.valueOf(fertilizerToWater[j][1]) + Long.valueOf(fertilizerToWater[j][2]) - fertilizers[i]
                    mappedValue = Long.valueOf(fertilizerToWater[j][0]) + Long.valueOf(fertilizerToWater[j][2]) - difference
                }
            }
            waters[i] = mappedValue
        }
    } else if (line.contains("light-to-temperature")) {
        currentCheck = "light-to-temperature"

        // check seed to soil
        for (int i = 0; i < waters.size(); i++) {
            // check if any mapping covers it
            Long mappedValue = waters[i]
            for (int j = 0; j < waterToLight.size(); j++) {
                if (waters[i] >= Long.valueOf(waterToLight[j][1]) &&
                    waters[i] <= (Long.valueOf(waterToLight[j][1]) + Long.valueOf(waterToLight[j][2]))) {
                    Long difference = Long.valueOf(waterToLight[j][1]) + Long.valueOf(waterToLight[j][2]) - waters[i]
                    mappedValue = Long.valueOf(waterToLight[j][0]) + Long.valueOf(waterToLight[j][2]) - difference
                }
            }
            lights[i] = mappedValue
        }
    } else if (line.contains("temperature-to-humidity")) {
        currentCheck = "temperature-to-humidity"

        // check seed to soil
        for (int i = 0; i < lights.size(); i++) {
            // check if any mapping covers it
            Long mappedValue = lights[i]
            for (int j = 0; j < lightToTemperature.size(); j++) {
                if (lights[i] >= Long.valueOf(lightToTemperature[j][1]) &&
                    lights[i] <= (Long.valueOf(lightToTemperature[j][1]) + Long.valueOf(lightToTemperature[j][2]))) {
                    Long difference = Long.valueOf(lightToTemperature[j][1]) + Long.valueOf(lightToTemperature[j][2]) - lights[i]
                    mappedValue = Long.valueOf(lightToTemperature[j][0]) + Long.valueOf(lightToTemperature[j][2]) - difference
                }
            }
            temperatures[i] = mappedValue
        }
    } else if (line.contains("humidity-to-location")) {
        currentCheck = "humidity-to-location"

        // check seed to soil
        for (int i = 0; i < temperatures.size(); i++) {
            // check if any mapping covers it
            Long mappedValue = temperatures[i]
            for (int j = 0; j < temperatureToHumidity.size(); j++) {
                if (temperatures[i] >= Long.valueOf(temperatureToHumidity[j][1]) &&
                    temperatures[i] <= (Long.valueOf(temperatureToHumidity[j][1]) + Long.valueOf(temperatureToHumidity[j][2]))) {
                    Long difference = Long.valueOf(temperatureToHumidity[j][1]) + Long.valueOf(temperatureToHumidity[j][2]) - temperatures[i]
                    mappedValue = Long.valueOf(temperatureToHumidity[j][0]) + Long.valueOf(temperatureToHumidity[j][2]) - difference
                }
            }
            humidities[i] = mappedValue
        }
    } else if (currentCheck == "seed-to-soil") {
        seedToSoil.add(line.split(" "))
    } else if (currentCheck == "soil-to-fertilizer") {
        soilToFertilizer.add(line.split(" "))
    } else if (currentCheck == "fertilizer-to-water") {
        fertilizerToWater.add(line.split(" "))
    } else if (currentCheck == "water-to-light") {
        waterToLight.add(line.split(" "))
    } else if (currentCheck == "light-to-temperature") {
        lightToTemperature.add(line.split(" "))
    } else if (currentCheck == "temperature-to-humidity") {
        temperatureToHumidity.add(line.split(" "))
    } else if (currentCheck == "humidity-to-location") {
        humidityToLocation.add(line.split(" "))
    }
}

// check humidity to location
for (int i = 0; i < humidities.size(); i++) {
    // check if any mapping covers it
    Long mappedValue = humidities[i]
    for (int j = 0; j < humidityToLocation.size(); j++) {
        if (humidities[i] >= Long.valueOf(humidityToLocation[j][1]) &&
            humidities[i] <= (Long.valueOf(humidityToLocation[j][1]) + Long.valueOf(humidityToLocation[j][2]))) {
            Long difference = Long.valueOf(humidityToLocation[j][1]) + Long.valueOf(humidityToLocation[j][2]) - humidities[i]
            mappedValue = Long.valueOf(humidityToLocation[j][0]) + Long.valueOf(humidityToLocation[j][2]) - difference
        }
    }
    locations[i] = mappedValue
}

closestLocation = locations[0]
for (int i = 0; i < locations.size(); i++) {
    if (locations[i] < closestLocation) {
        closestLocation = locations[i]
    }
}

println(closestLocation)
// 600279879
