import pandas as pd

data = {
    'weekdays':['sun','mun','tue','wed'],
    'cities':['lhr','krc','rwl','isl'],
    'visitors':[10,20,23,32]
}
users = pd.DataFrame(data)
print (users)

# or do it like this with zip

weekdays = ['sun','mun','tue','wed']
cities=['lhr','krc','rwl','isl']
visitors=[10,20,23,32]
labels=['weekdays','cities','visitors']
list_cols = [weekdays, cities, visitors]
zipped = list(zip(labels,list_cols))

#print (zipped)

data = dict(zipped)
users = pd.DataFrame(data)
users['fees'] = 0  #broadcasting a scalar value
print (users)


users.to_csv("data.csv")  #sep='\t'
#users.to_excel("data.xlsx") #for excel