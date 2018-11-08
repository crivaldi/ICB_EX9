# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 17:38:32 2018

@author: vysan
"""

import numpy
import pandas
from plotnine import *
surv=pandas.read_csv("survival.txt",sep="\t",header=0)
surv

a=ggplot(surv,aes(x="dose",y="surv"))
a+geom_point()+coord_cartesian()+theme_classic()+xlab("dose of radiation (rad)")+ylab("survival rate")+stat_smooth()
