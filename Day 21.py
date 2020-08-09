# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 12:00:28 2020

@author: priyansh
"""

# Bank loan logistic regression 

import pandas as pd
import statsmodels.api as st
dset1 = pd.read_excel('C:/Users/priyansh/Downloads/Letsupgrade/Day 21/Bank_Personal_Loan_Modelling.xlsx', 1)

# Remove column 'ID' & 'Zip Code'

dset1 = dset1.drop(['ID'],axis = 1)
dset1 = dset1.drop(['ZIP Code'], axis = 1)

# perform logistic regression

Y = dset1['Personal Loan']
X = dset1[['Age','Experience','Income','Family','CCAvg','Education','Mortgage','Securities Account','CD Account','Online','CreditCard']]

X1 = st.add_constant(X)

log1 = st.Logit(Y,X1)

result = log1.fit()

print (result.summary())


