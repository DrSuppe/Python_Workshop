from cell import myTinyCell

class gameOfLife():
    def __init__(self):

        self.nRows = 100
        self.nCollumns = 100

        pass

    def createField(self, nRows,nCol):
        self.arr = [[myTinyCell() for i in range(nCol)] for j in range(nRows)]
        pass

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

    def play(self):
        pass







test = gameOfLife()

test.createField(2, 2)

print(test.arr)

for i in range(0, 2):
    for j in range(0, 2):
        test.arr[i][j].test(i, j)
