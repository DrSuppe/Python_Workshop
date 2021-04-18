# ein Google-Suche nach Guis führt einen auf Pygame. Wenn man dann googlet, wie man mit Pygame Rechtecke zeichnet
#   kann man viel Informationen finden. Beispielsweise diese Website:
#   https://www.geeksforgeeks.org/how-to-draw-rectangle-in-pygame/

import pygame                           # nach der Recherche wird pygame installiert und importiert. Außerdem auch die
import time                             #   "time" library um wieder eine kleine Verzögerung zwischen den RUnden zu nutzen.
from Spiellogik import GameOfLife       #   Wir brauchen aber natürlcih auch unsere Klasse, die wir programmiert haben,
                                        #   daher impoertirem wir auch unser "GameOfLife" aus der Datei "Spiellogik"

nRows = 70          # hier wird die größe unseres Spielfeldes gesetzt, wie wir es vorher schon gemacht haben
nCollumns = 70      #   und als Vriable abgespeichert.


width = nRows * 10          # Da wir für jede Zelle ein kleines Rechteck haben wollen müssen wir die größe des Fensters
height = nCollumns * 10     #   in Pixeln berechnen. Wir nehmen hier an, dass jede Zelle 10 Pixel mal 10 Pixel groß ist.
                            #   Also wird die ANzahl der Zellen in Breite und Höhe mit den Pixeln pro Zelle multipliziert


#______ START SETUP______
# Das Setup besteht zum einen aus Elementen, die wir bei anderne Darstellungen schon benutzt haben. Wir muessen eine
#   Instanz des Spiels erstellen und dann ein Spielfeld initialisieren.
#   Andere Tiele kommen aus der Recherche nach visueller darstellung. Dabei orientieren wir uns an dem Link oben um ein
#   Pygame Fester zu initialisieren.

#______game of life setup
einGameOfLife = GameOfLife(nRows, nCollumns)        # erzeugt eine Instanz der Klasse "GameOfLife" wie wir es vorher auch
einGameOfLife.erstelleSpielfeld()                   #   gemacht haben. Außerdem wird die Methode "erstelleSpielfeld"
                                                    #   aufgerufen. Damit ist "einGameOfLife" ein Objekt, der Klasse
                                                    #   "GameOfLife" de, durch die Methode "erstelleSpielfeld" das Attribut
                                                    #   "gegeben" wurde. Es existiert also ein Spielfeld als Attribut des
                                                    #   Objektes "einGameOfLife"

#______pygame Gui setup
screen = pygame.display.set_mode((width, height))       # hier wird ein Fenster mit dem Namen "screen" erstellt.
                                                        #   dazu wird mit dem Befehl "pygame.display.set_mode((width, height))"
                                                        #   eine Instanz mit den Eigenschaften "height" und "width" als
                                                        #   Höhe und Breite.

pygame.display.set_caption('Game Of Life - Python Workshop')        # mit diesem befehl kann die Beschriftung des Fensters
                                                                    #   beliebig gewählt werden.

screen.fill((0,0,0))        # Hiermit wird der Hintergrund des Fensters auf eine Farbe gestezt
pygame.display.flip()       # dieser befehl ist wichtig , da er den Bildschirm "lädt" bzw aktualisiert und muss nach jeder
                            #   Aenderung aufgerufen werden.

#______ END SETUP______


def draw(Spielfeld):        # da wir jetzt unser Spielfeld anders darstellen wollen brauchen wir eine neue Funktion
                            #   für die Darstellung. Die wird hier "draw" genannt.

    for i in range(1, nRows-1):                 # Wie auch bei der vorherigen darstellungsfunktion müssen wir über alle
        for j in range(1, nCollumns-1):         #   Zellen des SPielfeldes iterieren um festzustellen, ob die Zelle
                                                #   lebendig, oder tot ist. Dann kann die Zelle entpsrechend dargestellt werden

            if Spielfeld[i][j].naechsterStatus == True:                             # Wenn die Zelle lebendig ist, wird
                pygame.draw.rect(screen, (255, 255, 255), (i*10, j*10, 10, 10))     #   ein weisses Rechteck an der Position
                Spielfeld[i][j].status = Spielfeld[i][j].naechsterStatus            #   gezeichnet. Außerdem wird der Status
                                                                                    #   der Zelle aktualisiert, wie auch
                                                                                    #   in den vorherigen Funktionen
                                                                                    #   zum dartsellen.
            else:
                pygame.draw.rect(screen, (0,0,0), (i*10, j*10, 10, 10))         # Wenn die Zelle nicht lebendig ist, wird
                Spielfeld[i][j].status = Spielfeld[i][j].naechsterStatus        #   an der Position der Zelle ein schwarzes
                                                                                #   Rechteck gezeichnet. Das ist vor allem
                                                                                #   wichtig, um die alten gezeichneten Zellen
                                                                                #   der vorherigen Iteration zu uebreschreiben


# Jetzt haben wir die gesamte Funktionalitaet fuer eine GUI zusammen und muessen im Grunde nur noch eine Schleife schreiben,
#   die immer die neuen Iterationen bestimmt. dazu nutzen wir hier eine "while" schleife. Wir k

if __name__ == "__main__":      # Diese If Abfrage sorgt dafür, dass die Datei nur ausgeführt wird, wenn man diese Datei
                                #   ausfuehrt. Das ist praktisch, weil man die Funktionen, die wir definiert haben evtl
                                #   aus einer anderen Datei raus aufrufen Will (wie bei Bibliotheken). In so einem Fall
                                #   Dann will man die ausfuehrbaren Dateien so abkapseln. Das ist einfach guter Stil

    runningBed = True   # die Variable wird gesetzt, damit wir in einer dauerschleife für den laufenden Betrieb bleibben
                        #   können. Durch das aendern der Variable auf "False" kann dann aus der daurschleife gebrochen
                        #   werden um das "Spiel" zu beenden.

    while runningBed:       # Hier ist unsere sich ständig wiederholende Schleife, wie wir es bereits kennen. Diese wiederholt
                            #   den Code in der Schleife so lange, bis die Variable "runningBed" nicht mehr auf True
                            #   gesetzt ist.

        for event in pygame.event.get():        # Diese Abfrage checkt in Pygame ob irgendwelche Eingaben vom Nutzer erfolgt
            if event.type == pygame.QUIT:       #   sind. Die Informationen kommen auhc aus dem Internet. Mit der Funktion
                runningBed = False              #   "pygmae.QUIT" wird überprüft, ob das Fenster geschlosssen werden soll,
                                                #   also auf das kleine Kreuz geclickt wird. wenn das der Fall ist, wird
                                                #   die VAriable "runnignBed" auf False gesetzt, weshalb wir dann aus der
                                                #   Schleife brechen.

        einGameOfLife.naechsterSchritt()    # Hiermit wird in unserer Instanz des GameOfLife der nächste zusatandes des
                                            #   Feldes berechnet und geschaut welche Zellen im naechsten Zeitschritt leben
                                            #   und welhce Sterben.

        draw(einGameOfLife.spielfeld)   # Hier rufen wir unsere Funktion zum Zeichnen des PSielfeldes auf, die wir weiter
                                        #   oben schon definiert haben. So wie wir unsere Fuktion oben definiert haben
                                        #   muessen iwr dann dort auch unser Spielfeld uebergeben damit die Inforamtionen
                                        #   ueber die Zellen von der "draw" Funktion richtig genutzt und aktualisiert
                                        #   werde koennen

        pygame.display.flip()   # wie bereits oben gesagt muss man bei pygame diesen befehl immer nochmal aufrufen um die
                                #   Aenderungen des Bidlschirm richtig darzustellen. Sowas findet man auch im Intenet

        time.sleep(0.2) # hier warten wir nocheinmal 0,2 Sekunden vor der nächsten Iteration.

