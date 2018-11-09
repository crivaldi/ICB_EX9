#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 13:33:39 2018

@author: saurylara
"""

import numpy 
import pandas
from plotnine import *

#Import the SpouseAges text file
SpouseAges = pandas.read_csv("/Users/saurylara/Desktop/SpouseAges.txt",sep="\t",header=0)

#Create scatterplot of the two variables that includes a trendline
a=ggplot(SpouseAges,aes(x="HusbandAge",y="WifeAge"))+theme_classic()+geom_point()
print(a+xlab("HusbandAge (y)")+ylab("WifeAge (y)")+stat_smooth(method="lm"))

#Import the data file
data = pandas.read_csv("/Users/saurylara/Desktop/ICB_EX9/data.txt")

#Generate a barplot with means of the four populations
d=ggplot(data)+theme_classic()+xlab("region")+ylab("observations")
d=d+geom_bar(aes(x="region",y="observations"),stat="summary",fun_y=numpy.mean)
print(d)

#Plot a scatter plot of all of the observations
a=ggplot(data,aes(x="region",y="observations"))+theme_classic()+geom_jitter()
print(a)

# The bar and scatter plot do tell me different things because you do not get the full story just by looking at the bar graph with means.
# When I first plotted the data using the bar graph, I thought that all of the observations were fairly similar for each region given the mean for all four was about 15.
# When I plotted the scatter plot though, I was able to tell that the regions had very different data spreads.
# The data points in the West region were fully spread out, in the East region fairly spread out, in the South region there were many high/low values, and in the North region all of the values were concentrated around 15.




