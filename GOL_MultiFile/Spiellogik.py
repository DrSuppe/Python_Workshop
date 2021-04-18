from Zelle import meineZelle    # Ermöglicht das verwenden von allen Sachen, die in Zelle enthalten sind.

import random   # importiert die Bibliothek  random. Diese Bibliothek ermöglicht es zufallszahlen zu generieren.

class GameOfLife:   # beginn der Anleitung(Klasse) für "GameofLife"

    def __init__(self, inputZeile, inputSpalte):    # Die "__init__-Funktion" wird immer aufgerufen, wenn nach dem Bauplan
                                                    # "GameOfLife" ein Objekt gebaut wird. ganz genau so, wie bei der Zelle

        self.nZeilen = inputZeile           # In der "__init__-Funktion" kann man Variablen definieren,
        self.nSpalten = inputSpalte         # welche nach der Anleitung "GameOfLife" zu dem Objekt gehören sollen
                                            # auch ganz genau so, wie bei der Zelle.

    def erstelleSpielfeld(self):    # hier wird eine Funktion definiert, die zu einem Objekt
                                    # gehören soll, das nach der Anleitung(Klasse) "GameOfLife"
                                    # gebaut werden soll. Auch das funktioniert genau so wie bei der Zelle

        self.spielfeld = []         # hier definieren wir ein weitere Attribut der Klasse "GameOfLife"
                                    # Das Attribut "spielfeld" wird hier erstmal als lehrer Array(Liste)
                                    # erstellt, um es später zu füllen.

        for i in range(self.nZeilen):       # diese For-Schleife iteriert über alle Zeilen des Objektes, welches
                                            # nach der Anleitung "GameOfLife" erstellt wurde

            spalte = []         # erstellt für jede Zeil eine neues lehres Array (Liste) mit Namen "spalte"

            for j in range(self.nSpalten):      # Diese For-Schleife iteriert für jede Zeile über alle Spalten des Objektes,
                                                # welches nach der Anleitung "GameOfLife" erstellt wurde

                spalte.append(meineZelle())     # Fügt dem Array "spalte" ein Objekt das nach der ANleitung der Klasse
                                                # "meineZelle" gebaut wurde hinzu.
                                                # dadurch wird das Array "spalte" mit so vielen objekten die nach der
                                                # Anleitung "meineZelle" gebaut sind aufgefüllt, wie es Spalten gibt.

            self.spielfeld.append(spalte)   # diese fügt dem Array "spielfeld"(das auch ein attribut des Objktes "GameOfLife" ist)
                                            # für jede Zeile einen Array Spalte hinzu.
                                            # dadurch entsteht eine Liste ("spielfeld") dessen Elemente alle
                                            # Listen ("spalte") sind. Dadurch haben wir im Grunde eine
                                            # 2D Matrix erstellt.


        for i in range(self.nZeilen):               # Diese beiden For-Schleifen iterieren über alle Zeilen
            for j in range(self.nSpalten):          # und alle Spalten der gerade erstellten 2D-Matrix (Liste von Listen)
                                                    # und betrachtet jedes einzelne enthaltene Element

                if (random.randint(0, 4)) == 1:         # hier wird die Funktion "random.randint(0, 4)" verwendet.
                                                        # das ist hier möglich, weil wir oben die Bibliothe "random importiert
                                                        # haben. Diese Funktion generiert eine zufallsnummer aus (o,1,2,3,4).
                                                        # Wenn diese Zufallszahl = 1 ist, wird der Code in der If-Abfrage ausgeführt.

                    self.spielfeld[i][j].status = True      # Hier wird das Attribut "status" des Objektes, das nach der Anleitung
                                                            # "meineZelle" gebaut wurde und in der 2D-Matrix an der Stelle
                                                            # (i,j) sitzt, auf "True" (also lebendig) geschaltet.

                if i == 0 or j == 0 or i == self.nZeilen-1 or j == self.nSpalten-1:     # Hier wird in der If-Abfrage geschaut, ob die aktuell
                                                                                        # betrachtete zelle Eine Bosition hat, wo irgendeine
                                                                                        # Koordinate minimal oder maximal ist. Also ob die
                                                                                        # aktuelle Zelle am Rand liegt.

                    self.spielfeld[i][j].status = False     # Wird ausgeführt, wenn eine Zelle Am Radn liegt. Hier wird das
                                                            # Attribut "status" des Objektes, das nach der Anleitung
                                                            # "meineZelle" gebaut wurde und in der 2D-Matrix an der Stelle
                                                            # (i,j) sitzt, auf "False" (also tot) geschaltet.



    def naechsterSchritt(self):     # hier wird eine Funktion definiert, die zu einem Objekt
                                    # gehören soll, das nach der Anleitung(Klasse) "GameOfLife"
                                    # gebaut werden soll. Auch das funktioniert genau so wie bei der Zelle
                                    # oder we bei der vorangegangenen Funktion.

        for i in range(1, self.nZeilen -1):         # Diese beiden For-Schleifen iterieren über fast alle Zeilen
            for j in range(1, self.nSpalten -1):    # und fast alle Spalten der gerade erstellten 2D-Matrix(Liste von Listen)
                                                    # und betrachtet jedes einzelne enthaltene Element.
                                                    # Da die For-Schleife von 1 bis Zeilen-1 geht (und bei den Spalten analog)
                                                    # werden hier die Ränder der 2D-Matrix nicht beachtet.

                # Die nachfolgenden If-Abfragen beschrieben die Logik des Game of Life.
                # Also alle Regeln, wann eine Zelle überlebt, stirbt oder zum Leben erwacht
                if self.spielfeld[i][j].status == False and  self.spielfeld[i][j].zaeleNachbarn(i, j, self.spielfeld ) == 3:
                    # Wenn das Attribut "status" einer Zelle am Ort (i,j) der 2D-matrix Falsch (also tot) ist
                    # und gleichzeitig die Methode "zaehleNachbarn()" der Zelle am Ort (i,j) der 2D-matrix erkennt,
                    # dass 3 Nachbarn am Leben sind wird das Folgenede ausgeführt:

                    self.spielfeld[i][j].naechsterStatus = True # Setzt das Attribut "naechsterStatus" der Zelle an der
                                                                # position (i,j) der 2D-Matrix auf "True"
                                                                #       -> die Zelle erwacht zum Leben.

                elif self.spielfeld[i][j].status == True and (self.spielfeld[i][j].zaeleNachbarn(i, j , self.spielfeld) == 3 or self.spielfeld[i][j].zaeleNachbarn(i, j , self.spielfeld) == 2):
                    # Wenn das Attribut "status" einer Zelle am Ort (i,j) der 2D-matrix "True" (also lebendig) ist
                    # und gleichzeitig die Methode "zaehleNachbarn()" der Zelle am Ort (i,j) der 2D-matrix erkennt,
                    # dass entweder 2 oder 3 Nachbarn am Leben sind wird das Folgenede ausgeführt:

                    self.spielfeld[i][j].naechsterStatus = True # Setzt das Attribut "naechsterStatus" der Zelle an der
                                                                # position (i,j) der 2D-Matrix auf "True"
                                                                #       -> die Zelle bleibt am Leben.

                else:       # In allen anderen Fällen wird flgendes Ausgeführt:

                    self.spielfeld[i][j].naechsterStatus = False    # Setzt das Attribut "naechsterStatus" der Zelle an der
                                                                    # position (i,j) der 2D-Matrix auf "False"
                                                                    #       -> die Zelle bleibt tot, wenn sie tot ist un dnicht genau 3
                                                                    #           Nachbarn hat.
                                                                    #       -> Zelle stirbt, wenn sie nicht genau 2 oder 3 Nachbarn hat.

