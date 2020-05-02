from cell import myTinyCell
import numpy as np

class gameOfLife():
    def __init__(self):

        self.nRows = 100
        self.nCollumns = 100

        pass

    def createField(self, nRows,nCol):
        self.arr = [[myTinyCell() for i in range(nCol)] for j in range(nRows)]
        pass

    def play(self):
        pass





test = gameOfLife()

test.createField(2, 2)

print(test.arr)
