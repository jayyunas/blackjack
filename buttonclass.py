from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        ## as you read through this, ask yourself:  what are the instance variables here?
        ## it would be useful to add comments describing what some of these variables are for...
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        #x-vars to determine button top left and bottom right corners
        self.xmax, self.xmin = x+w, x-w
        #y-vars to determine button top left and bottom right corners
        self.ymax, self.ymin = y+h, y-h
        #top left corner
        p1 = Point(self.xmin, self.ymin)
        #top right corner
        p2 = Point(self.xmax, self.ymax)
        #draw the button
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        #label the button
        self.label = Text(center, label)
        self.label.draw(win)
        self.activate() #sets button to 'active', colors text, bold outline color

    def getLabel(self):
        """Returns the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black') #color the text "black"
        self.rect.setWidth(2)       #set the outline to look bolder
        self.active = True          #set the boolean variable that tracks "active"-ness to True

    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.active = False
        self.label.setFill('darkgray')
        self.rect.setWidth(1)
        
    def isClicked(self, pt):
        """Returns true if button active and Point pt is inside"""
        if self.active and (pt.getX() <= self.xmax and pt.getX() >= self.xmin
                        and pt.getY() <= self.ymax and pt.getY() >= self.ymin):
            return True
        else:
            return False
    
if __name__ == "__main__": 
    main()
