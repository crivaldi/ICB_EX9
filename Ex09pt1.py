# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 17:01:10 2018

Exercise09

@author: Patricia
"""
import pandas
import matplotlib.pyplot as plt
import numpy as np
from plotnine import *


# data loaded into a data frame
data=pandas.read_csv("incomevSAT.txt", sep="\t")

x = data.iloc[:,0] # sets x equal to income column
yR = data.iloc[:,1] # gets SAT Reading scores
yM = data.iloc[:,2] # gets SAT Math scores
yW = data.iloc[:,3] # gets SAT Writing scores
yC = yR + yM + yW # cumulative SAT

plt.scatter(x, yC)
plt.title('Family Income vs. SAT')
plt.xlabel('Family Income') # x axis label
plt.ylabel('SAT score') # y axis label
z = np.polyfit(x,yC,1) # finds the linear line of best fit
p = np.poly1d(z)
plt.plot(x,p(x),"r--")
plt.show()

