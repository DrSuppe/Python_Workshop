class myTinyCell:   # eine Klasse myTinyCell erstellen

    def __init__(self, state, xPos, yPos ):
        self.state = state  #status der Zelle - lbendig oder Tot
        self.xPos = xPos    #Position der Zelle in X Richtung
        self.yPos = yPos    #Position der Zelle in Y Richtung


    def countNeighbours(self, population):

        self.neighbours = 0

        for i in range(-1, 2):
            for j in range(-1, 2):

                if population[self.yPos + i][self.xPos + j].state == True:
                    self.neighbours += 1

        if self.state == True:
            self.neighbours -=1


    def calcNextState(self):
        if self.state == False and self.neighbours == 3:
            self.state = True

        elif self.state == True and self.neighbours == 2 or self.neighbours == 3:
            self.state = True
        else:
            self.state = False