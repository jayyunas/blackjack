from Card import *
from random import *

class Deck:
    def __init__(self):
        #create an empty list for card list
        self.cardList = []
        #loop through all the suit and ranks to add all the cards to the card list
        for suit in ["d", "c", "h", "s"]:
            for r in range(1,14):
                self.cardList.append(Card(r, suit))

    #shuffle all the cards in the card list
    def shuffle(self):
        length = len(self.cardList)
        #run through each card in the list 
        for j in range(length):
            #make sure each card swaps with another card to make it random
            index = randrange(0,length)
            #create a temporary variable to store a random card
            temp = self.cardList[index]
            #change cardList[index] to cardList[j]
            self.cardList[index] = self.cardList[j]
            #change cardList[j] to cardList[index]
            self.cardList[j] = temp

    #delete the card from the card list after it's showed on the table
    #so it won't be deal again
    def dealCard(self):
        return self.cardList.pop(0)

    #return the number of cards left in the card list
    def cardsLeft(self):
        return len(self.cardList)

