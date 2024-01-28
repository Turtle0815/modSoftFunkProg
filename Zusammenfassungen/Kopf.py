# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 16:54:21 2024

@author: schla
"""

import Texte.Verfasser                                           
import Texte.Titel
import Texte.Regeln

def Funktion_Kopf():
    Zeile1 = Texte.Verfasser.Funktion_Verfasser()              # String mit Informationen zum Verfasser
    Zeile2 = Texte.Titel.Funktion_Titel()                      # String mit Informationen zum Titel
    Zeile3 = Texte.Regeln.Funktion_Regeln()                    # String mit Infromationen zum Titel
    
    Kopf = (Zeile1 + '\n' +
            Zeile2 + '\n' +
            Zeile3
           )
    return Kopf