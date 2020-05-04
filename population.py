from cell import myTinyCell
from random import randint

class myCellPopulation:

    def __init__(self, xMax, yMax):
        self.xMax = xMax + 2
        self.yMax = yMax + 2

        self.worldOfLife = [[myTinyCell(False, i, j) for i in range(self.xMax)] for j in range(self.yMax)]

        print("erster index: ", len(self.worldOfLife))
        print("zweiter index: ", len(self.worldOfLife[0]))

        for j in range(1, self.yMax-1):
            for i in range(1, self.xMax-1):
                print("i : ", i)
                print("j : ", j)
                print("")
                if randint(0, 1) == 1:
                    self.worldOfLife[j][i].state = True


    def getNextTimestep(self):

        for i in range(1, self.yMax - 1):
            for j in range(1, self.xMax - 1):
                self.worldOfLife[i][j].countNeighbours(self.worldOfLife)

        for i in range(1, self.yMax - 1):
            for j in range(1, self.xMax - 1):
                self.worldOfLife[i][j].calcNextState()


    def showWolrdOfLife(self):
        for i in range(1,self.xMax-1):
            print("")
            for j in range(1,self.yMax-1):

                if self.worldOfLife[j][i].state == True:
                    print("X ", end=" ")
                else:
                    print(". ", end=" ")
        print("")
        print("-----------------------------------------------------------------------------------------------------")