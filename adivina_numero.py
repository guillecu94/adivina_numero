#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:13:15 2018

@author: guillermo.cuevas
"""

import random
def adivina_numero():
     i= random.randint(0,10)
     while (True):
        numero = int(input("El número está entre el 0 y el 15. Inserta un número "))
        if numero is not i:
            print ("has fallado, vuelve a intentarlo")
        else:
            print ("Enhorabuena, has acertado el número")
            break
    
adivina_numero()