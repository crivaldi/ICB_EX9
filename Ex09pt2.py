# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:26:13 2018

Exercise 09 part 2

@author: Patricia
"""

import pandas
import matplotlib.pyplot as plt
import numpy as np

# data loaded into a data frame
data=pandas.read_csv("data.txt", sep=",")

# pt 1: make barplot with mean of the four populations
region = 'none'
for x in range(0,len(data)):
    region = str(data.iloc[x,0])
    if region == 'north':
        print('north')
    elif region == 'south':
        print('south')
    elif region == 'east': 
        print('east')
    elif region == 'west':
        print('west')