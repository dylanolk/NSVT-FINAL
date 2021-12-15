import struct
import sys
import csv
import numpy 
from scipy.io import wavfile
from scipy.signal import resample
import wave

input_filename = input("enter csv file: ")
data = []
fname = input_filename[:-4] + ".csv"
for time, value in csv.reader(open(fname, 'U'), delimiter=','):
    try:
        data.append(float(value))#Here you can see that the time column is skipped
    except ValueError:
        pass # Just skip it


arr = numpy.array(data)#Just organize all your samples into an array
# Normalize data
arr /= numpy.max(numpy.abs(data)) #Divide all your samples by the max sample value
filename_head, extension = fname.rsplit(".", 1)        
data_resampled = resample( arr, len(data) )
wavfile.write(fname[:-4]+"2.wav", samrate, data_resampled)
print ("File written succesfully !")

