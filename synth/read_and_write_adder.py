# -*- coding: utf-8 -*-
"""
BMCL BAEKSUWHAN
@author: lukious
"""

import sys, os, os.path
from scipy.io import wavfile
import pandas as pd


def write_wav(data, filename, framerate, amplitude):
    wavfile = wave.open(filename,'w')
    nchannels = 1
    sampwidth = 2
    framerate = framerate
    nframes = len(data)
    comptype = "NONE"
    compname = "not compressed"
    wavfile.setparams((nchannels,
                        sampwidth,
                        framerate,
                        nframes,
                        comptype,
                        compname))
    frames = []
    for s in data:
        mul = int(s * amplitude)
        frames.append(struct.pack('h', mul))

    frames = ''.join(frames)
    wavfile.writeframes(frames)
    wavfile.close()
    print("%s written" %(filename)) 

input_filename = input("Input file number:")
if input_filename[-3:] != 'wav':
    print('WARNING!! Input File format should be *.wav')
    sys.exit()

samrate, data = wavfile.read(str(input_filename))
print('Load is Done! \n')

wavData = pd.DataFrame(data)

if len(wavData.columns) == 2:
    print('Stereo .wav file\n')
    wavData.columns = ['R', 'L']
    stereo_R = pd.DataFrame(wavData['R'])
    stereo_L = pd.DataFrame(wavData['L'])
    print('Saving...\n')
    stereo_R.to_csv(str(input_filename[:-4] + "_Output_stereo_R.csv"), mode='w')
    stereo_L.to_csv(str(input_filename[:-4] + "_Output_stereo_L.csv"), mode='w')
    # wavData.to_csv("Output_stereo_RL.csv", mode='w')
    print('Save is done ' + str(input_filename[:-4]) + '_Output_stereo_R.csv , '
                          + str(input_filename[:-4]) + '_Output_stereo_L.csv')

elif len(wavData.columns) == 1:
    print('Mono .wav file\n')
    wavData.columns = ['M']

    wavData.to_csv(str(input_filename[:-4] + ".csv"), mode='w')

    print('Save is done ' + str(input_filename[:-4]) + '_Output_mono.csv')

else:
    print('Multi channel .wav file\n')
    print('number of channel : ' + len(wavData.columns) + '\n')
    wavData.to_csv(str(input_filename[:-4] + ".csv"), mode='w')

    print('Save is done ' + str(input_filename[:-4]) + '.csv')

import struct
import sys
import csv
import numpy 
from scipy.io import wavfile
from scipy.signal import resample
import wave


data = []
fname = input_filename[:-4] + ".csv"
for time, value in csv.reader(open(fname, 'U'), delimiter=','):
    try:
        data.append(float(value)+ 100.0)#Here you can see that the time column is skipped
    except ValueError:
        pass # Just skip it


arr = numpy.array(data)#Just organize all your samples into an array
# Normalize data
arr /= numpy.max(numpy.abs(data)) #Divide all your samples by the max sample value
filename_head, extension = fname.rsplit(".", 1)        
data_resampled = resample( arr, len(data) )
wavfile.write(fname[:-4]+"added.wav", samrate, data_resampled)
print ("File written succesfully !")
