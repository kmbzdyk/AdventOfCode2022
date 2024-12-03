inputFile = open('aoc2input.txt', 'r')
inputLines = inputFile.readlines()

def isReportSafe(report):
    order = ""
    safe = True

    for i in range(len(report) - 1):
        if safe:
            if order == "":
                if int(report[i].strip()) > int(report[i + 1].strip()):
                    order = "d"

                    if (int(report[i].strip()) - int(report[i + 1].strip())) > 3:
                        safe = False
                elif int(report[i].strip()) < int(report[i + 1].strip()):
                    order = "i"

                    if (int(report[i + 1].strip()) - int(report[i].strip())) > 3:
                        safe = False
                else:
                    safe = False
            elif safe == False:
                print("unsafe - do nothing")
            else:
                if int(report[i].strip()) > int(report[i + 1].strip()):
                    if order != "d":
                        safe = False
                    else:
                        if (int(report[i].strip()) - int(report[i + 1].strip())) > 3:
                            safe = False
                elif int(report[i].strip()) < int(report[i + 1].strip()):
                    if order != "i":
                        safe = False
                    else:
                        if (int(report[i + 1].strip()) - int(report[i].strip())) > 3:
                            safe = False
                else:
                    safe = False
    return safe

def part1(input):
    safeReportsCount = 0

    for line in input:
        currentReport = line.split(" ")
        
        if isReportSafe(currentReport):
            safeReportsCount += 1

    return safeReportsCount

def part2(input):
    safeReportsCount = 0

    for line in input:
        currentReport = line.split(" ")

        if isReportSafe(currentReport):
            safeReportsCount += 1
        else:
            isReallySafe = False

            for i in range(len(currentReport)):
                modifiedArray = currentReport.copy()
                modifiedArray.pop(i)

                if isReportSafe(modifiedArray):
                    isReallySafe = True
                    break

            if isReallySafe:
                safeReportsCount += 1

    return safeReportsCount


# print(part1(inputLines))
print(part2(inputLines))