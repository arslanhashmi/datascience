import numpy as np


np_height = np.array([1.73, 1.68, 1.71])
np_weight = np.array([65.4 , 59.2, 63.6])

bmi = np_weight / np_height ** 2

print ( bmi )

bool_check = bmi > 21

print ( bool_check )

element = bmi[ bmi > 21 ] # very important it selects the true values from the array

print ( element )

# 2D numpy arrays

np_2d = np.array([[1.73, 1.68, 1.71],[65.4 , 59.2, 63.6]])

print ( np_2d )
print ("----")
print ( np_2d[:,1:3] )
print ( np_2d.shape )
print (np_2d[:,0])
mean_height = np.mean(np_2d[:,0])
median_height = np.median(np_2d[:,0])
corelated_fun = np.corrcoef (np_2d[:,0], np_2d[:,1])
std = np.std(np_2d[0:1])
print (std)
print (mean_height)
print (median_height)
print (corelated_fun)

height = np.round(np.random.normal(1.75,0.20,5000),2)
weight = np.round(np.random.normal(60.30,15,5000),2)

np_city = np.column_stack((height,weight))

print ( np_city )