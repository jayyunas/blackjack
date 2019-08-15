from graphics import *
from buttonclass import*
from Card import *
from Deck import *
from BlackJack import *

def main():
    #game intro page (win)
    win1 = GraphWin("BlackJack Home Page", 600, 600)
    background = win1.setBackground("lightblue")
    messageBox1 = Text(Point(300,100),"Welcome to the BlackJack Game!")
    messageBox2 = Text(Point(300,150),"Please read the rules and then click Start to begin!")
    messageBox3 = Text(Point(300,350),"Rules: \nIn the Black Jack game, \nall number cards have their face value. \nJacks, Kings and Queens are worth 10.")
    messageBox4 = Text(Point(300,410),"Ace is counted as either 1 or 11 \nautomatically by the program depending on the situation.")                   
    messageBox5 = Text(Point(300,470),"The aim of the Black Jack Game is to get 21 \nor as close to 21 as possible. \nclick Hit when you want to draw one more card and \nclick Stand when you don't want any more cards added to your hand")                   
    messageBox1.draw(win1)
    messageBox2.draw(win1)
    messageBox3.draw(win1)
    messageBox4.draw(win1)
    messageBox5.draw(win1)
    
    #draw buttons
    Start = Button(win1, Point(250,230),50,30,"Start")
    Quit = Button(win1, Point(350,230),50,30,"Quit")
    

    #take a mouse click to proceed 
    pt = win1.getMouse()
    while not Quit.isClicked(pt):
        #call the start function!
        if Start.isClicked(pt):
            win1.close()
            start()
        pt = win1.getMouse()
    #close intro screen when new game stars
    win1.close()

          
def start():
    #start the blackjack game in another window (win)
    win = GraphWin("Black Jack Game", 800, 600)
    background = win.setBackground("lightblue")
    
    #draw buttons
    Hit = Button(win,Point(160,550), 90, 30, "Hit")
    Stand = Button(win,Point(320,550), 90, 30, "Stand")
    Play = Button(win,Point(480,550), 90, 30, "Play")
    Exit = Button(win,Point(640,550), 90, 30, "Exit")

    #deactivate hit and stand, and activate play and exit
    Hit.deactivate()
    Stand.deactivate()
    Play.activate()
    Exit.activate()
    
    #ask user to enter his/her name if wanted
    messageBox1 = Text(Point(400,150),"Please enter your name (under 20 letters) here and then click Play to staet the game")
    messageBox2 = Text(Point(400,180),"If you don't want to specify your name, just click Play to get started(''Player'' will be displayed next to your score).")
    inputBox = Entry(Point(400,220),30)
    inputBox.setText("Player")
    messageBox1.draw(win)
    messageBox2.draw(win)
    inputBox.draw(win)
    
    
    #if the player did not click on the button, remind the player to click again
    pt=win.getMouse()
    reprompt=True
    prompt1=Text(Point(400,280),"")
    prompt1.draw(win)
    while not Play.isClicked(pt):
        if reprompt:
            prompt1.setText("Please click again. Click the ''Play'' button to begin.")
            reprompt = False
        pt=win.getMouse()

    #deactivate Play button once they've clicked on it
    Play.deactivate()
    
    #undraw prompt one
    prompt1.undraw()

    #undraw additional prompt and undraw messageBox
    inputBox.undraw()
    messageBox1.undraw()
    messageBox2.undraw()

    #The game is about to start. Change the background to green
    background = win.setBackground("green")

    #show player and dealer's name
    dealerName = Text(Point(100,100), "Dealer")
    dealerName.setStyle("bold")
    dealerName.draw(win)
    #get player's name from input
    name = inputBox.getText()
    userName = Text(Point(100,400), name)
    userName.setStyle("bold")
    userName.draw(win)

    #start a new game using BlackJack class
    game = BlackJack()

    #call initDeal function (deals first cards)
    game.initDeal(win, 200, 100, 200, 400)

    #hide dealer's second card
    dHide2 =Image(Point(300,100),"playingcards/"+"b1fv.gif")
    dHide2.draw(win)

    #change the state of the buttons
    Play.deactivate()
    Hit.activate()
    Stand.activate()

    #calculate scores for the player and show player's score on the window
    pScore = Button(win, Point(100,450), 40, 30, game.evaluateHand(game.pHand))

    #if the player has 21, the dealer reveals their card and show how many points they have
    if game.evaluateHand(game.pHand) == 21:
        winPrompt = Text(Point(350,270),"CONGRATS! YOU WIN!!!Click Exit to end the game").draw(win)

        #show dealer score & card
        dScore = Button(win, Point(100, 150), 40, 30, game.evaluateHand(game.dHand))
        dHide2.undraw()

        #activate only exit button
        Play.deactivate()
        Stand.deactivate()
        Hit.deactivate()

    #if the player didn't win instantly, get a mouse click   
    else:
        pt = win.getMouse()

    #set the initial x coordinate 
    x = 300
    x1 = 300

    #until "Exit" is clicked
    while not Exit.isClicked(pt):

        #if hit is clicked, a new card will be drawn on player's side and player's score will be re-calculated
        if Hit.isClicked(pt):
            game.hit(win, x, 400)
            x = x + 100

            #update player's score
            pScore = Button(win, Point(100,450), 40, 30, game.evaluateHand(game.pHand))

            #if the player has 21, we check whether the dealer has 21 as well
            if game.evaluateHand(game.pHand) == 21:

                #if both dealer and player have 21, game is a tie
                if game.evaluateHand(game.pHand) == game.evaluateHand(game.dHand):
                    #show dealer's card
                    dHide2.undraw()
                    tiePrompt = Text(Point(350,270),"~PUSH~ Click Exit to end the game").draw(win)
                    #update player score
                    dScore = Button(win, Point(100, 150), 40, 30, game.evaluateHand(game.dHand))

                    #change the state of the buttons
                    Hit.deactivate()
                    Stand.deactivate()
                    Play.deactivate()

                #if only the player has 21 and dealer has less, then player wins
                else:
                    dHide2.undraw()
                    winPrompt = Text(Point(350,270),"CONGRATS! YOU WIN!!!Click Exit to end the game").draw(win)
                    dScore = Button(win, Point(100, 150), 40, 30, game.evaluateHand(game.dHand))

                    #deactivate all buttons except exit
                    Hit.deactivate()
                    Stand.deactivate()
                    Play.deactivate()

            #if player busted
            elif game.evaluateHand(game.pHand) > 21:
                dHide2.undraw()
                losePrompt = Text(Point(350,270),"YOU BUSTED, DEALER WINS. Click Exit to end the game.").draw(win)
                dScore = Button(win, Point(100, 150), 40, 30, game.evaluateHand(game.dHand))

                #deactivate all buttons except exit
                Hit.deactivate()
                Stand.deactivate()
                Play.deactivate()

        #if the stand button is clicked, show all dealer's card and dealer's total score
        elif Stand.isClicked(pt):
            game.dealerPlays(win, x1, 100)
            x1 = x1 + 100
            game.evaluateHand(game.dHand)
            dScore = Button(win, Point(100, 150), 40, 30, game.evaluateHand(game.dHand))
            dHide2.undraw()
            
            #if dealer has less than 21
            if game.evaluateHand(game.dHand) < 21:
                
                #if player's score is equal to dealer's score, it's a tie
                if game.evaluateHand(game.pHand) == game.evaluateHand(game.dHand):
                    tiePrompt = Text(Point(350,270),"~PUSH~ Click Exit to end the game").draw(win)
                    dScore = Button(win, Point(100, 150), 40, 30, game.evaluateHand(game.dHand))

                    #deactivate all buttons except exit
                    Hit.deactivate()
                    Stand.deactivate()
                    Play.deactivate()

                #if player's score is greater than dealer's score, player wins
                elif game.evaluateHand(game.pHand) > game.evaluateHand(game.dHand):
                    winPrompt = Text(Point(350,270),"CONGRATS! YOU WIN!!!Click Exit to end the game").draw(win)
                    dScore = Button(win, Point(100, 150), 40, 30, game.evaluateHand(game.dHand))

                    #deactivate all buttons except exit
                    Hit.deactivate()
                    Stand.deactivate()
                    Play.deactivate()
                    
                #if player's score is less than dealer's score, dealer wins
                else:
                    losePrompt = Text(Point(350,270),"OOPS, DEALER WINS. Click Exit to end the game.").draw(win)
                    dScore = Button(win, Point(100, 150), 40, 30, game.evaluateHand(game.dHand))

                    #deactivate all buttons except exit
                    Hit.deactivate()
                    Stand.deactivate()
                    Play.deactivate()

            #if dealer busted
            elif game.evaluateHand(game.dHand) > 21:
                winPrompt = Text(Point(350,270),"DEALER BUSTED. YOU WIN!!!Click Exit to end the game").draw(win)
                dScore = Button(win, Point(100, 150), 40, 30, game.evaluateHand(game.dHand))

                #deactivate all buttons except exit
                Hit.deactivate()
                Stand.deactivate()
                Play.deactivate()
                
            #if dealer has 21, dealer wins
            else:
                winPrompt = Text(Point(350,270),"OOPS, DEALER WINS. Click Exit to end the game.").draw(win)
                dScore = Button(win, Point(100, 150), 40, 30, game.evaluateHand(game.dHand))

                #deactivate all buttons except exit
                Hit.deactivate()
                Stand.deactivate()
                Play.deactivate()

        #ask for another mouseclick until exit is clicked  
        pt = win.getMouse()

    #close window
    win.close()

    main()

main()
