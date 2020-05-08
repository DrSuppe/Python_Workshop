from Spiellogik import GameOfLife
import time

nZeilen = 20    # Die Anzahl der Zeilen, die das Spielfeld haben soll
nSpalten = 20   # Die Anzahl der Spalten, die das Spielfeld haben soll

                # sind hier als Variabeln defineirt, damit wir sie später verwenden können.
                # Wenn das Format des Spielfeldes geändert werden soll, kann man diese Variablen anpassen

def konsolenAusgabe(spielfeld):     # Dies ist die Funktion, die Beschriebt, wie das SPiel dargestellt werden soll

    for i in range(1, nZeilen-1):   # "For-Schleife" iteriert über alle Zeilen, ausser der
                                    # ersten und der Letzten, damit der Rand nicht betrachtet wird

        print("")       # ist hier hinzugefügt, damit nach jeder Zeile eine neue Zeile angefangen wird.

        for j in range(1, nSpalten -1):     # "For-Schleife" iteriert über alle Spalten, ausser der
                                            # ersten und der Letzten, damit der Rand nicht betrachtet wird

            if spielfeld[i][j].naechsterStatus == True:     #Wenn die Zelle lebt soll folgendes passsieren.

                print("X ", end=" ")        #schreibe ein X ohen Zeilenumbruch in die Konsole

                spielfeld[i][j].status = spielfeld[i][j].naechsterStatus    # Setze den Aktuellen Status als den nächsten
                                                                            # status. Damit wird der Alte Status verworfen,
                                                                            # der nächste Status wird zum aktuellen status
                                                                            # und es kann der neue "naechsteStatus" berechnet werden

            else:       # Wenn die Zelle nicht lebt (also tot ist) sollfolgendes passieren

                print("  ", end=" ")    #schreibe ein Lehrzeichen ohen Zeilenumbruch in die Konsole

                spielfeld[i][j].status = spielfeld[i][j].naechsterStatus    # Setze den Aktuellen Status als den nächsten
                                                                            # status. Damit wird der Alte Status verworfen,
                                                                            # der nächste Status wird zum aktuellen status
                                                                            # und es kann der neue "naechsteStatus" berechnet werden


    print("")       # nach der letzten zeile muss uach noch ein Zeilenumbruch ausgegeben werden,damit die
                    # Trennlinie nicht hinter der letzten Zeile in die selbe Zeile geschrieben wird.

    print("-------------------------------------------------------")    # eine Trennlinie soll in der Konsole ausgegebn werden
                                                                        # damit man die Spielfelder gut voneinander abgrenzen kann


spiel = GameOfLife(nZeilen, nSpalten)   # nutzt den Bauplan der Klasse GameOfLife um ein GameOfLife mit dem Namen
                                        # "spiel" zu bauen. "spiel" ist also ein Objekt, das nach der Anleitung(Klasse)
                                        # GameOfLife gebaut wurd. "spiel" ist ein Objekt und eine Instanz der Klasse

                                        # in der AUto Analogie wäre "spiel" ein bestimmtes Auto, welches nach dem Bauplan gebaut wurde

spiel.erstelleSpielfeld()   #Hier wird von dem Objekt "spiel" die Methode "erstelle SPielfeld aufgerufen.
                            #"speil wurde nach der Anleitung der Klassse "GameOfLife" Gebaut.
                            # In der Anleitung(Klasse) "GameOfLife" haben wir auch eine Funktion definiert,
                            # die ein Spielfeld aufbaut. Jedes Objekt, welches also nach der Anleitung(Klasse)
                            # "GameOfLife" gebaut wird, hat also auch die Funktion "erstelleSpielfeld" eingebaut.

                            #mit dem Ausruckt "spiel.erstelleSpielfeld()" sagt man, dass das Objet "spiel"
                            # die  Funktion "erstelleSpielfeld" für sich ausführen soll.



while True:     # diese While Schleife sorgt dafür, dass die schritte immer weider aufgerufen werden,
                # damit alle Funktionen in der "While-Schleife" immer wieder ausgeführt werden.
                # Da wir nirgends gesagt haben, wann die Whle Schleife aufhören soll,
                # geht das  auch ewig weiter. Man muss es also manuell beenden.

    spiel.naechsterSchritt()        #führt von dem Objekt "spiel" die Funktion "naechsterSchrit()" aus

    konsolenAusgabe(spiel.spielfeld)    # führt die Funktion Konsolenausgabe aus

    time.sleep(1)       # das ist eine kleine Verzögerung in Sekunden bevor es weiter geht
                        # hier wartet das Programm "time.sleep(Sekunden)"
                        # das haben wir am ende einfach noch eingbeaut, weil das Spiel sonst ziemlich
                        # schnell läuft und man nicht viel erkennt.

                        # Um "time.sleep(Sekunden)" zu nutzen haben wir oben noch "time" importiert.
                        # man kann die Zeit auch beliebig anpassen. Auch Kommazahlen (z.B. 0,3 oder 1,5) funktionieren
