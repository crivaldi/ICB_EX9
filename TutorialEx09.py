# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 22:37:17 2018

@author: Alicia
"""

#Question 2

import numpy
import pandas
from plotnine import *

data=pandas.read_csv("data.txt",sep=",",header=0)
data.head(5)
df=ggplot(data)+theme_classic()+xlab("region")+ylab("observations")
df+geom_bar(aes(x="factor(region)",y="observations"),stat="summary",fun_y=numpy.mean)
#To check barplot mean values are correct
data.groupby(['region'])['observations'].mean()

a=ggplot(data,aes(x="region",y="observations"))
a+geom_point()+coord_cartesian()+theme_bw()
geom_jitter()


