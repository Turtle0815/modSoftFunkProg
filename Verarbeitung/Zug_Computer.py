# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 18:46:53 2024

@author: schla
"""

import Hilfen.Zufallsgenerator

def Funktion_Zug_Computer():
   Liste = ['x1', 'x2', 'x3', 'y1', 'y2', 'y3', 'z1', 'z2', 'z3']
   Auswahl = (Hilfen.Zufallsgenerator.Funktion_Zufallsgenerator(9))
   a = Auswahl - 1
   Zug  = Liste[a]
   
   return [Zug, 'o']