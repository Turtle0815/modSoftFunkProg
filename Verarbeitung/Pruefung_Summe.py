# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 16:38:04 2024

@author: schla
"""

import Verarbeitung.Summe

Wert_Zeile_1 = [0, 0, 0]
Wert_Zeile_2 = [0, 0, 0]
Wert_Zeile_3 = [0, 0, 0]
Wert_Spalte_x = [0, 0, 0]
Wert_Spalte_y = [0, 0, 0]
Wert_Spalte_z = [0, 0, 0]
Wert_Diagonale_l = [0, 0, 0]
Wert_Diagonale_r = [0, 0, 0]

def Funktion_Pruefung_Summe(Zug):
    Feld = Zug[0] 
    Belegung = Zug[1]
    Summe = 0
    
    if Feld[0] == 'x':
        if Feld[1] == '1':
            if Belegung == 'x':
                Wert_Zeile_1[0] = 1
                Wert_Spalte_x[0] = 1
                Wert_Diagonale_l[0] = 1
            if Belegung == 'o':
                Wert_Zeile_1[0] = 4
                Wert_Spalte_x[0] = 4
                Wert_Diagonale_l[0] = 4
        if Feld[1] == '2':
            if Belegung == 'x':
                Wert_Zeile_2[0] = 1
                Wert_Spalte_x[1] = 1
            if Belegung == 'o':
                Wert_Zeile_2[0] = 4
                Wert_Spalte_x[1] = 4
        if Feld[1] == '3':
            if Belegung == 'x':
                Wert_Zeile_3[0] = 1
                Wert_Spalte_x[2] = 1
                Wert_Diagonale_r[2] = 1
            if Belegung == 'o':
                Wert_Zeile_3[0] = 4
                Wert_Spalte_x[2] = 4
                Wert_Diagonale_r[2] = 4
    if Feld[0] == 'y':
        if Feld[1] == '1':
            if Belegung == 'x':
                Wert_Zeile_1[1] = 1
                Wert_Spalte_y[0] = 1
            if Belegung == 'o':
                Wert_Zeile_1[1] = 1
                Wert_Spalte_y[0] = 1
        if Feld[1] == '2':
            if Belegung == 'x':
                Wert_Zeile_2[1] = 1
                Wert_Spalte_y[1] = 1
                Wert_Diagonale_l[1] = 1
                Wert_Diagonale_r[1] = 1
            if Belegung == 'o':
                Wert_Zeile_2[1] = 4
                Wert_Spalte_y[1] = 4
                Wert_Diagonale_l[1] = 4
                Wert_Diagonale_r[1] = 4
        if Feld[1] == '3':
            if Belegung == 'x':
                Wert_Zeile_3[1] = 1
                Wert_Spalte_y[2] = 1                
            if Belegung == 'o':
                Wert_Zeile_3[1] = 4
                Wert_Spalte_y[2] = 4 
    if Feld[0] == 'z':
        if Feld[1] == '1':
            if Belegung == 'x':
                Wert_Zeile_1[2] = 1
                Wert_Spalte_z[0] = 1
                Wert_Diagonale_r[0] = 1
            if Belegung == 'o':
                Wert_Zeile_1[2] = 4
                Wert_Spalte_z[0] = 4
                Wert_Diagonale_r[0] = 4
        if Feld[1] == '2':
            if Belegung == 'x':
                Wert_Zeile_2[2] = 1
                Wert_Spalte_z[1] = 1
            if Belegung == 'o':
                Wert_Zeile_2[2] = 4
                Wert_Spalte_z[1] = 4
        if Feld[1] == '3':
            if Belegung == 'x':
                Wert_Zeile_3[2] = 1
                Wert_Spalte_z[2] = 1
                Wert_Diagonale_l[2] = 1                
            if Belegung == 'o':
                Wert_Zeile_3[2] = 4
                Wert_Spalte_z[2] = 4
                Wert_Diagonale_l[2] = 4 
                
    Summe_Spalte_x = Verarbeitung.Summe.Funktion_Summe(Wert_Spalte_x)
    Summe_Spalte_y = Verarbeitung.Summe.Funktion_Summe(Wert_Spalte_y)
    Summe_Spalte_z = Verarbeitung.Summe.Funktion_Summe(Wert_Spalte_z)
    Summe_Zeile_1 = Verarbeitung.Summe.Funktion_Summe(Wert_Zeile_1)
    Summe_Zeile_2 = Verarbeitung.Summe.Funktion_Summe(Wert_Zeile_2)
    Summe_Zeile_3 = Verarbeitung.Summe.Funktion_Summe(Wert_Zeile_3)
    Summe_Diagonale_l = Verarbeitung.Summe.Funktion_Summe(Wert_Diagonale_l)
    Summe_Diagonale_r = Verarbeitung.Summe.Funktion_Summe(Wert_Diagonale_r)
    
    if  (Summe_Spalte_x   == 3 or
        Summe_Spalte_y    == 3 or
        Summe_Spalte_z    == 3 or
        Summe_Zeile_1     == 3 or
        Summe_Zeile_2     == 3 or
        Summe_Zeile_3     == 3 or
        Summe_Diagonale_l == 3 or
        Summe_Diagonale_r == 3):
        Summe = 3
        
    if  (Summe_Spalte_x   == 12 or
        Summe_Spalte_y    == 12 or
        Summe_Spalte_z    == 12 or
        Summe_Zeile_1     == 12 or
        Summe_Zeile_2     == 12 or
        Summe_Zeile_3     == 12 or
        Summe_Diagonale_l == 12 or
        Summe_Diagonale_r == 12):
        Summe = 3
        
    return Summe