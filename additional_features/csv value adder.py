import csv
import numpy as np
import pandas as pd
filename = input("enter csv file: ")

file = open(filename)

csv_file = csv.reader(file)

temp_csv = []
new_csv = []

for row in csv_file:
    temp_csv.append(row)

for row in temp_csv[1:]:
    row[1] = str(int(row[1]) + 3)
    #new_csv.append(row)
    

#outfile = np.asarray(new_csv)
outfile = np.asarray(temp_csv)
np.savetxt( (filename[:-4] + "added.csv"), outfile, delimiter=',', fmt = '%s')


