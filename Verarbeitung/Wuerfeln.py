# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 07:12:29 2024

@author: schla
"""

import Verarbeitung.Zeitverzoegerung     # importiert die Funktion zum Einbau einer Zeitverzögerung
import Verarbeitung.Zeitdarstellung      # importiert die Funktion zur Darstellung eines Zeitablaufs
import Hilfen.Zufallsgenerator           # importiert die Funktion Zufallsgenerator

def Funktion_Wuerfeln(Verzoegerung, Zeit, Range):
    Verarbeitung.Zeitverzoegerung.Funktion_Zeitverzoegerung(Verzoegerung)      # baut eine Zeitverzögerung ein, damit der Nutzer in Ruhe fertig lesen kann
    Verarbeitung.Zeitdarstellung.Funktion_Zeitdarstellung(Zeit)
    Ergebnis = Hilfen.Zufallsgenerator.Funktion_Zufallsgenerator(Range)   
   
    if Ergebnis == 1:
        return ('Du beginnst.', 1)
    if Ergebnis == 2:
        return ('Ich beginne.', 2)