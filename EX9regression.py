# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 19:43:02 2018

@author: Seth
"""

import pandas as pd
import numpy as np
mortgage = pd.read_csv('sample_mortgage_data.txt', header = 0, sep = '\t')
from plotnine import *
#scatterplot of median home price and mortgage interest rates, adds trendline
a = ggplot(mortgage, aes(x = "Median home price", y = "interest rate (%)"))
a + geom_point() + coord_cartesian() + stat_smooth(method = "lm")