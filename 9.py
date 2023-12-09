puzzleInput = open(".\\Python\\AoC\\9.txt").read().split('\n')

def InterpretNumbers(line):
    numbersToList = []
    for input in line.split(' '): numbersToList.append(int(input))
    return numbersToList

def IsAllZeroes(numberList):
    if numberList[0] == 0 and numberList[-1] == 0:
        return True

def ListDifferences(numberList):
    differencesList = []
    listIter = 0
    while listIter < len(numberList) - 1:
        differencesList.append(numberList[listIter + 1] - numberList[listIter])
        listIter += 1
    return differencesList

def AllListsToZero(numberList):
    listsToZero = []
    listsToZero.append(numberList)
    currentList = listsToZero[0]
    while not IsAllZeroes(currentList):
        currentList = ListDifferences(currentList)
        listsToZero.append(currentList)
    return listsToZero

def AddNumber(numberList, difference, forward):
    if forward:
        lastNumber = numberList[-1]
        numberList.append(lastNumber + difference)
    else:
        firstNumber = numberList[0]
        numberList.insert(0, firstNumber - difference)
    return numberList

def RetrieveNewNumber(numberList, forward):
    listsToZero = AllListsToZero(numberList)
    numberToAdd = 0
    lastListIndex = len(listsToZero) - 1
    while len(listsToZero) > 0:
        currentList = listsToZero.pop(lastListIndex)
        lastListIndex -= 1
        currentList = AddNumber(currentList, numberToAdd, forward)
        if forward:
            numberToAdd = currentList[-1]
        else:
            numberToAdd = currentList[0]
    return numberToAdd

listOfLines = []
for line in puzzleInput:
    listOfLines.append(InterpretNumbers(line))

answersList1 = []
answersList2 = []
for numberList in listOfLines:
    answersList1.append(RetrieveNewNumber(numberList, True))
    answersList2.append(RetrieveNewNumber(numberList, False))
    
print(sum(answersList1))
# 2043183816
print(sum(answersList2))
# 1118
