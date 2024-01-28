# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:57:06 2024

@author: schla
"""

Felder_frei = ['x1', 'x2', 'x3', 'y1', 'y2', 'y3', 'z1', 'z2', 'z3']

def Funktion_Test_frei(Zug):
    a = 0
    frei = 0
    while a < len (Felder_frei):
        if Felder_frei[a] == Zug:
            Felder_frei.remove(Zug) 
            frei = 1
        a = a + 1    
    return frei