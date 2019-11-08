# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:29:13 2019

@author: es534
"""
import numpy as np
import pandas as pd
seed=pd.read_excel('Input_RAS.xlsx', 'seed', na_values=['NA'], skipfooter=None, index_col=0, parse_cols='A:FM', skiprows=None, header=0)
goal=pd.read_excel('Input_RAS.xlsx', 'goal', na_values=['NA'], skipfooter=None, index_col=0, parse_cols='A:FN', skiprows=None, header=0)
ras(seed, goal)