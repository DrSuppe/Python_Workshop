from random import randint      #importiere die funktion "randint" aus der Bibliothek "random" (um Zufallszahlen zu erzeugen)
import time     #importiere die Bibliothek "time" (um Zeit zu nutzen)

##------------------VORBEREITUNG FueR DAS SPIEL---------------------

nRows = 30      #definiere die Anzahl der Zeilen mit einer Variable
nCollumns = 30      #definiere die Anzahl der Spalten mit einer Variable

world = []      #initialisiere ein leeres Array, dass wir als welt fuer das Game of Life nutzen

for i in range(nRows):      # start einer for-Schleife, die von 0 bis nRows-1 eingeschlossen hochzaehlt

    columns = []        # initalisiere ein weiteres leeres Array, das wir fuer die erste Spalte nutzen

    for j in range(nCollumns ):     # start einer for-Schleife, die von 0 bis nCollumns-1 eingeschlossen hochzaehlt

        columns.append([False, False])      # Fuege an jeder Stelle der Spalte "columns" das Array [Fals, False] ein
                                            #   Diese Werte sind dazu da um festzulegen, ob eine Zelle lebt oder tot ist
                                            #   Hier nutzen wir zei Speicherplaetze, weil wir einmal den aktuellen Zustand
                                            #   der Zelle sichern wollen und zusaetzlich auch noch den vergangenen.
                                            #   das ist wor allem nuetzlich, damit wir alle Nachbarn ueberpruefen koennen,
                                            #   ohne, dass die Haelfte der Nachbarn schon "verarbeitet" wurde

    world.append(columns)       # Fuege fuer jedes Element aus nRows die Spalte "columns" in "world" ein

            # Damit haben wir jetzt unser Spielfeld "world". World ist ein Array (Reih) von Arrays (Spalten) Wo an jeder
            #   Stelle zwei Werte fuer den Status der Zelle gespeichert sind.
            #   Anschaulicher dargestellt ist es ein 2D Feld, wo an jeder stelle ein Array mit zwei Eintraegen sitzt

for i in range(1, nRows-1):     # eine For-Schleife, die ueber alle Reihen außer die beiden aeußersten iteriert
    for j in range(1, nCollumns-1):     # eine For-Schleife, die ueber alle Spalten außer die beiden aeußersten iteriert
                                        #   Damit iterieren wir ueber alle Felder unserer "welt, asser dem "aeußersten"
                                        #   Ring an Feldern um zu vermeiden, dass man "aus dem Feld rauslaeuft"

        if randint(0, 4) == 1:      # If-Abfrage, wenn ein Zufallswert zwischen 0 und 4 = eins ist. Somit wird ein
                                    #   in einem Viertel aller Faelle die Bedingung erfuellt

            world[i][j][1]= True        # wenn deie Bedingung erfuellt ist, wird an der Position zu der wir gerade mit den
                                        #   for-Schleifen gezaehlt haben der zweite Wert auf "True" gesetzt.
                                        #   uebertragen heisst das, dass wir zufaellig ein Viertel der Zellen auf "lebend"
                                        #   setzen.

##------------------VORBEREITUNG FERTIG---------------------


##------------------LOGIK DES SPIELS ANFANG---------------------

def nextCycle():        # Hier definieren wir uns eine Funktion mit dem Name "nextCycle".
                        #   Diese Funktion hat keine Argumente und kann spaeter wieder aufgerufen werden
                        #   Alles was innerhalb der Funktion steht wird beim Aufruf ausgefuehrt

    for i in range(1, nRows -1):
        for j in range(1, nCollumns-1):     # Wieder eine Iteration über alle Felder des Spielfeles, ausser dem Rand

            # Hier kommen jetzte die "Spielregeln" des Game of Life
            if (world[i][j][1] == False and countNeighbours(i, j)  == 3):   # Wenn die Zelle an dem Punkt, an dem wir
                                                                            #   gerade mit den For-Schleifen sind tot ist
                                                                            #   und genau drei nachbarn hat...

                                                                            # In der Abfrage wird außerdem die Funktion
                                                                            #   "countNeighbours" aufgerufen und daher
                                                                            #   auch ausgeführt.

                world[i][j][0] = True       # ...wird sie Lebendig

            elif (world[i][j][1] == True and (countNeighbours(i, j) == 2 or countNeighbours(i, j) == 3)):
                                    # wenn eine Zelle lebt und zwei der drei Nachbarn hat,...

                world[i][j][0] = True       #...beliebt sie am Leben
            else:
                world[i][j][0] = False      # In allen anderen Fällen stirbt die Zelle, oder bleibt tot.


def countNeighbours( y, x):     # Hier wird die Funktion "countNeighbours" definiert. Diese Funktion fordert zwei
                                #   Argumente, die beim Aufruf der Funktion übergeben werden müssen und in der Funktion
                                #   verwendet werden.

    nNeighbours = 0     # Die Anzahl der lebenden Nachbarn wird mit 0 initialisiert

    for i in range(-1, 2):
        for j in range(-1, 2):      # Wieder eine Iteration, aber diesmal nur über alle 8 angrenzenden Felder

            if world[y + i][x + j][1] == True:      # Wenn eine Zelle auf einem der angrenzenden Felder lebt...
                nNeighbours += 1        #... wird der Zaehler der lebenden Nachbarn um e1 erhöht.

    # Allerdings haben wir jetzt die mittlere Zelle, deren Nachbarn wir zaehlen wollten mitgezaehlt...
    if world[y][x][1] == True:
        nNeighbours -= 1        # ...daher muessen wir von unserem Zaehler wieder eins abziehen, wenn die mittlere Zelle
                                #   lebendig ist.

    return nNeighbours      # Diese Funktion gibt die Anzahl der lebendigen NAchbarzellen zurueck.
                            #   Da die Anzahl der lebenden Nachbarn von der Art her eine einfache Zahl ist,
                            #   kann man die Funktion bei Aufruf  im Grunde als Zahl behandeln.

##------------------LOGIK DES SPIELS ENDE---------------------


def showWolrdOfLife():      # noch eine Funktion, die wir definieren. Diese Funktion soll unser Spiel auch darstellen
                            #   Ein richtiges GUI ist ein wenig aufwendig, deswegen machen wir hier eine sehr
                            #   rudimentäre darstellung in der Konolenausgabe

    print("--" * nRows)     # zuerst soll eine reihe von "--" gedruckt werden, damit ein Feld gegen das nächste
                            #   abgegrenzt wird.

    for i in range(1, nRows - 1):
        print("")       # dieses kleine gedruckte "nichts" ist dafür da, dass nach jeder Zeile ein Zeilenumbruch
                        #   eingefügt wird.

        for j in range(1, nCollumns - 1):   # mal wieder eine Iteration über alle Felder des Spielfeldes abgesehen von
                                            #   dem aeussersten Rand. Allerdings wird zwischendrinnen au

            if world[i][j][0] == True:      #Wenn eine Zelle lebt,...
                '''print("ausgabe True", end = "")'''
                print("X ", end=" ")        #   ... dann wird an ihrer Position ein X gedruckt. das "end=" "" ist dazu
                                            #   da, dass nicht nach jeder Zelle ein Zeilenumbruch entsteht.

                world[i][j][1] = world[i][j][0]     # ausserdem wird auch noch der zukuenftige Zustand gleich dem jetzigen
                                                    #   Zustand gesetzt.

            elif world[i][j][0] == False:       # Wenn eine Zelle tot is...
                '''# print("ausgabe false", end = "")
                # print(arr[i][j][0], end = "")'''
                print("  ", end=" ")        #... dann wird nur ein Leerzeichen gedruckt.

                world[i][j][1] = world[i][j][0]     # ausserdem wird auch noch der zukuenftige Zustand gleich dem jetzigen
                                                    #   Zustand gesetzt.
    print("")               # Nach jedem Feld wird ein Zeilenumbruch gedruckt und
    print("--" * nRows)     #   auch nochmal eine Trennlinie. Das ist alles nur zur Uebersicht.

if __name__ == "__main__":      # Diese If Abfrage sorgt dafür, dass die Datei nur ausgeführt wird, wenn man diese Datei
                                #   ausfuehrt. Das ist praktisch, weil man die Funktionen, die wir definiert haben evtl
                                #   aus einer anderen Datei raus aufrufen Will (wie bei Bibliotheken). In so einem Fall
                                #   Dann will man die ausfuehrbaren Dateien so abkapseln. Das ist einfach guter Stil

    while True:     # Im Grunde wird das immer wieder wiederholt... ohne Ende...

        # An dieser stele wurde oben das "Setup" schon ausgefuehrt. Wir haben also ein Spielfeld mit zufaellig lebenden
        #   und Zellen initialisiert und können damit arbeiten.

        nextCycle()     # Zuerst wird die Funktion "nextCycle" aufgerufen um den nachsten Satus des Spielfeldes
                        #   zu berechnen.

        showWolrdOfLife()       # Nachdem wir die naechste Iteration bestimmt haben, soll diese auch angezeigt werden

        time.sleep(0.1)       # Bevor die While-Schleife wiederholt wird wollen wir einen Moment warte, damit der
                            #   Rechner das ganze Ding nicht in unerkennbarer irwitziger Geschwindigkeit herunterrasselt.