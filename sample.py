# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np, pandas as pd
from sklearn import tree,metrics,model_selection,preprocessing

df=pd.read.csv('kyphosis.csv')
df