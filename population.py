from cell import myTinyCell

class myCellPopulation:
    xMax = 100
    yMax = 100
    worldOfLife

    def __init__(self, xMax, yMax):
        self.xMax = xMax
        self.yMax = yMax
        for i in range(0, (self.xMax-1)):
            for j in range(0, (self.yMax-1)):
                print('yay. i is:')
                print(i)
                print('j is:')
                print(j)
                self.worldOfLife[i][j] = myTinyCell(False, i, j)

    def populateWorld(self):
        for i in range(0, (self.xMax-1)):
            for j in range(0, (self.yMax-1)):
                self.worldOfLife[i][j].determineAdjacentCells(self.worldOfLife)

