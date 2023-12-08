puzzleInput = open(".\\Python\\AoC\\7.txt").read().split('\n')

# Part One

values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
cardMap = {'A': 14, 'K': 13, 'Q':12, 'J':11, 'T':10}
cardMapKeys = cardMap.keys()

class Card():
    def __init__(self, card, bid):
        super().__init__()
        self.rawCard = card
        self.cardValues = self.CardAsValues(self.rawCard)
        self.highestValue = self.GetHighestValue(self.cardValues)
        self.bid = int(bid)
        self.bestHand = self.EvaluateBestHand(self.highestValue)
    
    def CardAsValues(self, rawCard):
        cardValues = []
        for item in rawCard:
            if item.isdigit(): cardValues.append(int(item))
            if item in cardMapKeys: cardValues.append(cardMap[item])
        return cardValues

    def GetHighestValue(self, cardValues):
        highestValue = []
        for val in values:
            for thisVal in cardValues:
                if val == thisVal: highestValue.append(val)
        highestValue.sort(reverse=True)
        return highestValue
    
    def EvaluateBestHand(self, cardValues):
        uniqueValues = 0
        currentValue = 0
        ofAKind = 0
        tally = 0
        for value in cardValues:
            if value != currentValue:
                if tally > ofAKind: ofAKind = tally
                currentValue = value
                uniqueValues += 1
                tally = 1
            else: tally += 1
        if tally > ofAKind: ofAKind = tally
        match ofAKind:
            case 5: return 6 #5 of a kind
            case 4: return 5 #4 of a kind
            case 3: 
                if uniqueValues == 2: return 4 #Full House
                else: return 3 #3 of a kind
            case 2: 
                if uniqueValues == 3: return 2 #Two pair
                else: return 1 #Pair
        return 0 #High Card
    
    def __eq__(self, obj): return self.cardValues == obj.cardValues
    def __lt__(self, obj):
        if self.bestHand < obj.bestHand: return True
        if self.bestHand > obj.bestHand: return False
        value = 0; 
        while value < len(self.cardValues):
            if self.cardValues[value] < obj.cardValues[value]: return True
            if self.cardValues[value] > obj.cardValues[value]: return False
            value += 1
    def __gt__(self, obj):
        if self.bestHand > obj.bestHand: return True
        if self.bestHand < obj.bestHand: return False
        value = 0; 
        while value < len(self.cardValues):
            if self.cardValues[value] > obj.cardValues[value]: return True
            if self.cardValues[value] < obj.cardValues[value]: return False
            value += 1

allCards = []
for item in puzzleInput:
    a,b = item.split(' ')
    newCard = Card(a,b)
    allCards.append(newCard)
allCards.sort()

answerOne = 0
counter = 1
while counter <= len(allCards):
    answerOne += counter * allCards[counter - 1].bid
    counter += 1
print(answerOne)

#251106089

#Part 2

jokerValues = [1,2,3,4,5,6,7,8,9,10,12,13,14]
jokerCardMap = {'A': 14, 'K': 13, 'Q':12, 'J':1, 'T':10}
jokerCardMapKeys = jokerCardMap.keys()

class JokerCard():
    def __init__(self, card, bid):
        super().__init__()
        self.rawCard = card
        self.jokers = 0
        self.cardValues = self.CardAsValues(self.rawCard)
        self.highestValue = self.GetHighestValue(self.cardValues)
        self.bid = int(bid)
        self.bestHand = self.EvaluateBestHand(self.highestValue)
        if self.jokers > 0:
            self.bestHand = self.EvaluateJoker(self.bestHand, self.jokers)
    
    def CardAsValues(self, rawCard):
        cardValues = []
        for item in rawCard:
            if item.isdigit(): cardValues.append(int(item))
            if item in jokerCardMapKeys: cardValues.append(jokerCardMap[item])
        return cardValues

    def GetHighestValue(self, cardValues):
        highestValue = []
        for jVal in jokerValues:
            for intVal in cardValues:
                if jVal == intVal: highestValue.append(jVal)
        highestValue.sort(reverse=True)
        return highestValue
    
    def EvaluateBestHand(self, cardValues):
        uniqueValues = 0
        currentValue = 0
        ofAKind = 0
        tally = 0
        for value in cardValues:
            if value == 1:
                self.jokers += 1
            if value != currentValue:
                if tally > ofAKind: ofAKind = tally
                currentValue = value
                uniqueValues += 1
                tally = 1
            else: tally += 1
        if tally > ofAKind: ofAKind = tally
        match ofAKind:
            case 5: return 6 #5 of a kind
            case 4: return 5 #4 of a kind
            case 3: 
                if uniqueValues == 2: return 4 #Full House
                else: return 3 #3 of a kind
            case 2: 
                if uniqueValues == 3: return 2 #Two pair
                else: return 1 #Pair
        return 0 #High Card
        
    def EvaluateJoker(self, bestHand, jokers):
        match bestHand:
            case 0: #High Card
                match jokers:
                    case 1:
                        return 1
            case 1: #Pair
                match jokers:
                    case 1:
                        return 3 #3 of a kind
                    case 2: #Pair is jokers
                        return 3 #3 of a kind
            case 2: #Two Pair
                match jokers:
                    case 1:
                        return 4 #Full House
                    case 2:
                        return 5 #4 of a kind
            case 3: #3 of a kind
                match jokers:
                    case 1:
                        return 5 #4 of a kind
                    case 3: #3 of a kind is jokers
                        return 5
            case 4: #Full House
                #Full house means the jokers are either the pair or 3 of a kind
                return 6 #5 of a kind
            case 5: #4 of a kind
                return 6 #The jokers are either the 4 of a kind, or the odd one, therefore, 5 of a kind
            case 6:
                return 6
        return 7

    def __eq__(self, obj): return self.cardValues == obj.cardValues

    def __lt__(self, obj):
        if self.bestHand < obj.bestHand: return True
        if self.bestHand > obj.bestHand: return False
        value = 0
        while value < len(self.highestValue):
            if self.cardValues[value] < obj.cardValues[value]: return True
            if self.cardValues[value] > obj.cardValues[value]: return False
            value += 1
        if self.jokers > obj.jokers: return True
        if self.jokers < obj.jokers: return False
    
    def __gt__(self, obj):
        if self.bestHand > obj.bestHand: return True
        if self.bestHand < obj.bestHand: return False
        value = 0; 
        while value < len(self.highestValue):
            if self.cardValues[value] > obj.cardValues[value]: return True
            if self.cardValues[value] < obj.cardValues[value]: return False
            value += 1
        if self.jokers < obj.jokers: return True
        if self.jokers > obj.jokers: return False

allJokerCards = []
for item in puzzleInput:
    a,b = item.split(' ')
    newCard = JokerCard(a,b)
    allJokerCards.append(newCard)
allJokerCards.sort()

answerTwo = 0
counter = 1
while counter <= len(allCards):
    answerTwo += counter * allJokerCards[counter - 1].bid
    counter += 1
print(answerTwo)
# 249620106
