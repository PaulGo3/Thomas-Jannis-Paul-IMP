print("_______________________________________________________________________________")
import csv
print("Program to demonstrate csv.writer() function")
print("\n")
p_details =[('course','fees','place'),('Python',22000,'Pune'),('Android',11000,'Assam'),('Java',30000,'Delhi')]
c = open('csv-test.csv','w')
print("File is opened for writing:")
o = csv.writer(c)
for p in p_details:
    o.writerow(p)
c.close()

import numpy as np

arr = [10, 20, 30]
print("1-D array :", arr)
print("Standard Deviation of arr is ", np.std(arr))

