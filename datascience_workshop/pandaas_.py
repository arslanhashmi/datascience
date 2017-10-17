
import pandas as pd
import numpy as np
#data = pd.read_table('data/chipotle.tsv')
#print (file)
#print (data.head(3))

#print (data.describe())
#list = ['pehla','dosra','tesra','chotha','panchnwan']

#data = pd.read_table('data/movieusers.tsv')

#print (data.head())


#data = pd.read_csv('data/imdb_1000.csv')
#print ((data.describe()))

#print (np.mean(pd.read_csv('data/imdb_1000.csv').star_rating))
#print (np.sum(pd.read_csv('data/imdb_1000.csv').star_rating)/len(data))

drink = pd.read_csv('data/drinks.csv')
drink.drop(0)
print (drink.head())
print (drink.info())



