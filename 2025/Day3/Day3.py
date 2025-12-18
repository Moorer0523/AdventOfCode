import os, math

input = open(os.path.join(os.path.dirname(__file__), "Input"), "r")
inputList = input.read().split()

def findMaxPower(bank, limit):
    max1 = 0
    maxIndex = 0
    max2 = 0
    index = 0
    for i in range(10):
            #define search value
            search = str(9-i)

            #find first index of serch value
            index = bank[maxIndex:].find(search)

            #if search value isn't at end of list, place as max
            if index+1 < len(bank) and index != -1:
                if max1 == 0:
                    max1 = search
                    maxIndex = index
                    #check if max2 is populated and return
                    if max2 != 0:
                        break
                    #check if search value exists in remainder of string
                    elif bank[index+1:].find(search) > -1 and max2 == 0:
                        max2 = search
                        break
                else:
                    max2 = search
                    break
            #if value at end of str, set to 2nd max
            elif index+1 == len(bank):
                max2 = search
    return int(f"{max1}{max2}")

def problemOne():
    outputSum = 0
    for i in inputList:
        outputSum += findMaxPower(i, 2)
    print(outputSum)

#start day 2

def findLargestVolt(bank):
    joltDict = {}
    optimalDict = {}
    startingIndex = 0
    currIndex = 0
    protectedNumbers = 11
    maxJolt = ""

    #convert to dict
    for i in range(len(bank)):
        joltDict[i]=bank[i]

    #find largest number in range of possible options
    while protectedNumbers > -1:
        currIndex = startingIndex
        for j in range(startingIndex, len(bank) - protectedNumbers):
            if joltDict[j] > joltDict[currIndex]:
                currIndex = j
        optimalDict[currIndex] = joltDict[currIndex]
        startingIndex = currIndex + 1
        protectedNumbers -= 1
        
    #reassamble into string
    for key in optimalDict.keys():
        maxJolt += optimalDict[key]

    #return cast as int
    print(maxJolt)
    return int(maxJolt)

def problemTwo():
    outputSum = 0
    for val in inputList:
        outputSum += findLargestVolt(val)
    print(outputSum)

problemTwo()
# problemOne()
