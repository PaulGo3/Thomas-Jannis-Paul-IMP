y = (100,98,101,93,94,91,90,90,97,93,93,95,93,91,89,89,88,89,90,91,94,93,94,96,92,93,93,92,91,90,90,89,91,95,97,93,92,95,98,93,91,96,98,95,93,96,93,93,95,92,90,88,87,91,89,90,88,87,89,86,86,89,92,90,92,93,91,89,87,86,88,87,90,93,92,90,89,91,93,90,92,94)

print("_______________________________________________________________________________")

import csv

with open('csv-test.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
print(data)

import numpy as np

arr = (10,20,30)
print("1-D array :", arr)
print("Standartabweichung ist: ", np.std(y))


