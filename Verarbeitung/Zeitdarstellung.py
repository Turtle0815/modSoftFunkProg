# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 07:31:47 2024

@author: schla
"""

import time

def Funktion_Zeitdarstellung(Zeit):
    a = 0
    while a < Zeit:
        print ('.', end = '')       
        time.sleep(0.3)
        a = a + 1
    print ('')
    print ('')

    