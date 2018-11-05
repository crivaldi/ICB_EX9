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
north = 0
south = 0
east = 0
west = 0
region = 'none'
for x in range(0,len(data)):
    region = str(data.iloc[x,0])
    if region == 'north':
        north = north + int(data.iloc[x,1])
    elif region == 'south':
        south = south + int(data.iloc[x,1])
    elif region == 'east': 
        east = east + int(data.iloc[x,1])
    elif region == 'west':
        west = west + int(data.iloc[x,1])

means = [north, south, east, west]

opacity = 0.8
n_groups = 4
fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

rects1 = ax.bar(index, means, bar_width, alpha = opacity, color='g')

ax.set_xlabel('Region')
ax.set_ylabel('Mean')
ax.set_title('Mean Observations per Region')
ax.set_xticks(index)
ax.set_xticklabels(('North', 'South', 'East', 'West'))
fig.tight_layout()
plt.show()










