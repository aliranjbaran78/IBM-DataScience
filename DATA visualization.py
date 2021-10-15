# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 20:21:43 2021

@author: Ali
"""

#data frame import
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from pandas import DataFrame,Series
from numpy.random import randn
from matplotlib import rcParams
df1 = pd.read_csv('D:\\Downloads\\rsi.csv')
'''simple plot'''
xx=range(1,10)
y = [1,2,3,4,0,4,3,2,1]
plt.plot(xx,y,color='#7C977C')

'''simple line chart'''
df1.plot()

#Bar Chart
plt.bar(xx, y)

df1.plot(kind = 'bar')
df1.plot(kind = 'barh')#bar horizoiontial

# PIE CHART
yy=[5,3,6,7,6,3]
plt.pie(yy) 
'''saving a plot'''
plt.pie(yy)
plt.savefig('pie_chart.png')
'''find current working directory'''
#%pwd
plt.plot(xxx)