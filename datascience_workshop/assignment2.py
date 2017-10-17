
import pandas as pd
import numpy as np


local = pd.read_csv('data/data_local_billing.csv',sep=',')

churn_target = pd.read_csv('data/data_churn_target.csv',sep=',')

international_billings = pd.read_csv('data/data_international_billing.csv',sep=',')

headers = churn_target.merge(international_billings,left_on='Phone', right_on='Phone', how='inner')
total_data = local.merge(headers,left_on='Phone', right_on='Phone', how='outer')

#print (total_data.columns.tolist())

#print ('Total data ', total_data.shape)
#print ('Null checking...', total_data.isnull().values.any(), 'means data has null values')
#print ('Data types of the columms')
#print ('types...\n', total_data.dtypes)
#print (total_data.describe())
total_data.fillna(0,inplace=True)
#print (total_data.isnull().values.any())
total_data = total_data.drop(['State','Area Code','Phone'],axis=1)
#print (total_data.shape)
features = total_data.drop(['Churn?'],axis=1).columns
#print (features)
yes_no_cols = ["Int'l Plan","VMail Plan"]
total_data[yes_no_cols] = total_data[yes_no_cols] == 'yes'
total_data['Churn?'] = total_data['Churn?'] == 'True'
#total_data["Churn?"].replace(("False.","True."),(0,1),inplace=True) # no need now it is already dono above.
print (total_data.head())
