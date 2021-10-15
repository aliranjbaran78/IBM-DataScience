# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 18:57:09 2021

@author: Ali
"""

import numpy as np
import pandas as pd

from pandas import Series, DataFrame
#selecting n creating data frames

series_obj = Series(np.arange(8), 
                    index=['row 1','row 2','row 3','row 4',
                           'row 5','row 6','row 7','row 8'])
print(series_obj)

np.random.seed(17)
df=DataFrame(np.random.rand(36).reshape(6,6),
             index=['row 1','row 2','row 3','row 4',
                           'row 5','row 6'],
            columns=['col 1','col 2','col 3','col 4','col 5','col 6'])

#data slicing

df.loc[['row 2','row 5'],['col 5','col 2']]
df['row 3':'row 7']

#Filtering with scalars

print(df >.2)
df[df>6]

#Setting value by scalars

series_obj['row 1','row 2','row 5']=[.2,.5,.6]

#Missing values 
missing =np.nan
seri=Series(['row 1','row 2','row 3',missing,'row 5','row 6',missing,'row 8'])


seri.isnull()
np.random.seed(25)
df_obj =DataFrame(np.random.rand(36).reshape(6,6))
df_obj.loc[3:5,0]=missing
df_obj.loc[1:4,5]=missing
print(df_obj)
'''filling missing value by average'''
filled=df_obj.fillna(df_obj.mean(skipna=True))
print(filled)
''' Filling missing values by zero n giving num'''
filled1=df_obj.fillna(0)
filled2=df_obj.fillna({0: 0.1, 5:1.25})
'''Flling by giving last known num'''
filled3=df_obj.fillna(method='ffill')
'''count num of na'''
df_obj.isnull().sum()
'''omitiing nans'''
df_non_na = df_obj.dropna(axis=1)

#DELETE Duplicate items
dff =DataFrame({'col 1':[1,2,2,2,3,3,3],
                'col 2':['a','a','b','b','b','c','c'],
                'col 3':['A','A','B','B','B','C','C']})
'''show duplicated rows'''
dff.duplicated()
'''REMOVE duplicated'''
dff.drop_duplicates()
'''REMOVE ANY DUPLICATE WHICH IS IN COL 3'''
dff.drop_duplicates(['col 3'])
dff.drop(['col 1','col 2'], axis=1 ) #drop by col index


'''CONCATNATING DATAFRAMES'''
df010=DataFrame(np.arange(49).reshape(7,7))
df0100=pd.DataFrame(np.arange(15).reshape(5,3))
dfjoint=pd.concat([df010,df0100],axis=1) #add by col

'''ADD data'''
seris=Series(np.arange(6))
seris.name='add_variable'
jointdf=DataFrame.join(df0100,seris)

add_df=jointdf.append(jointdf,ignore_index = True)

'''Data Sorting'''
dfsort=add_df.sort_values(by=(1),ascending =[False])