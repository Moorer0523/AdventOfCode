import os, math

input = open(os.path.join(os.path.dirname(__file__), "Input"), "r")
inputList = input.read().split()


def checkIfOpen(row, column):
    rollCount = 0
    #prevent negative indexing
    if column == 0:
        startIndex = 0
    else:
        startIndex = column - 1

    #check if above exists
    #print(f"Checking for @ in {row}, {column}")
    if row > 0:
        rollCount += inputList[row-1].count('@',startIndex, column + 2)
    #check if below exists
    if row < len(inputList)-1:
        rollCount += inputList[row+1].count('@',startIndex, column + 2)
    #check current row
    rollCount += inputList[row].count('@',startIndex, column + 2)

    #print(f"Found {rollCount} nearby rolls")
    if rollCount > 4:
        return False
    else:
        return True

def findOpenRolls(row):
    openRollList = []
    start = 0
    end = len(inputList[row])
    searchIndex = inputList[row].find('@', start, end)
    while searchIndex > -1:
        #print(f"Searching row {row} from {start} to {end}")
        if checkIfOpen(row,searchIndex):
            #print(f"Found an open roll in row {row} at {searchIndex}")
            openRollList.append([row,searchIndex])
        searchIndex = inputList[row].find('@', searchIndex+1, end)

    #print(f"Found {len(openRollList)} open rolls in row {row}")
    return openRollList

def removeOpenRolls(openRollList):
    for coord in openRollList:
        inputList[coord[0]] = inputList[coord[0]][:coord[1]] + '.' + inputList[coord[0]][coord[1]+1:]

def problemOne():
    totalOpenRolls = 0
    for i in range(len(inputList)):
        totalOpenRolls += len(findOpenRolls(i))
    print(totalOpenRolls)


def problemTwo():
    totalOpenRolls = 0
    allOpenRolls = []
    loopCheck = True
    while loopCheck:
        for i in range(len(inputList)):
            rowOpenRolls = findOpenRolls(i)
            if len(rowOpenRolls) > 0 :
                totalOpenRolls += len(rowOpenRolls)
                allOpenRolls.append(rowOpenRolls)

        for j in allOpenRolls:
            removeOpenRolls(j)
        if len(allOpenRolls) == 0:
            print("No more open rolls")
            print(totalOpenRolls)
            loopCheck = False
        else:
            allOpenRolls.clear()


#problemOne()

# print(inputList[0])
# removeOpenRolls(findOpenRolls(0))
# print(inputList[0])

problemTwo()