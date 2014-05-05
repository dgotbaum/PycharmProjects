#First collumn : Connections IP>IP
#Second collumn : Duration of connection
#Third collumn : Start times

# TODO: Graph Duration against start times

__author__ = 'dgotbaum'
def seconds(start,end):
    newTime = start.split(":")
    startMinute = eval(newTime[1])
    startSecond = eval(newTime[2]) + (startMinute*60)


    newEnd = end.split(":")
    endMinute = eval(newEnd[1])
    endSecond = eval(newEnd[2]) +(endMinute*60)


    result = endSecond - startSecond
    return result
def numSecs(start):
    time = start.split(":")
    startMinute = eval(time[1])
    startSecond = eval(time[2]) + (startMinute*60)
    return startSecond
def main():
    fileName = input("what is the file name?")
    f = open(fileName,"r")
    starts = {}
    ends = {}
    F =[]
    #With the open file, this separates the timestamp, connection, and flag from each line and adds it to correct dictionary
    for line in f:
        if len(line) >1:
            #time of connection
            time = line[:15]

            #what is happening
            stamp = line[line.find("[")+1]
            lineList = line.split(" ")
            print(stamp)
            #print(time)

            #IP's in connection
            connection = lineList[2]+lineList[3]+lineList[4]
            #print(connection)
            if stamp == "S":
                starts[connection] = time
            elif stamp == "F":
                F.append(connection)
            elif stamp == "R":
                ends[connection] = time
            elif stamp == "." and (connection in F):
                ends[connection] = time

    for key in starts.keys():
        if key in ends.keys():
            print(seconds(starts[key],ends[key])," ",numSecs(starts[key]))






main()