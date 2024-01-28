# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 11:25:12 2024

@author: schla
"""
import Verarbeitung.Zeile_1
import Verarbeitung.Zeile_2
import Verarbeitung.Zeile_3
import Verarbeitung.Pruefung_Summe

def Funktion_Verarbeitung_Zug(Feld, Belegung):
    Spalte = Feld[0]
    Zeile = Feld[1]
    if Zeile == '1':
        if Spalte == 'x':
            Belegung_1 = (Verarbeitung.Zeile_1.Funktion_Zeile_1(Belegung, ' ', ' '))
        if Spalte == 'y':
            Belegung_1 = (Verarbeitung.Zeile_1.Funktion_Zeile_1(' ', Belegung, ' '))
        if Spalte == 'z':
            Belegung_1 = (Verarbeitung.Zeile_1.Funktion_Zeile_1(' ', ' ', Belegung))
    else:
        Belegung_1 = (Verarbeitung.Zeile_1.Funktion_Zeile_1(' ', ' ', ' '))
    if Zeile == '2':
        if Spalte == 'x':
            Belegung_2 = (Verarbeitung.Zeile_2.Funktion_Zeile_2(Belegung, ' ', ' '))
        if Spalte == 'y':
            Belegung_2 = (Verarbeitung.Zeile_2.Funktion_Zeile_2(' ', Belegung, ' '))
        if Spalte == 'z':
            Belegung_2 = (Verarbeitung.Zeile_2.Funktion_Zeile_2(' ', ' ', Belegung))
    else:
        Belegung_2 = (Verarbeitung.Zeile_2.Funktion_Zeile_2(' ', ' ', ' '))
    if Zeile == '3':
        if Spalte == 'x':
            Belegung_3 = (Verarbeitung.Zeile_3.Funktion_Zeile_3(Belegung, ' ', ' '))
        if Spalte == 'y':
            Belegung_3 = (Verarbeitung.Zeile_3.Funktion_Zeile_3(' ', Belegung, ' '))
        if Spalte == 'z':
            Belegung_3 = (Verarbeitung.Zeile_3.Funktion_Zeile_3(' ', ' ', Belegung))
    else:
        Belegung_3 = (Verarbeitung.Zeile_3.Funktion_Zeile_3(' ', ' ', ' '))
               
    Zeile1 = '     x    y    z'
    Zeile2 = ''
    Zeile3 = '1    ' + Belegung_1[0] + '    ' + Belegung_1[1] + '    ' + Belegung_1[2]
    Zeile4 = '2    ' + Belegung_2[0] + '    ' + Belegung_2[1] + '    ' + Belegung_2[2]
    Zeile5 = '3    ' + Belegung_3[0] + '    ' + Belegung_3[1] + '    ' + Belegung_3[2]
    
    Feld = Zeile1 + '\n' + Zeile2 + '\n' + Zeile3 + '\n' + Zeile2 + '\n' + Zeile4 + '\n' + Zeile2 + '\n' + Zeile5 + '\n' + Zeile2
     
    return Feld