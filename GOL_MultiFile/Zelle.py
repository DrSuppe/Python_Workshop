class meineZelle:       # beginn der Anleitung(Klasse) für eine Zelle

    def __init__(self):     #Die "__init__-Funktion" wird immer aufgerufen, wenn nach dem Bauplan
                            # "meineZelle" ein Objekt gebaut wird.

        self.status = False                 # in der "__init__-Funktion" kann man Variablen definieren,
        self.naechsterStatus = False        # welche nach der Anleitung "meineZelle" zu dem Objekt gehören sollen



    def zaeleNachbarn(self, Zeile, Spalte, spielfeld):  # hier wird eine Funktion definiert, die zu einem Objekt
                                                        # gehören soll, das nach der Anleitung(Klasse) "meineZelle"
                                                        # gebaut werden soll

        nNachbarn = 0       # diese Funktion soll die Anzahl der lebenen nachbarn zählen.
                            # daher wird jedes Mal, wenn gezählt wird die Anzahl als 0 definiert

        for i in range(-1, 2):              # Diese beiden "For-Schleifen" itereieren weisen den Werten i und j
            for j in range(-1, 2):          # nacheinander die Werte (-1, 0, 1) zu.
                                            # dadurch hat man sozusagen ein 3 mal 3 Feld: (-1,-1) (-1,0) (-1,1)
                                            #                                             (0,-1)  (0,0)  (0,1)
                                            #                                             (1,-1)  (1,0)  (1,-1)


                if spielfeld[Zeile + i][Spalte + j].status == True:     # Hier wird überprüft ob eine Nachbarzelle lebendig ist
                                                                        # Dafür wird die Position der aktuellen Zelle mit
                                                                        # "spielfeld[Zeile][Spalte]" abgerufen. Da wir jetzt
                                                                        # von -1 bis 1 in beide Richtungen Iterieren und diese Werte
                                                                        # zu der Zellenpoition addieren, wird die aktuelle Zelle zum
                                                                        # Mittelpunkt des obden dargestellten 3x3 Feldes:(-1,-1)    (-1,0)         (-1,1)
                                                                        #                                                (0,-1)  (aktuelle Zelle)  (0,1)
                                                                        #                                                (1,-1)     (1,0)          (1,-1)

                    nNachbarn += 1      # Wenn eine Nachbarzelle lebendig ist, wird der Zähler,
                                        # der die lebendigen Nachbarn zählt um 1 erhöht


        if spielfeld[Zeile][Spalte].status == True:     # Da wir auch die Mosition der eigenen Zelle abfragen
                                                        # wird in die vorangegangene Zählung auch der Wert der
                                                        # eigenen zelle gezählt. Um Das zu vermeiden muss man 1 wieder
                                                        # abziehen, wenn die eigene Zelle lebendig ist.
            nNachbarn -= 1

        return nNachbarn        # sorgt dafür, dass das Ausführen dieser Funktion den Wert "nNachbarn" gitb.
                                # man kann also sagen, dass meineVariable = zaeleNachbarn(Zeile,Spalte,Population)
                                #   in dem Fall würde meineVariable = nNachbarn der Zelle an der Stelle (Zeile, Spalte) sein
