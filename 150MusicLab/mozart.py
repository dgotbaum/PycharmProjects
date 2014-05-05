#August Olsen and Andrew Winslow
#We have adhered to the honor code
#4/6/13

import soundwave
import random

minuetTable = []
trioTable = []
dur = 0.3

def extractMinuet():
    inputFile = open("mTable.txt","r")
    for line in inputFile:
        minuetTable.append(line.split(" "))
def extractTrio():
    inputFile = open("tTable.txt","r")
    for line in inputFile:
        trioTable.append(line.split(" "))
def generateMinuet():
    minuet = []
    for i in range(16):
        rInt = random.randrange(11)
        temp = minuetTable[rInt]
        minuet.append(temp[i])
    return minuet
def generateTrio():
    trio = []
    for i in range(16):
        rInt = random.randrange(6)
        temp = trioTable[rInt]
        trio.append(temp[i])
    return trio
def getMinuet(n):
    string = '../Mfiles/M' + str(n) + '.wav'
    return string
def getTrio(n):
    string = '../Tfiles/T' + str(n) + '.wav'
    return string
def main():
    extractMinuet()
    extractTrio()
    TRIO = generateTrio()
    MINUET = generateMinuet()
    print(MINUET)
    print(TRIO)

    music = soundwave.Soundwave()
    for num in MINUET:
        measure = soundwave.Soundwave(getMinuet(eval(num)))
        music.concat(measure)
    for num in TRIO:
        measure = soundwave.Soundwave(getTrio(eval(num)))
        music.concat(measure)
    for num in MINUET:
        measure = soundwave.Soundwave(getMinuet(eval(num)))
        music.concat(measure)
    music.play()



main()