from cell import myTinyCell
from random import randint
class gameOfLife():
    def __init__(self, inputY, inputX):

        self.nRows = inputY
        self.nCollumns = inputX

        pass

    def createField(self):
        self.arr = [[myTinyCell() for i in range(self.nRows)] for j in range(self.nCollumns)]
        for i in range(0, self.nRows):
            for j in range(0, self.nCollumns):
                if i == 0 or i == self.nRows or j == 0 or j == self.nCollumns:
                    self.arr[i][j].nextState = False
                else:
                    if randint(0, 1) == 1:
                        self.arr[i][j].nextState = True

    def nextCycle(self):
        for i in range(1, self.nRows -1):
            for j in range(1, self.nCollumns):
                if self.countNeighbours(i, j) <= 1 or self.countNeighbours(i, j) >=4:
                    self.arr[i][j].nextState = False
                else:
                    self.arr[i][j].nextState = True


    def countNeighbours(self, x, y):
        nNeighbours = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.arr[i][j].state == True:
                    nNeighbours += 1
        return nNeighbours


    def draw(self):
        for i in range(1, self.nRows-1):
            for j in range(1, self.nCollumns-1):
                if self.arr[i][j].nextState == False:
                    print(i, ",", j, "-", "0")
                    self.arr[i][j].state == self.arr[i][j].nextState
                else:
                    print(i, ",", j, "-" ,"X")
                    self.arr[i][j].state == self.arr[i][j].nextState


    def play(self):
        pass






test = gameOfLife(5,5)

test.createField()

test.draw()

