from cell import myTinyCell
from random import randint
class gameOfLife():

    def __init__(self, inputY, inputX):
        self.nRows = inputY
        self.nCollumns = inputX


    def createField(self):
        self.arr = [[myTinyCell() for i in range(self.nRows)] for j in range(self.nCollumns)]
        for i in range(0, self.nRows):
            for j in range(0, self.nCollumns):
                if i == 0 or i == self.nRows or j == 0 or j == self.nCollumns:
                    self.arr[i][j].nextState = False
                    self.arr[i][j].state = False
                else:
                    if randint(0, 4) == 1:
                        self.arr[i][j].nextState = True
                        self.arr[i][j].state = True

    def nextCycle(self):
        for i in range(1, self.nRows -1):
            for j in range(1, self.nCollumns-1):
                if (self.arr[i][j].state == False and self.countNeighbours(i, j)  == 3):
                    self.arr[i][j].nextState = True
                elif self.arr[i][j].state == True and (self.countNeighbours(i, j) == 2 or self.countNeighbours(i, j) == 3):
                    self.arr[i][j].nextState = True
                else:
                    self.arr[i][j].nextState = False


    def countNeighbours(self, y, x):
        nNeighbours = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.arr[y + i][x +j].state == True:
                    nNeighbours += 1

        if self.arr[y][x].state == True:
            nNeighbours -= 1

        return nNeighbours



