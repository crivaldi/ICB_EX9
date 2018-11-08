#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 14:04:49 2018

@author: mlpoterek
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pylab

#Problem 1
location = r'/Users/mlpoterek/Biocomp/ICB_EX9/pred_obs.csv'
df = pd.read_csv(location,  encoding="utf-8-sig")

plt.plot("Predicted", "Observed",'bo', data = df)

#To generate the trendline
z = np.polyfit(df['Predicted'], df['Observed'], 1)
p = np.poly1d(z)
pylab.plot(df['Predicted'],p(df['Predicted']),"r--")  

#To add labels      
plt.ylabel('Observed Cases')
plt.xlabel('Predicted Cases')
plt.show

#Problem 2
location1 = r'/Users/mlpoterek/Biocomp/ICB_EX9/data.txt'
df1 = pd.read_csv(location1,  encoding="utf-8-sig")

north_df = df1[df1["region"]== "north"]
south_df = df1[df1["region"]== "south"]
east_df = df1[df1["region"]== "east"]
west_df = df1[df1["region"]== "west"]

#Bar graph of means
plt.bar(("north", "south", "east", "west"), (north_df['observations'].mean(), south_df['observations'].mean(), east_df['observations'].mean(), west_df['observations'].mean()))
plt.ylabel('Population Mean')
plt.xlabel('Region')
plt.show

#Scatter plot of all observations
sns.stripplot(x='region', y='observations', data=df1, jitter=True, alpha = .4)
sns.despine()

#The bar graph shows all four regions to be very similar, as each has 
#essentially the same population mean. The scatterplot, though, reveals that
#observations from the north region are clustered around the mean, that
#observations from the east and west regions are relatively consistently
#spread out around the mean, and that the south region's data is clustered into
#two distinct groups: one far above the mean and one far below. 
