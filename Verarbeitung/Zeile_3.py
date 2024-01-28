# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 11:42:14 2024

@author: schla
"""

Belegung_3 = [' ', ' ', ' ']

def Funktion_Zeile_3(x3, y3, z3):
    if Belegung_3[0] == ' ':
        if Belegung_3[0] != x3:
            Belegung_3[0] = x3
    if Belegung_3[1] == ' ':
        if Belegung_3[1] != y3:
            Belegung_3[1] = y3
    if Belegung_3[2] == ' ':
        if Belegung_3[2] != z3:
            Belegung_3[2] = z3
    
    return (Belegung_3)
    