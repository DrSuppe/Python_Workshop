from population import myCellPopulation
import time

def main():
    ourPopulation = myCellPopulation(20, 20)

    while True:
        ourPopulation.getNextTimestep()
        ourPopulation.showWolrdOfLife()
        time.sleep(0.4)


main()
