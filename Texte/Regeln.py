# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 17:03:11 2024

@author: schla
"""

def Funktion_Regeln ():        # Verfasserinformationen
    Zeile1 = 'Die Regeln:'
    Zeile2 = 'Tic-Tac-Toe wird von zwei Spielern auf einem 3x3 - Spielfeld gespielt.'
    Zeile3 = 'Die Spieler kennzeichnen abwechselnd ein Feld auf dem Spielfeld mit dem Ziel, als erster Drei Felder in einer Reihe, Spalte oder Diagonale zu kennzeichnen.'
    Zeile4 = 'Deine Züge werden mit x gekennzeichnet und meine mit o.'
    Zeile5 = 'Gib bitte immer das Feld ein, das du belegen möchtest. (z.B. x1)'
    Zeile6 = 'Alles klar? Weiter mit "Enter"!'
    
    Regeln = (Zeile1 + '\n' +
             Zeile2 + '\n' +
             Zeile3 + '\n' + '\n' +
             Zeile4 + '\n' +
             Zeile5 + '\n' + '\n' +
             Zeile6
            ) 
                
    return Regeln