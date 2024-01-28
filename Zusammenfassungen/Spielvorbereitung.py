# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 17:47:26 2024

@author: schla
"""

import Texte.Spielaufforderung
import Texte.Ankuendigung_Wuerfeln

def Funktion_Spielvorbereitung():
    Zeile1 = Texte.Spielaufforderung.Funktion_Spielaufforderung()
    Zeile2 = Texte.Ankuendigung_Wuerfeln.Funktion_Ankuendigung_Wuerfeln()
    
    Spielvorbereitung = ('\n' + Zeile1 + '\n' +
                         Zeile2 + '\n'
                         )
    
    return Spielvorbereitung