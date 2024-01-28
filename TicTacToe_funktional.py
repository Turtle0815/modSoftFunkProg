# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 16:49:12 2024

@author: schla
"""

# Import der verwendeten Funktionen

import Zusammenfassungen.Kopf                                          # importiert die Funktion für der Bereitstellung des Kopfes                          
import Zusammenfassungen.Spielvorbereitung                             # importiert die Funktion für die Darstellung der Spielvorbereitungen
import Benutzereingaben.Enter                                          # importiert die Funktion zum Abwarten der Benutzereingabe <Return>                  
import Verarbeitung.Wuerfeln                                           # importiert die Funktion zur Darstellung des Würfelns
import Verarbeitung.Spielfeld_Start                                    # importiert die Funktion zur Darstellung des leeren Anfangs-Spielfeldes
import Zusammenfassungen.Spieler_beginnt                               # importiert die Funktion zur Darstellung des Spiels wenn der Spieler den ersten Zug hat
import Zusammenfassungen.Computer_beginnt                              # importiert die Funktion zur Darstellung des Spiels wenn der Computer den ersten Zug hat

# Ablauf des Hauptprogramms

# Kopf

print (Zusammenfassungen.Kopf.Funktion_Kopf(), end = '')                                # stellt alle Strings des Kopfes dar
Benutzereingaben.Enter.Funktion_Enter()                                                 # erwartet <return> als Benutzereingabe

# Spielvorbereitung (Start-Spieler festlegen, erstes Spiefeld darstellen)

print (Zusammenfassungen.Spielvorbereitung.Funktion_Spielvorbereitung(), end = '')      # stellt alle Strings zur Spielvrobereitung dar
Wuerfel = (Verarbeitung.Wuerfeln.Funktion_Wuerfeln(2, 7, 2))                            # übergibt der Funktion Wuerfeln die Verzögerung, die Wartezeit und den Auswahl-Rang
print (Wuerfel[0])
print (Verarbeitung.Spielfeld_Start.Funktion_Spielfeld_Start())

if Wuerfel[1] == 1:                                                                     # Verzweigung des Programms je nach erstem Spieler
    (Zusammenfassungen.Spieler_beginnt.Funktion_Spieler_beginnt())
if Wuerfel[1] == 2:
    (Zusammenfassungen.Computer_beginnt.Funktion_Computer_beginnt())
