# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 15:29:59 2021

@author: Amulya
"""

import numpy as np, pandas as pd
from sklearn import tree,metrics,model_selection,preprocessing

df=pd.read_csv('kyphosis.csv')
df

y=df['Kyphosis']
X=df[['Age','Number','Start']]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

from sklearn import tree
dtree=tree.DecisionTreeClassifier(criterion='entropy',max_depth=3,random_state=0)
dtree.fit(X_train,y_train)

pred=dtree.predict([[71,3,5]])
pred