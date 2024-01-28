# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 11:42:14 2024

@author: schla
"""

Belegung_1 = [' ', ' ', ' ']

def Funktion_Zeile_1(x1, y1, z1):
    if Belegung_1[0] == ' ':
        if Belegung_1[0] != x1:
            Belegung_1[0] = x1
    if Belegung_1[1] == ' ':
        if Belegung_1[1] != y1:
            Belegung_1[1] = y1
    if Belegung_1[2] == ' ':
        if Belegung_1[2] != z1:
            Belegung_1[2] = z1
    
    return Belegung_1
    