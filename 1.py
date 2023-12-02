puzzleInput = open(".\\PowerShell\\AoC\\1.txt").read().split('\n')
numbersList = ['1','2','3','4','5','6','7','8','9','0','one','two','three','four','five','six','seven','eight','nine']

def LocateStartAndEnd(puzzleLine, start, end):
    #Assume numbersList and puzzleLine are correct types!
    for num in numbersList:
        if (start is False and puzzleLine.startswith(num)):
            start = num if numbersList.index(num) < 10 else numbersList[(numbersList.index(num) - 10)]
        if (end is False and puzzleLine.endswith(num)):
            end = num if numbersList.index(num) < 10 else numbersList[(numbersList.index(num) - 10)]
    if start and end: return int(str(start + end))
    if start is False: puzzleLine = puzzleLine[1:]
    if end is False: puzzleLine = puzzleLine[:-1]
    return LocateStartAndEnd(puzzleLine, start, end)

partTwoAnswers = []
for line in puzzleInput:
    partTwoAnswers.append(LocateStartAndEnd(line,False,False))
print(str(sum(partTwoAnswers)))
