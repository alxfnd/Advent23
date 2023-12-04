import re
puzzleInput = open(".\\Python\\AoC\\4.txt").read().split('\n')

pointTotals = []

# Part 2
cardCounter = []
for line in puzzleInput:
    cardCounter.append(1)

for line in puzzleInput:
    winningNumbers,toCheck = line.split(':')[1].split('|')
    winningNumbers = re.findall("[0-9]+",winningNumbers)
    toCheck = re.findall("[0-9]+",toCheck)
    currentPoints = 0
    currentWins = 0 # Part 2
    for number in winningNumbers:
        if number in toCheck:
            currentWins += 1 # Part 2
            if currentPoints == 0: currentPoints += 1 
            else: currentPoints *= 2
    pointTotals.append(currentPoints)

    #Part 2
    currentGame = int(re.search("[0-9]+",line.split(':')[0]).group())
    counter = 0
    while counter < cardCounter[currentGame - 1]:
        increaseCards = 0
        for win in range(0,currentWins):
            cardCounter[(currentGame + increaseCards)] = cardCounter[(currentGame + increaseCards)] + 1
            increaseCards += 1
        counter += 1

print(sum(pointTotals))
print(sum(cardCounter))
