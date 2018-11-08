# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:26:13 2018

Exercise 09 part 2

@author: Patricia
"""

import pandas
import matplotlib.pyplot as plt
import numpy as np
from plotnine import *

# data loaded into a data frame
data=pandas.read_csv("data.txt", sep=",")

# pt 1: make barplot with mean of the four populations using matplotlib
north = 0
north_count = 0
south = 0
south_count = 0
east = 0
east_count = 0
west = 0
west_count = 0
region = 'none'
# iterate through data frame to get sum of north,south,east,west and their # observations
for x in range(0,len(data)):
    region = str(data.iloc[x,0])
    if region == 'north':
        north = north + int(data.iloc[x,1])
        north_count = north_count + 1
    elif region == 'south':
        south = south + int(data.iloc[x,1])
        south_count = south_count + 1
    elif region == 'east': 
        east = east + int(data.iloc[x,1])
        east_count = east_count + 1
    elif region == 'west':
        west = west + int(data.iloc[x,1])
        west_count = west_count + 1
# find mean of each area using sum and count
means = [north/north_count, south/south_count, east/east_count, west/west_count]

opacity = 0.8 # a color strength I liked
n_groups = 4 # 4 bars
fig, ax = plt.subplots() # bar graph is named ax

index = np.arange(n_groups)
bar_width = 0.35 # width of bar

rects = ax.bar(index, means, bar_width, alpha = opacity, color='g') #graph

ax.set_xlabel('Region')#x axis label
ax.set_ylabel('Mean')# y axis label
ax.set_title('Mean Observations per Region')# title
ax.set_xticks(index) # middle of each bar
ax.set_xticklabels(('North', 'South', 'East', 'West'))# labels to x axis
fig.tight_layout()# nice layout
plt.show() #display

# part 2: a scatterplot of the data using plotnine
scatter = ggplot(data,aes(x="region",y="observations"))
print(scatter+geom_point(alpha=0.1)+theme_classic())


