import sys

#def updateAllPos():


# Class for objects
class tnsNao:

    def __init__(self, pos, rect, sheet, render = False):
        self.tnsPos   = pos
        self.tnsRect  = rect
        self.tnsSize  = [rect[2], rect[3]]
        self.tnsSheet = sheet
        self.toRender = render
    
    # Nao drawing function
    def tnsDraw(self, screen):
        import main
        self.tnsSize = main.size
        if self.toRender:
            screen.blit(self.tnsSheet, self.tnsPos, self.tnsRect)
            tnsSize = main.getSize()
            return True
        return False

    # Send if the nao was clicked
    def tnsClick(self, mousePos):

        if  mousePos[0] > self.tnsPos[0] and mousePos[0] < self.tnsSize[0] + self.tnsPos[0] and \
            mousePos[1] > self.tnsPos[1] and mousePos[1] < self.tnsSize[1] + self.tnsPos[1] and \
            self.toRender:
            return True

        else:
            return False

# Exit from game function
def exitGame():
    sys.exit()