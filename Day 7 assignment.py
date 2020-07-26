# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 11:20:13 2020

@author: priyansh
"""

# import libraries required for this analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import data

dataset1=pd.read_csv('general_data.csv')

print(dataset1.head())

# check null character
dataset1.isnull()

# remove duplicates

dataset1.duplicated()

dataset1.drop_duplicates()

# univariate analysis
dataset3=dataset1[['Age','DistanceFromHome','Education','MonthlyIncome', 'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear', 'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].describe()

print(dataset3)

# find median
dataset3=dataset1[['Age','DistanceFromHome','Education','MonthlyIncome', 'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear', 'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].median()

print(dataset3)

# find mode
dataset3=dataset1[['Age','DistanceFromHome','Education','MonthlyIncome', 'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear', 'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].mode()
print(dataset3)

# find variance
dataset3=dataset1[['Age','DistanceFromHome','Education','MonthlyIncome', 'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear', 'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].var()
print(dataset3)

# find skewness
dataset3=dataset1[['Age','DistanceFromHome','Education','MonthlyIncome', 'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear', 'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].skew()
print(dataset3)

# find Kurtosis 
dataset3=dataset1[['Age','DistanceFromHome','Education','MonthlyIncome', 'NumCompaniesWorked', 'PercentSalaryHike','TotalWorkingYears', 'TrainingTimesLastYear', 'YearsAtCompany','YearsSinceLastPromotion', 'YearsWithCurrManager']].kurt()
print(dataset3)

# Age
box_plot=dataset1.Age
plt.boxplot(box_plot)

# MonthlyIncome
box_plot1=dataset1.MonthlyIncome
plt.boxplot(box_plot1)

# YearsAtCompany
box_plot2=dataset1.YearsAtCompany
plt.boxplot(box_plot2)
