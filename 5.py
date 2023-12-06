import re
puzzleInput = open(".\\Python\\AoC\\5.txt").read().split('\n')

seeds = []
for seed in re.findall("\\d+",puzzleInput.pop(0)): seeds.append(int(seed))
puzzleInput.pop(0) #Remove first blank line

#Map the seed to its range value
partTwoSeeds = {}
seedsIter = 0
while seedsIter < len(seeds):
    startSeed = seeds[seedsIter]
    partTwoSeeds[str(startSeed)] = seeds[seedsIter + 1]
    seedsIter += 2

def InterpretLine(line):
    a,b,c = re.findall("\\d+",line)
    return(int(a),int(b),int(c))

#Return integer value of seed if it's in range (not a true/false value as name implies)
def InRange(seed,rangeInput):
    dest = rangeInput[0]; source = rangeInput[1]; rangeAdd = rangeInput[2]
    if seed >= source and seed <= (source + rangeAdd):
        return (seed + (dest - source))
    return seed

#Part 2: Used to retrieve the current range gap between seed and maximum value
def GetRange(seed,rangeInput):
    dest = rangeInput[0]; source = rangeInput[1]; rangeAdd = rangeInput[2]
    return (source + rangeAdd) - seed

#Use a bool variable to determine if we have to keep looking for a new value
#Smallest range tells me what the smallest amount of seeds I can skip is - they would all be the previous seed but +1
def CalculateSeedValue(seed, puzzleInput):
    returningSeed = seed
    findMap = True
    smallestRange = -1
    for line in puzzleInput:
        if line == '' or ':' in line:
            findMap = True
            continue
        if findMap:
            seedRef = returningSeed
            returningSeed = InRange(returningSeed,InterpretLine(line))
        if seedRef != returningSeed:
            currentRange = GetRange(seedRef,InterpretLine(line))
            if currentRange < smallestRange or smallestRange == -1: smallestRange = currentRange
            seedRef = returningSeed
            findMap = False
    return (returningSeed,smallestRange)

#Part One
values = []
for seed in seeds:
    values.append(CalculateSeedValue(seed,puzzleInput)[0])

#Part Two
#Use the mapped range to create a while loop counter
#Append current seed value, then add the smallest range to the counter to skip x seeds
partTwoValues = []
for seed in partTwoSeeds:
    startSeed = int(seed)
    baseRef = startSeed
    counter = int(partTwoSeeds[seed])
    while startSeed < baseRef + counter:
        a,b = CalculateSeedValue(startSeed,puzzleInput)
        partTwoValues.append(a)
        if b > 1: startSeed = startSeed + b
        else: startSeed = startSeed + 1

values.sort()
print("Part 1 is: " + str(values[0]))
partTwoValues.sort()
print("Part 2 is: " + str(partTwoValues[0]))
