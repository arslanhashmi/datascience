
import numpy as np

file_name = "FL_insurance_sample.csv"
#data = np.loadtxt(file_name,delimiter=",",skiprows=1)
#data = np.loadtxt(file_name,delimiter=",",usecols=[0,2]) # few rows
data = np.loadtxt(file_name,delimiter=",",dtype=str) # few rows
data1 = np.genfromtxt(file_name, delimiter=',', names=True, dtype=None)
print( data )
print( "data1", data1 )

