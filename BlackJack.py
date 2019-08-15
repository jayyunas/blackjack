#This is the black jack class which consists all
# the functions that needs to be called when the game is played
from Card import *
from Deck import *
from graphics import *
from random import *
from buttonclass import *

class BlackJack:
    """Attributes of this Blackjack class are as follows:

INSTANCE VARIABLES
 
dealerHand: a list of PlayingCard objects representing the dealer's hand
playerHand: a list of PlayingCard objects representing the player's hand
playingDeck: a Deck object representing the deck of cards the game is being played with"""


    def __init__(self):
        """constructor that initializes instance variables
it also gives the playingDeck an initial shuffle"""

        #create an empty list for all dealer's card
        dHand = []
        #create an empty list for all player's card
        pHand = []
        #create a deck to play the cards
        self.Deck = Deck()
        #shuffle the cards on the deck
        self.Deck.shuffle()
        #introduce self to transfer variables
        self.dHand = dHand
        self.pHand = pHand

    #Initial Deal (two cards)
    def initDeal(self, gwin, xposD, yposD, xposP, yposP):
        """deals out initial cards, 2 per player and
displays dealer and player hands on graphical win
xposD and yposD give initial position for dealer cards
xposP and yposP are analogous """
        #set accumulator to 0
        x=0
        #randomly draw two cards for both dealer and player and display them on the window
        for i in range(2):
            initCardP = self.Deck.dealCard()
            #get a random suit for the card
            pSuit = initCardP.getSuit()
            #get a random rank for the card
            pRank = initCardP.getRank()
            #draw the card on the window
            pCard = Image(Point((xposP+x), yposP), "playingcards/" + pSuit + str(pRank) + ".gif")
            pCard.draw(gwin)
            #append the rank of the card to the cardlist
            self.pHand.append(initCardP)
            
            initCardD = self.Deck.dealCard()
            dSuit = initCardD.getSuit()
            dRank = initCardD.getRank()
            dCard = Image(Point((xposD+x), yposD), "playingcards/" + dSuit + str(dRank) + ".gif") 
            dCard.draw(gwin)
            self.dHand.append(initCardD)
            x = x + 100

    #When "Hit" is clicked        
    def hit(self, gwin, xPos, yPos):
        """adds a new card to the player's hand and places it at xPos, yPos"""
        #get a card and then delete it from the card list after it's dealt
        hitCard = self.Deck.dealCard()
        #get a random  suit for the card
        pSuit = hitCard.getSuit()
        #get a random rank for the card
        pRank = hitCard.getRank()
        #get the image for the card with suit and rank indicated above
        #increase the x axis by 100 everytime a new car is added
        im = Image(Point(xPos + 100, yPos), "playingcards/" + pSuit + str(pRank) + ".gif")
        #draw the card on the window
        im.draw(gwin)
        #append the card on the player's cardlist
        self.pHand.append(hitCard)
  

    #Calculate the total score for both player and dealer
    def evaluateHand(self, hand): 
        """totals the cards in the hand that is passed in and returns total
        (ace counts as 11 if doing so allows total to stay under 21)"""
        #initialize total as 0
        total = 0
        hasAce = False

        #loop through all the cards in player/dealer's hand
        for cards in hand:
            #if one of the cards' initial value is 1
            if cards.BJValue() == 1:
                #there's Ace in the card list
                hasAce = True
            #Ace is counted as is face value--1
            total = total + cards.BJValue()

        #if Ace is in the card list and the total is equal or less than 10    
        if hasAce and total + 10 <= 21:
            #Ace is counted as 11
            total = total + 10

        #return the total score
        return total

    def dealerPlays(self, gwin, xPos, yPos):
        """dealer deals cards to herself, stopping when hitting "soft 17 """
        #initialize total as 0
        total = 0
        #calculate the score for dealer after initial deal
        total = self.evaluateHand(self.dHand)

        #if the total score is below soft 17
        while total < 17:
            #draw another card for the dealer and then delete it from the card list after it's dealt
            dealerHit = self.Deck.dealCard()
            dSuit = dealerHit.getSuit()
            dRank = dealerHit.getRank()
            self.dHand.append(dealerHit)
            #update dealer's total score
            total = self.evaluateHand(self.dHand)
            #draw the new card on the window
            dImg = Image(Point(xPos+100, yPos), "playingcards/" + dSuit + str(dRank) + ".gif")
            dImg.draw(gwin)
            #increment the x value
            xPos = xPos+100
        #return total value of dealer's hand
        return total
















    
