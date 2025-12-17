import os

input = open(os.path.join(os.path.dirname(__file__),"day1InputTest"),"r")
inputList = input.read().split()

def problemOne():
    comboValue = 50
    zeroLandCounter = 0

    for i in inputList:
        # Parse numbers out from value
        value = int(i.lstrip("LR"))

        if i[0] == "L":
            comboValue -= value
            # Check if the value has passed zero in the negative direction 
            while comboValue < 0:
                comboValue += 100
        else:
            comboValue += value
            # Check if the value has passed zero in the positive direction 
            while comboValue > 99:
                comboValue -= 100

        if comboValue == 0:
            zeroLandCounter += 1

    print("Times hit zero: " + str(zeroLandCounter))


def problemTwo():
    comboValue = 50
    completeTurns = 0
    changeDistance = 0
    
    for i in inputList:
        fullDistance = int(i.lstrip("LR"))

        # Reduce change down to under 100 & break out reamining distance
        changeDistance = fullDistance % 100
        completeTurns += fullDistance // 100

        # Determine if remaining distance causes a turn
        if i[0] == "L":
            if changeDistance > comboValue:
                if comboValue != 0:
                    completeTurns += 1
                comboValue = comboValue - changeDistance + 100
            else:
                comboValue -= changeDistance

        else:
            if changeDistance + comboValue > 100:
                completeTurns += (changeDistance + comboValue) // 100
            #Move to new value
            comboValue = (comboValue + changeDistance) % 100
        
        # Case of landing on 0 after movement
        if comboValue == 0 and changeDistance > 0:
            completeTurns += 1
        
        print("Complete turns after loop:", completeTurns)

    print("Times zero showed up:", str(completeTurns))

#problemOne()
problemTwo()