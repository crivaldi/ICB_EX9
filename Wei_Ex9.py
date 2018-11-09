#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 19:07:44 2018

@author: Alicia
"""

#Website with data used: http://tylervigen.com/view_correlation?id=3857
###Note:This was just a fun unexpected correlations website I used. I know it's not realistic 
#Data inserted into Excel file and exported as txt file

import pandas as pd
import matplotlib.pyplot as mpl
import numpy as np
import plotnine

####PROBLEM1
data=pd.read_csv('RandCorr.txt',sep = '\t')
#data #sanity check

x = data.iloc[:,0] #telling python what to rename column one as
y = data.iloc[:,1] #telling python what to rename column two as
z = data.iloc[:,2] #telling python what to rename column three as

#Scatter plotting # of suicides first
fig, ax1 = mpl.subplots()
mpl.plot(x,y,'r.')
mpl.legend(['Suicides'],loc=2)
#Labels
ax1.set_xlabel('Year') 
ax1.set_ylabel('#Suicides', color='r')
#Best fit line
a = np.polyfit(x,y,2)
p1 = np.poly1d(a) 
mpl.plot(x,p1(x),"r--")
#Setting y min
ax1.set_ylim(ymin=5000) #I'm adjusting the min y value so we can REALLY see the "correlation"

#Scatter plotting # of Lawyers
ax2 = ax1.twinx()
mpl.plot(x,z,'b.')
#bestfitline
b = np.polyfit(x,z,1)
p2 = np.poly1d(b)
mpl.plot(x,p2(x),"b--")
#Labels
mpl.legend(['# of Lawyers'],loc=4)
ax2.set_ylabel('# of Lawyers', color = 'b')
#setting y min
ax2.set_ylim(ymin=14000)

#GeneralLabels
mpl.title('Unexpected Correlations')
mpl.xlabel('Year')
         
mpl.figure()    
            
####PROBLEM 2####
data2 = pd.read_csv("data.txt",sep = ',')
#part1#
def mean(cardinal,data):
    data3 = data2[data2["region"] == cardinal]
    return data3

n = mean('north',data2)
nx = n.mean()
#print nx

e = mean('east',data2)
ex = e.mean()
#print ex

s = mean('south',data2)
sx = s.mean()
#print sx

w = mean('west',data2)
wx = w.mean()
#print wx

#Plotting Bar Graph
regions = ['north', 'east','south','west']
pos = np.arange(len(regions))
ymeans = [float(nx), float(ex), float(sx), float(wx)]

mpl.bar(pos,ymeans,color='blue',edgecolor='black')

#Part2
from plotnine import *
p = ggplot(data2, aes('region','observations'))+geom_jitter()
p.draw()