# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:50:51 2018

@author: Annaliese
"""

# Exercise 9

# import packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from plotnine import *

##############################################

# Part One

# define file name 
file = "season.data.csv"

# read the csv file in
data = pd.read_csv("season.data.csv")

# produce a scatterplot
data.columns.values
x = data.loc[:,'tech.score']
y = data.loc[:, 'comp.score']

# calculate trend line
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

# plot
plt.scatter(x, y)
plt.xlabel("Technical Score")
plt.ylabel("Component Score")
plt.title("Component Score vs. Technical Score for the 2017-2018 Figure Skating Grand Prix Season")
plt.plot(x, p(x), "r--")

# I included this data inthe assignment submission for reproducibility

#########################################################

# get new data
data = pd.read_csv("data.txt")

# calculate the means by each region
means = data.groupby('region')['observations'].mean()

# make a bar plot
means.plot(kind = "bar")

# make scatter plot
base = ggplot(data, aes(x = "region", y = "observations"))
base + geom_point() + geom_jitter() + theme_classic()

# The two plots show very different information. The bar plot shows that all 
# of the means are very close together, but the scatterplot reveals
# that the spread of the data varies with the region. The West and East 
# regions have large variability in their observations, whereas North has
# very little variation. The south region has two modes for its observations,
# which is very different from the others.