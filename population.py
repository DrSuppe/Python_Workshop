from cell import myTinyCell

class myCellPopulation:

    def __init__(self, xMax, yMax):
        self.xMax = xMax
        self.yMax = yMax

        self.worldOfLife = [[myTinyCell(False, xMax, yMax) for i in range(self.xMax)] for j in range(self.yMax)]


    def populateWorld(self, population):

        for i in range(0, (self.xMax-1)):
            for j in range(0, (self.yMax-1)):
                self.worldOfLife[i][j].determineAdjacentCells()
                print(self.worldOfLife[i][j].adjacentCells)

