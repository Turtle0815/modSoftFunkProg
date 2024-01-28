# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 10:21:39 2024

@author: schla
"""

import Texte.Spielfeld_Titel

def Funktion_Spielfeld_Start():
    print (Texte.Spielfeld_Titel.Funktion_Spielfeld_Titel())
    Zeile1 = '     x    y    z'
    Zeile2 = ''
    Zeile3 = '1'
    Zeile4 = '2'
    Zeile5 = '3'
    
    Feld = Zeile1 + '\n' + Zeile2 + '\n' + Zeile3 + '\n' + Zeile2 + '\n' + Zeile4 + '\n' + Zeile2 + '\n' + Zeile5 + '\n' + Zeile2
     
    return Feld