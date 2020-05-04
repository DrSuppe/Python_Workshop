from cell import myTinyCell
from random import randint


class gameOfLife():

    def __init__(self, inputY, inputX):
        self.nRows = inputY
        self.nCollumns = inputX


    def createField(self):
        #TODO Spielfeld Array mit geschachtelten For-Schleifen
        self.arr = []
        for i in range(self.nRows):
            col = []
            for j in range(self.nCollumns ):
                col.append(myTinyCell())
            self.arr.append(col)

        for i in range(0, self.nRows):
            for j in range(0, self.nCollumns):
                if i == 0 or i == self.nRows-1 or j == 0 or j == self.nCollumns-1:
                    self.arr[i][j].nextState = False
                    self.arr[i][j].state = False
                else:
                    if randint(0, 4) == 1:
                        self.arr[i][j].nextState = True
                        self.arr[i][j].state = True

    def nextCycle(self):
        for i in range(1, self.nRows -1):
            for j in range(1, self.nCollumns-1):
                if (self.arr[i][j].state == False and self.arr[i][j].countNeighbours(i, j, self.arr)  == 3):
                    self.arr[i][j].nextState = True
                elif self.arr[i][j].state == True and (self.arr[i][j].countNeighbours(i, j, self.arr)  == 2 or self.arr[i][j].countNeighbours(i, j, self.arr)  == 3):
                    self.arr[i][j].nextState = True
                else:
                    self.arr[i][j].nextState = False






