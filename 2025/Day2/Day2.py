import os, math

input = open(os.path.join(os.path.dirname(__file__), "Input"), "r")
inputList = input.read().split(",")


def problemOne():
    invalidNumberSum = 0

    # build ranges
    for i in inputList:
        # build range to check
        x = i.split("-")
        currentRange = range(int(x[0]), int(x[1]))

        for num in currentRange:
            # convert to string, split in half and compare. If equal, add to total
            numStr = str(num)
            if numStr[: len(numStr) // 2] == numStr[len(numStr) // 2 :]:
                invalidNumberSum += num

    print(invalidNumberSum)


def problemTwo():
    invalidNumberSum = 0
    # build ranges
    for i in inputList:
        # build range to check
        x = i.split("-")
        currentRange = range(int(x[0]), int(x[1]) + 1)
        for num in currentRange:
            numStr = str(num)
            # check first 1/2 of each word for repeats
            for j in range((len(numStr) // 2)):
                if len(numStr) % (j + 1) == 0:
                    # define search value
                    search = numStr[: j + 1]
                    # define required number of repetitions
                    countMax = len(numStr) // (j + 1)
                    # count number of times search value appears in complete string
                    count = numStr.count(search)
                    # if repetition count equals max possible, add to sum and break loop
                    if count == countMax:
                        invalidNumberSum += num
                        break
    return(invalidNumberSum)


# problemOne()
problemTwo()
