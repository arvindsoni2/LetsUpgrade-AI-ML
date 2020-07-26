# import modules
import pandas as pd


from scipy.stats.stats import pearsonr

dataset=pd.read_csv('general_data.csv')

dataset['TotalWorkingYears']=dataset['TotalWorkingYears'].fillna(11.28)
print(dataset.columns)


stats,p=pearsonr(dataset.Attrition, dataset.DistanceFromHome)
print(stats, p)


stats, p=pearsonr(dataset.Attrition, dataset.MonthlyIncome)

print(stats, p)

stats, p=pearsonr(dataset.Attrition, dataset.TotalWorkingYears)
print(stats, p)

stats, p=pearsonr(dataset.Attrition, dataset.YearsAtCompany)
print(stats, p)

stats, p=pearsonr(dataset.Attrition, dataset.YearsWithCurrManager)
print(stats, p)