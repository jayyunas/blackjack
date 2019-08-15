class Card:
    #initialize the rank and suit for cards
    def __init__(self,rank,suit):
        """rank is an int in the range 1-13 indicating the rank Ace-King,
and siut is a single character "d,""c,""h," or "s" indicating the suit
(dimonds,clubs,herats,or spades).Create the corresponding card."""
        #return rank and suit
        self.rank = rank
        self.suit = suit

    #return rank in the main function
    def getRank(self):
        """returns the rank of the card"""
        return self.rank

    #return suit in the main function
    def getSuit(self):
        """returns the suit of the card"""
        return self.suit

    #return card value(rank) in the main function
    def BJValue(self):
        """returns the Blackjack value of the card. Ace counts as 1, face cards
count as 10"""
        #if the face value of a card is greater or equals to 10
        if self.rank >= 10:
            #count the value as 10
            return 10
        #if the face value of a card is less than 10
        else:
            #return the face value of the card
            return self.rank

    #return the string name of the card
    def __str__(self):
        """returns a string that names the card. For example, "Ace of Spades."""
        #create a dictionary of suits
        self.suitDic = {"s": "spades","d":"diamonds","h":"hearts","c":"clubs"}
        #create a list of ranks
        self.rankList = ["", "Ace","Two","Three","Four","Five","Six","Seven","Eight",
                    "Nine","Ten","Jack","Queen","King"]
        self.rank = self.rankList[self.rank]
        self.suit = self.suitDic[self.suit]
        self.name = self.rank + " of " + self.suit
        return self.name
      



