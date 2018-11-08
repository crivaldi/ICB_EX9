# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 23:14:07 2018

@author: vysan
"""

import numpy
import pandas
from plotnine import *
data=pandas.read_csv("data.txt",sep=",",header=0)

#barplot of means
a=ggplot(data)+theme_classic()+xlab("region")+ylab("observations")
a+geom_bar(aes(x="factor(region)",y="observations"),stat="summary",fun_y=numpy.mean)
#check barplot means
data.groupby(["region"])["observations"].mean()

#scatter plot of all observations 
b=ggplot(data,aes(x="factor(region)",y="observations"))
b+geom_point()+coord_cartesian()+theme_classic()+xlab("region")+ylab("observations")+geom_jitter()
b+geom_jitter()+coord_cartesian()+theme_classic()+xlab("region")+ylab("observations")

#the bar and scatter plot tell different stories
#the barplot shows the mean of observations for each region
#but the scatterplot shows us the actual distribution of individual points of observations across regions