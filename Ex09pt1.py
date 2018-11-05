# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 17:01:10 2018

Exercise09

@author: Patricia
"""

import pandas
import matplotlib.pyplot as plt
import numpy as np

# Part 1 Analysis of Sports Teaam data

# data loaded into a data frame
data=pandas.read_csv("incomevSAT.txt", sep="\t")

x = data.iloc[:,0] # sets x equal to income column
yR = data.iloc[:,1]
yM = data.iloc[:,2]
yW = data.iloc[:,3]
yC = yR + yM + yW # cumulative SAT
area = np.pi*3
colors = (0,0,0)


plt.scatter(x, yC, s=area, c=colors, alpha=0.5)
plt.title('Family Income vs SAT')
plt.xlabel('Family Income')
plt.ylabel('SAT score')
plt.show()
