
# data will be two dimensional matrix ( could be numpy array or a dataframe) data and features are in the data, and sample is what we have
# for practise, similarly it could be structured and unstructured, cleansing is important.

from sklearn.datasets import load_iris
import numpy as np
import pandas as pd
#import mglearn
#import premeble

iris = load_iris()
#print(type(iris))
#print(iris.keys()) #data:target:target_names:DESCR:feature_names:
#print (iris['DESCR'])
#print(iris.data[0])
#print(iris.data.shape)
#print(iris.target.shape) #important
#print(iris.target) #target is basically the classes or the labels
#print(np.bincount(iris.target))


