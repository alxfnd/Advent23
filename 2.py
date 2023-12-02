import re

puzzleInput = open(".\\Python\\2.txt").read().split('\n')
validGames = []
powerOfMinimum = []
for line in puzzleInput:
    gameID = re.search(pattern="\s\\d{0,3}[:]",string=line).group()[1:-1]
    badDraw = False
    green = 0; red = 0; blue = 0
    for cubeDraw in line.split(':')[1].split(';'):
        for colourCube in cubeDraw.split(','):
            numberColour = colourCube.strip().split(' ')
            number = int(numberColour[0])
            match numberColour[1]:
                case 'green':
                    if number > green:
                        green = number
                    if number > 13:
                        badDraw = True
                case 'red':
                    if number > red:
                        red = number
                    if number > 12:
                        badDraw = True
                case 'blue':
                    if number > blue:
                        blue = number
                    if number > 14:
                        badDraw = True
    powerOfMinimum.append(red * green * blue)
    if badDraw == False:
        validGames.append(int(gameID))

print("Answer one is: " + str(sum(validGames)))
print("Answer two is: " + str(sum(powerOfMinimum)))
