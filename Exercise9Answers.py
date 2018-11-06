#Answer to number 1
import pandas as pd
import numpy as np
from plotnine import *
cd ../
cd Desktop
pwd
wages=pd.read_csv("wages.csv")
a=ggplot(wages,aes(x="yearsSchool",y="wage"))
a+geom_point()+coord_cartesian()
a=ggplot(wages,aes(x="yearsSchool",y="wage"))+theme_classic()+geom_point()
a+xlab("Years of School")+ylab("Wage")+stat_smooth(method="lm")


#Anser to number 2 after converting data.txt into a csv manually
cd ../ICB_EX9
data=pd.read_csv("data.csv")
data.shape
! pip install scikit-misc
#Barplot of means of data
d=ggplot(data)+theme_classic()+xlab("Region")+ylab("Observations")
d+geom_bar(aes(x="region",y="observations"),stat="summary",fun_y=np.mean)
#Scatterplot of data
e=ggplot(data)+theme_classic()+coord_cartesian()+xlab("Region")+ylab("Observations")
e+geom_jitter(aes(x="region",y="observations"))
#Barplot and scatter tell similar stories since they show the general distribution and relationship of regions and observations.  
