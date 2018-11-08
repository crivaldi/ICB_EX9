# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 22:37:17 2018

@author: Alicia
"""
import numpy
import pandas
from plotnine import *
#Question 1 - sample data for Gray Kangaroos
data=pandas.read_csv("GrayKangaroo.txt",sep="\t",header=0)
data.head(5)
a=ggplot(data,aes(x="Nasal Length",y="Nasal Width"))
a+geom_point()+coord_cartesian()+theme_classic()+stat_smooth(method="lm")

#Question 2
data=pandas.read_csv("data.txt",sep=",",header=0)
data.head(5)
df=ggplot(data)+theme_classic()+xlab("region")+ylab("observations")
df+geom_bar(aes(x="factor(region)",y="observations"),stat="summary",fun_y=numpy.mean)
#To check barplot mean values are correct
data.groupby(['region'])['observations'].mean()

a=ggplot(data,aes(x="region",y="observations"))
a+geom_point()+coord_cartesian()+theme_classic()+geom_jitter()


#The bar plot shows you that the mean number of observations for each region is about the same
#When you create the scatter plot you see that even though the means are similar, the actual points of observation vary for each region
#While the east and west regions are fairly evenly spread in terms of observations, the north region is clumped together around 15 and the south region is clumped around 5 and 25
#These various sets of observations all return similar means, but the scatterplot gives a more accurate depiction of what is going on for number of observations in each region