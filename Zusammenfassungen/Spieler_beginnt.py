# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 10:11:36 2024

@author: schla
"""

import Benutzereingaben.Zug_Spieler                                            # importiert die Funktion, die den Zug des Spielers abfragt
import Verarbeitung.Zug_Computer                                               # importiert die Fuktion, die den Zug des Computers festlegt
import Verarbeitung.Verarbeitung_Zug                                           # importiert die Funktion zur Verarbeitung der Züge; übergibt das Feld und den Spieler
import Verarbeitung.Test_frei                                                  # importiert die Funktion zur Prüfung, ob ein gewähltes Feld schon belegt ist
        
def Funktion_Spieler_beginnt():
    Anzahl_frei = 9    
    while Anzahl_frei > 0:
        Zug = (Benutzereingaben.Zug_Spieler.Funktion_Zug_Spieler())        
        Feld = Zug[0]
        Belegung = Zug[1]
        frei = (Verarbeitung.Test_frei.Funktion_Test_frei(Feld))
        while frei == 0:
            print ('Dieses Feld ist schon belegt. Bitte wähle ein anderes.')
            Zug = (Benutzereingaben.Zug_Spieler.Funktion_Zug_Spieler())
            Feld = Zug[0]
            frei = (Verarbeitung.Test_frei.Funktion_Test_frei(Feld))
        print ('')
        print (Verarbeitung.Verarbeitung_Zug.Funktion_Verarbeitung_Zug(Feld, Belegung))
        Summe = Verarbeitung.Pruefung_Summe.Funktion_Pruefung_Summe(Zug)
        if Summe == 3:
            print ('')
            print ('Herzlichen Glückwunsch, du hast gewonnen.')
            Anzahl_frei = 0
        else:
            Zug = (Verarbeitung.Zug_Computer.Funktion_Zug_Computer())
            Feld = Zug[0]
            Belegung = Zug[1]
            frei = (Verarbeitung.Test_frei.Funktion_Test_frei(Feld))
            while frei == 0:
                Zug = (Verarbeitung.Zug_Computer.Funktion_Zug_Computer())
                Feld = Zug[0]
                frei = (Verarbeitung.Test_frei.Funktion_Test_frei(Feld))
            print ('Mein Zug: ', Feld)
            print (' ')
            print (Verarbeitung.Verarbeitung_Zug.Funktion_Verarbeitung_Zug(Feld, Belegung))
            Summe = Verarbeitung.Pruefung_Summe.Funktion_Pruefung_Summe(Zug)
            if Summe == 12:
                print ('')
                print ('Ich habe gewonnen. Vielen Dank für das Spiel.')
                Anzahl_frei = 0
            else:
                Anzahl_frei = Anzahl_frei - 1   
        

        
