from population import myCellPopulation

def main():
    ourPopulation = myCellPopulation(100,100)
    ourPopulation.populateWorld(ourPopulation)
    #print(ourPopulation)

main()
