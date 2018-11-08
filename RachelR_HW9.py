# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 17:21:02 2018

@author: Rachel R
"""

import numpy as np
import pandas as pd
import os
from plotnine import *

# Question 1: making a scatterplot from my data
os.chdir("C:\Users\Rachel R\documents")
cars=pd.read_csv("cars.txt",sep="\t",header=0)
a=ggplot(cars,aes(x="city-mpg",y="price"))
a+geom_point()

# Question 2: 
os.chdir("C:\Users\Rachel R\desktop\ICB_EX9")
data=pd.read_csv("data.txt",sep=",",header=0)
data.head(5)
# As a barplot of means 
b=ggplot(aes(data,x="region",y="observations"))
b+geom_bar(stat="identity", position='dodge')
# As a scatterplot 
b=ggplot(data,aes(x="region",y="observations"))
b+geom_point()
b+geom_jitter(alpha=0.1)
#The bar plot shows me that the mean observations for the east and south regions are practically identical, which the scatterplot proves to be untrue. The scatterplot shows that the east and south region observations are vastly different because the south region has a bimodal distribution. This bimodal distribution creates an illusive mean in the bar plot that is not descriptive of the actual data. 