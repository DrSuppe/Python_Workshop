from random import randint
import time

nRows = 30
nCollumns = 30

world = []

for i in range(nRows):
    columns = []
    for j in range(nCollumns ):
        columns.append([False, False])

    world.append(columns)

for i in range(1, nRows-1):
    for j in range(1, nCollumns-1):
        if randint(0, 4) == 1:
            world[i][j][1]= True


def nextCycle():
    for i in range(1, nRows -1):
        for j in range(1, nCollumns-1):

            if (world[i][j][1] == False and countNeighbours(i, j)  == 3):
                world[i][j][0] = True
            elif (world[i][j][1] == True and (countNeighbours(i, j) == 2 or countNeighbours(i, j) == 3)):
                world[i][j][0] = True
            else:
                world[i][j][0] = False


def countNeighbours( y, x):
    nNeighbours = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if world[y + i][x + j][1] == True:
                nNeighbours += 1

    if world[y][x][1] == True:
        nNeighbours -= 1

    return nNeighbours


def showWolrdOfLife():
    print("--" * nRows)
    for i in range(1, nRows - 1):
        print("")
        for j in range(1, nCollumns - 1):
            if world[i][j][0] == True:
                '''print("ausgabe True", end = "")'''
                print("X ", end=" ")
                world[i][j][1] = world[i][j][0]

            elif world[i][j][0] == False:
                '''# print("ausgabe false", end = "")
                # print(arr[i][j][0], end = "")'''
                print("  ", end=" ")
                world[i][j][1] = world[i][j][0]

    print("")
    print("--" * nRows)

if __name__ == "__main__":
    while True:
        nextCycle()
        showWolrdOfLife()
        time.sleep(0.1)