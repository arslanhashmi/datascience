import csv

string='MainThread run_blocking_tasks: waiting for executor tasks.'
print (len(string.split(' ')))
string1="sdDSs"
print (string1.lower())

from numpy import genfromtxt
my_data = genfromtxt('dataSets/names.csv', dtype=None, delimiter=',', names=True)
print (my_data)