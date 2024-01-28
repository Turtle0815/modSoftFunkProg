# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 07:33:37 2024

@author: schla
"""

import random

def Funktion_Zufallsgenerator(Range):
    Ergebnis = random.choice(range(1, Range))                        # gibt eine Zufallszahl zwischen 1 und der mit dem Aufruf übergebenen Zahl zurück
    return Ergebnis
    