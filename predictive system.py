# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle 

loaded_model = pickle.load(open('C:/Users/Mian c/Downloads/Deploying Deep Learning Model/trained_model.sav', 'rb'))

lno = len(loaded_model)
#print(loaded_model)

if loaded_model == 0.3:
        print("Output =  Promoters")    
else:
        print("Output = Non-Promoters")