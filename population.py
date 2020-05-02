from cell import myTinyCell

class myCellPopulation:
    xMax = 100
    yMax = 100
    worldOfLife = [[0,0],[0,0]]

    def __init__(self, xMax, yMax):
        self.xMax = xMax
        self.yMax = yMax
        for i in (0, (self.xMax-1)):
            for j in (0, (self.yMax-1)):
                self.worldOfLife[i][j] = myTinyCell(False, i, j)

    def populateWorld(self):
        for i in (0, (self.xMax-1)):
            for j in (0, (self.yMax-1)):
                self.worldOfLife[i][j].determineAdjacentCells(self.worldOfLife)

