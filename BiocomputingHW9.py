# -*- coding: utf-8 -*-
"""
Created on Thu Nov 08 17:31:50 2018

@author: Alexis
"""

import numpy as np
import pandas as pd
from plotnine import *
#problem 1
df=pd.read_csv("Ice_cream_sold_in_Temp.txt") #reads ice cream file

a=ggplot(df,aes(x="temperature",y="Number of ice-creams sold")) #tell what df and columns to read
a=a+geom_point()+coord_cartesian() #changes how plotted
a=a+xlab("Temperature of day in Celsius")+ylab("Number of ice creams sold")+stat_smooth(method="lm")#Adds label
a=a+theme_bw()+ggtitle("Temperature of day Vs ice cream sold")#adds title and makes background white
print(a) #prints a 

#problem 2 HW9
datadf=pd.read_csv("data.txt") #reads data.txt

d=ggplot(datadf)+theme_classic()+xlab("Region")+ylab("Mean number of observations") #tells what columns are of interest
d=d+geom_bar(aes(x="factor(region)",fill="region",y="observations"),stat="summary",fun_y=np.mean)#finds the mean of regions
d=d+scale_fill_manual(values=["Midnightblue", "blue", "royalblue","aquamarine"]) #gives color to region
print(d)

b=ggplot(datadf,aes(x="region",y="observations"))#tells what columns are of interest 
b=b+theme_classic()+geom_jitter()#adds jiter to make it look nicer
print(b) #prints b

#double checking mean
SouthRows=datadf[datadf.region=='south']
SouthMean=SouthRows['observations'].mean()
NorthRows=datadf[datadf.region=='north']
NorthMean=NorthRows['observations'].mean()
WestRows=datadf[datadf.region=='west']
WestMean=WestRows['observations'].mean()
EastRows=datadf[datadf.region=='east']
EastMean=EastRows['observations'].mean()

#Yes the bar graph and the scatter plots tell different stories.
#The bar graph shows that the means of the regions are very similar in value
#One may conclude that as the means are almost the same, their observations are similar as well
#However looking at the scatterplot tells a different story. 
#The scatterplot shows that the regions all have vastly different distribution spreads.
#From a dense distribution for the north region to the sparsly distribution for west
#As such to get the full picture both graphs are needed



 