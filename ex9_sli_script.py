import numpy as np
import pandas as pd
from plotnine import *

# Task 1

df = pd.read_table("treedata.txt")

# remove blank cells
df.replace('', np.nan, inplace=True)
df.dropna(inplace=True)

# plot data
ggplot(df, aes(x='DBH',y='Height'))+geom_point()+theme_classic()+ xlim(0,40)+\
stat_smooth(method="lm",color='red')


# Task 2

data = pd.read_table("data.txt",sep=",")

ggplot(data)+theme_classic()+geom_bar(aes(x="factor(region)",y="observations"),stat="summary",fun_y=np.mean)
ggplot(data,aes(x='region',y='observations'))+theme_classic()+geom_point()+geom_jitter()
