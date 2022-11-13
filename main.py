print("_______________________________________________________________________________")
import csv
print("Program to demonstrate csv.reader() function:")
print("\n")
c = open('csv-test.csv','r')
print("The csv file is opened for reading:")
print("\n")

o = csv.reader(c)
print("The contents of the above file is as follows:")
for r in o:
    print (r)
c.close()

import csv

with open('csv-test.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

import numpy as np

arr = (10,20,30)
print("1-D array :", arr)
print("Standard Deviation of arr is ", np.std(arr))

