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
            print("found", search, "at index:", index)
            print("remaining string to search", bank[index+1:])
            #if search value isn't at end of list, place as max
            if index+1 < len(bank) and index != -1:
                if max1 == 0:
                    max1 = search
                    maxIndex = index
                    print("assigned", max1, "to max1. max2 value is", max2)
                    #check if max2 is populated and return
                    if max2 != 0:
                        break
                    #check if search value exists in remainder of string
                    elif bank[index+1:].find(search) > -1 and max2 == 0:
                        print("found 2nd instance of", search)
                        max2 = search
                        break
                else:
                    max2 = search
                    print("assigned", max2, "to max2")
                    break
            #if value at end of str, set to 2nd max
            elif index+1 == len(bank):
                max2 = search
    print(f"found max of {max1}{max2}")
    return int(f"{max1}{max2}")

def problemOne():
    outputSum = 0
    for i in inputList:
        outputSum += findMaxPower(i, 2)
    print(outputSum)



problemOne()
