# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 11:42:14 2024

@author: schla
"""

Belegung_2 = [' ', ' ', ' ']

def Funktion_Zeile_2(x2, y2, z2):
    if Belegung_2[0] == ' ':
        if Belegung_2[0] != x2:
            Belegung_2[0] = x2
    if Belegung_2[1] == ' ':
        if Belegung_2[1] != y2:
            Belegung_2[1] = y2
    if Belegung_2[2] == ' ':
        if Belegung_2[2] != z2:
            Belegung_2[2] = z2
    
    return (Belegung_2)
    