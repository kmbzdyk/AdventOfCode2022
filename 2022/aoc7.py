inputFile = open('aoc7input.txt', 'r')
inputLines = inputFile.readlines()

def calculateDirectorySize(directory, directoryFiles):
    currentDirectorySize = 0

    for item in directoryFiles[directory]:
        if isinstance(item, int): # it's a file size
            currentDirectorySize += item
        else: # it's a subdirectory
            currentDirectorySize += calculateDirectorySize(item, directoryFiles)
    return currentDirectorySize

def part1(input):
    locationList = [] # stores current location path
    currentDirectory = "" # stores current folder
    directoryFiles = {} # map containing directory as key and its files as values
    sumOfDirectorySizes = 0

    for line in input:
        if "$ cd" in line: # if it's a directory
            currentCommand = line.replace("$ cd ", "").strip()

            if currentCommand == '..':
                locationList.pop(len(locationList)-1)
                locationList.pop(len(locationList)-1)
                currentDirectory = ''.join(locationList)
            else:
                locationList.append(currentCommand)
                if len(locationList)>1: locationList.append("/")

                currentDirectory = ''.join(locationList)

                directoryFiles[currentDirectory] = []
        elif any(char.isdigit() for char in line): # if it's a file
            fileSize = line.split(" ")[0]
            directoryFiles[currentDirectory].append(int(fileSize))
        elif "dir " in line: # if it's a subdirectory
            subdirectoryName = line.replace("dir ", "").strip()
            directoryFiles[currentDirectory].append(''.join(locationList) + subdirectoryName + "/")

    for directory in directoryFiles:
        directorySize = calculateDirectorySize(directory, directoryFiles)
        if directorySize <= 100000:
            sumOfDirectorySizes += directorySize

    return sumOfDirectorySizes

def part2(input):
    totalDiskSpace = 70000000
    spaceForUpdate = 30000000
    locationList = [] # stores current location path
    currentDirectory = "" # stores current folder
    directoryFiles = {} # map containing directory as key and its files as values

    for line in input:
        if "$ cd" in line: # if it's a directory
            currentCommand = line.replace("$ cd ", "").strip()

            if currentCommand == '..':
                locationList.pop(len(locationList)-1)
                locationList.pop(len(locationList)-1)
                currentDirectory = ''.join(locationList)
            else:
                locationList.append(currentCommand)
                if len(locationList)>1: locationList.append("/")

                currentDirectory = ''.join(locationList)

                directoryFiles[currentDirectory] = []
        elif any(char.isdigit() for char in line): # if it's a file
            fileSize, fileName = line.split(" ")
            directoryFiles[currentDirectory].append(int(fileSize))
        elif "dir " in line: # if it's a subdirectory
            subdirectoryName = line.replace("dir ", "").strip()
            directoryFiles[currentDirectory].append(''.join(locationList) + subdirectoryName + "/")

    currentFolderSizeToDelete = calculateDirectorySize("/", directoryFiles)

    unusedSpace = totalDiskSpace - currentFolderSizeToDelete
    spaceToFreeUp = spaceForUpdate - unusedSpace
    
    for directory in directoryFiles:
        directorySize = calculateDirectorySize(directory, directoryFiles)
        if directorySize >= spaceToFreeUp:
            if directorySize < currentFolderSizeToDelete:
                currentFolderSizeToDelete = directorySize

    return currentFolderSizeToDelete
    
print(part1(inputLines))
print(part2(inputLines))