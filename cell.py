class myTinyCell:   # eine Klasse myTinyCell erstellen
                    #   dient sozusagen als Anleitung/Bauplan, jedes mal, wenn das Spiel eine Zelle erstellt

    state = False
    xPos = 0
    yPos = 0
    neighbours = 0
    adjacentCells = [0,0,0]

    def __init__(self, state, xPos, yPos ):
        self.state = state  #status der Zelle - lbendig oder Tot
        self.xPos = xPos    #Position der Zelle in X Richtung
        self.yPos = yPos    #Position der Zelle in Y Richtung
          # bei der Erstellung einer Zelle, soll jede Zelle feststellen, wer Ihre Nachbarn sind
                                            #       Das ist notwendig um Randfälle abzufangen, wo die Suche nach Nachbarzellen aus dem Feld laufen könnte.

    def determineAdjacentCells(self, population):
        # Die Koordinaten eines Feldes beginne bei Programmiern klassicher Weise oben Links

        if self.xPos == 1 and self.yPos == 1: # Ecke oben links
            self.adjacentCells = [population[self.xPos + 1][self.yPos], population[self.xPos + 1][self.yPos + 1], population[self.xPos][self.yPos + 1]]
            # die restlichen Fälle müssen nur überprüft werden, wenn der erste Fall nicht eintritt. Daher "elif" das gilt auch für alle folgenden Fälle

        elif self.xPos == 1 and self.yPos == population.yMax: # Ecke unten links
            self.adjacentCells = [population[self.xPos][self.yPos - 1], population[self.xPos + 1][self.yPos - 1], population[self.xPos + 1][self.yPos]]

        elif self.xPos == population.xMax and self.yPos == 1:   # Ecke oben rechts
            self.adjacentCells = [population[self.xPos - 1][self.yPos], population[self.xPos - 1][self.yPos + 1], population[self.xPos][self.yPos + 1]]

        elif self.xPos == population.xMax and self.yPos == population.yMax: # Ecke unten Rechts
            self.adjacentCells = [population[self.xPos][self.yPos - 1], population[self.xPos - 1][self.yPos - 1], population[self.xPos - 1][self.yPos]]

        elif self.xPos == 1 and self.yPos > 1 and self.yPos < population.yMax: # linke Kante
            self.adjacentCells = [population[self.xPos][self.yPos - 1], population[self.xPos + 1][self.yPos - 1], population[self.xPos + 1][self.yPos], population[self.xPos + 1][self.yPos + 1], population[self.xPos][self.yPos + 1]]

        elif self.xPos == population.xMax and self.yPos > 1 and self.yPos < population.yMax:   # rechte Kante
            self.adjacentCells = [population[self.xPos][self.yPos - 1], population[self.xPos - 1][self.yPos - 1], population[self.xPos - 1][self.yPos], population[self.xPos - 1][self.yPos + 1], population[self.xPos][self.yPos + 1]]

        elif self.yPos == 1 and self.xPos > 1 and self.xPos < population.xMax: # obere Kante
            self.adjacentCells = [population[self.xPos - 1][self.yPos], population[self.xPos - 1][self.yPos + 1], population[self.xPos][self.yPos + 1], population[self.xPos + 1][self.yPos + 1], population[self.xPos + 1][self.yPos]]

        elif self.yPos == population.yMax and self.xPos > 1 and self.xPos < population.xMax:   # untere Kante
            self.adjacentCells = [population[self.xPos - 1][self.yPos], population[self.xPos - 1][self.yPos - 1], population[self.xPos][self.yPos - 1], population[self.xPos + 1][self.yPos + 1], population[self.xPos + 1][self.yPos]]
        else:
            self.adjacentCells = [population[self.xPos - 1][self.yPos - 1], population[self.xPos - 1][self.yPos], population[self.xPos - 1][self.yPos + 1], population[self.xPos][self.yPos + 1], population[self.xPos + 1][self.yPos + 1], population[self.xPos + 1][self.yPos], population[self.xPos + 1][self.yPos - 1], population[self.xPos][self.yPos - 1]]

    def countNeighbours(self):

        self.neighbours = 0
        for i in self.adjacentCells:
            if i.state == True:
                self.neighbours += 1

    def changeState(self):
        if self.state == False and self.neighbours == 3:
            self.state = True

        if self.state == True:
            if self.neighbours > 2:
                self.state = False

            if self.neighbours < 3:
                self.state = False