import re
puzzleInput = open(".\\Python\\AoC\\6.txt").read().split('\n')

times = []; distance = []
for time in re.findall("\\d+",puzzleInput[0]): times.append(int(time))
for dist in re.findall("\\d+",puzzleInput[1]): distance.append(int(dist))

partTwoTime = ""; partTwoDistance = ""
for time in re.findall("\\d+",puzzleInput[0]): partTwoTime += time
for dist in re.findall("\\d+",puzzleInput[1]): partTwoDistance += dist

def DistanceTravelled(time, power):
    return power * (time - power)

def RecordBroken(dist, record):
    return dist > int(record)

def TotalRecords(time, dist):
    milli = 0
    NewRecord = 0
    while milli < time:
        if (RecordBroken(DistanceTravelled(time,milli),dist)):
            NewRecord += 1
        milli += 1
    return NewRecord

def CalculatePartOne(recordKeeper):
    finalAnswer = recordKeeper.pop(0)
    for record in recordKeeper:
        finalAnswer *= record
    return finalAnswer

recordKeeper = []
thisRace = 0
while thisRace < len(times):
    recordKeeper.append(TotalRecords(times[thisRace],distance[thisRace]))
    thisRace += 1

partTwoAnswer = TotalRecords(int(partTwoTime),int(partTwoDistance))

print(CalculatePartOne(recordKeeper)) #211904
print(partTwoAnswer)
