import math
puzzleInput = open(".\\Python\\AoC\\8.txt").read().split('\n')

directions = puzzleInput.pop(0)
puzzleInput.pop(0)

class Route():
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right
    def GetRoute(self, route):
        if route == 'L':
            return self.left
        if route == 'R':
            return self.right
    def GetName(self):
        return self.name

def FindRoute(name):
    for route in allRoutes:
        if route.GetName() == name:
            return route
        
def HowLongIsThisRoute(start, end, stops):
    counter = 0
    dest = start
    currentRoute = FindRoute(dest)
    item = 0
    while stops != 0:
        while item < len(directions):
            dest = currentRoute.GetRoute(directions[item])
            counter += 1
            currentRoute = FindRoute(dest)
            if currentRoute.GetName().endswith(end): 
                stops -= 1
            if stops == 0: break
            item += 1
            if item == len(directions): item = 0
    return counter

allRoutes = []
startingRoutes = []
for route in puzzleInput:
    routeName = route.split(' ')[0]
    if routeName.endswith('A'): startingRoutes.append(routeName)
    allRoutes.append(
        Route(
            routeName,
            route.split('(')[1].split(',')[0],
            route.split(' ')[3].split(')')[0]
        )
    )

initialValue = []
for start in startingRoutes:
        initialValue.append(HowLongIsThisRoute(start, 'Z', 1))

# math.lcm is my cheat because I looked it up.
# I already figured the idea of multiplying the values to determine the answer
# But that doesn't reveal the lowest common multiplier
# I'm quite satisfied not writing a mathematical algorithm to solve this one.
print(math.lcm(*initialValue))
# 10151663816849

# You can tell by my implementation of "stops" that I tried other methods to solve this one
