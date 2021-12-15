#!/usr/bin/env python
# coding: utf-8

# In[1]:


#
# A basic program that reads a WAV file displays its frequency waveform, and exports a CSV 
#   file of all of its points and a CSV file of its maximum frequency
# Contributor: Seth Spiegel


import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.io import wavfile

# WAV file reader and displayer 
# edited from code by Eugene Klyshko, https://klyshko.github.io/teaching/2019-02-22-teaching
plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.figsize'] = (9, 7)

sampFreq, sound = wavfile.read('taunt.wav')

sound.dtype, sampFreq

#(dtype('int16'), 44100)

sound = sound / 2.0**15

sound.shape

(45568, 2)

length_in_s = sound.shape[0] / sampFreq
print(length_in_s)

plt.subplot(2,1,1)
plt.plot(sound[:,0], 'r')

#plt.xlabel("left channel, sample #")
#plt.subplot(2,1,2)
#plt.plot(sound[:,1], 'b')
#plt.xlabel("right channel, sample #")
#plt.tight_layout()

#extract points from the plot. credit https://stackoverflow.com/questions/9850845/how-to-extract-points-from-a-graph

#empty string to store points
points = []
graph = plt.plot(sound[:,0], 'r')
xvalues = graph[0].get_xdata()
yvalues = graph[0].get_ydata()
xyValues = graph[0].get_xydata()
#print("xvalues: ", xvalues)

#export x and y data as csv files for C++ program?
xExport = np.asarray(xvalues)
yExport = np.asarray(yvalues)
xyExport = np.asarray(xyValues)
np.savetxt("x_values", xExport, delimiter=",")
np.savetxt("y_values", yExport, delimiter=",")
np.savetxt("xy_values", xyExport, delimiter=",")
plt.show()

#time = np.arange(sound.shape[0]) / sound.shape[0] * length_in_s


#plt.plot(time[6000:7000], signal[6000:7000])
#plt.xlabel("time, s")
#plt.ylabel("Signal, relative units")
#plt.show()



# In[ ]:





# In[ ]:




