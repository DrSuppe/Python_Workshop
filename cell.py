class myTinyCell:

    neighbours = 0

    def __init__(self, state, xPos, yPos, population):
        self.state = state
        self.xPos = xPos
        self.yPos = yPos
        if xPos - 1 < 0 :

        if xPos
        self.adjacentCells = [population[xPos,yPos], population[], population[], population[], population[], population[], population[], population[],]

    def determineAdjacentCells(self, population):

    def countNeighbours(self):

        self.neighbours = 0
        for i in self.adjacentCells:
            if i.state == True:
                self.neighbours += 1

    def changeState(self):
        if self.state == False and self.neighbours == 3:
            self.state = True

        if self.state == True:
            if self.neighbours > 2:
                self.state = False

            if self.neighbours < 3:
                self.state = False