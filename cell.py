class myTinyCell:

    def __init__(self):
        self.state = False
        self.nextState = False

    def countNeighbours(self, y, x, arr):
        nNeighbours = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if arr[y + i][x +j].state == True:
                    nNeighbours += 1

        if arr[y][x].state == True:
            nNeighbours -= 1

        return nNeighbours
