import pandas as pd

file_name = "FL_insurance_sample.csv"
data = pd.read_csv(file_name,index_col=0) #if there is no header write header=None and can assign column names like names=[...] na_values='-1"
print (data.head())
print ('1----')
print (data)
print ('2----')
print (data.point_granularity.value_counts(dropna=False))
print ('3----')
print (data.construction.value_counts(dropna=False))
print ('4----')
print (data.construction.value_counts(dropna=False).head()) #to return top 5 counts or head(2) to see only first two similarly tail()
print ('5----')
print (data.values)
print ('6----')
print (data[data.point_granularity > 3])
print ('7----')
print (data.describe()) # just fun
print ('8----')
data.point_granularity.plot('hist')
data.boxplot(column='point_granularity',by='county')
import matplotlib.pyplot as plt
plt.show()