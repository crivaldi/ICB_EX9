# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 20:18:57 2018

@author: Seth
"""

import pandas as pd
import numpy as np
from plotnine import *
data = pd.read_csv('data.txt', header = 0, sep = ",")
#scatterplot of region and observations
b = ggplot(data, aes(x = "region", y = "observations"))
b + geom_point() + coord_cartesian() + geom_jitter()
#histogram of region and observations
c = ggplot(data, aes(x = "region"))
c + geom_histogram() + theme_classic()
#The mean of observations in all 4 regions is similar. However, the scatterplot shows different
#variation between the regions. Error bars in the histogram would reflect variation.