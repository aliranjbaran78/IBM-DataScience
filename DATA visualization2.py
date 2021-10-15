# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 14:29:06 2021

@author: Ali
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from pandas import DataFrame,Series
from numpy.random import randn
from matplotlib import rcParams

pdf= pd.read_csv('D:\Downloads\population.csv')

plt.bar(pdf['iso_code'], pdf['growth_rate'])