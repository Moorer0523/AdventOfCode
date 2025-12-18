import os, math

input = open(os.path.join(os.path.dirname(__file__), "InputTest"), "r")
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

def findLargestVolt(bank):
    joltDict = {}
    startingIndex = 0
    maxJolt = ""

    #convert to dict
    for i in range(len(bank)):
        joltDict[i]=bank[i]

    #find largest starting in range of possible options
    for j in range(len(bank) - 11):
        if joltDict[j] > joltDict[startingIndex]:
            startingIndex = j

    #remove numbers ahead of starting value:
    for k in range(startingIndex):
        joltDict.pop(k)

    #trim to 12 numbers
    for popValue in range(1,10):
        for key in list(joltDict):
            if len(joltDict) > 12 and int(joltDict[key]) == popValue:
                joltDict.pop(key)
        if len(joltDict) == 12:
            break

    #sort by value
    sortedTup = sorted(joltDict.items(), key=lambda value: value[1], reverse=True)

    #reassamble into string
    for index,value in sorted(sortedTup):
        if len(maxJolt) < 12:
            maxJolt += joltDict[index]

    #return cast as int
    return int(maxJolt)

def problemTwo():
    outputSum = 0
    for val in inputList:
        outputSum += findLargestVolt(val)
    print(outputSum)

problemTwo()
# problemOne()
