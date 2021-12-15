import struct
import sys
from scipy.io import wavfile
from scipy.signal import resample
import wave
import csv
import numpy as np
import pandas as pd
#import librosa
import soundfile as sf
import time
import math
import itertools
import seaborn as sns
import matplotlib.pyplot as plt
import sys, os, os.path
import numpy 
from pydub import AudioSegment
from pydub.playback import play
import pyaudio
import numpy as np
import threading
import base64 
#from flask import Flask, render_template, request, make_response
from scipy.io import wavfile
#from thm import freq
from io import StringIO, BytesIO

#functions:
#wav_to_array(file)
#wav_to_csv(filename)
#frequency_modulator(file, shift)
#roboticize(input_filename)



    
#helper function for wav_to_csv
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


#this function accepts a wav file and exports a 2d array containing all sampling points to recreate the audio file
def wav_to_array(input_filename):
    if input_filename[-3:] != 'wav':
        print('WARNING!! Input File format should be *.wav')
        sys.exit()

    samrate, data = wavfile.read(str(input_filename))
    wavData = pd.DataFrame(data)
    arr = wavData.to_numpy()
    arr = np.transpose(arr)

    #if len(wavData.columns) == 2:
        #wavData.columns = ['R', 'L']
        #stereo_R = pd.DataFrame(wavData['R'])
        #stereo_L = pd.DataFrame(wavData['L'])

    #if (len(wavData.columns) == 1):
        #wavData.columns = ['M']

    #return(wavData)
    return(arr)


#this function accepts a wav file and saves a csv file containing all sampling points to recreate the audio file to the same location as the caller
def wav_to_csv(input_filename):
    if input_filename[-3:] != 'wav':
        print('WARNING!! Input File format should be *.wav')
        sys.exit()

    samrate, data = wavfile.read(str(input_filename))
    #print('Load is Done! \n')

    wavData = pd.DataFrame(data)

    if len(wavData.columns) == 2:
        #print('Stereo .wav file\n')
        wavData.columns = ['R', 'L']
        stereo_R = pd.DataFrame(wavData['R'])
        stereo_L = pd.DataFrame(wavData['L'])
        #print('Saving...\n')
        stereo_R.to_csv(str(input_filename[:-4] + "_Output_stereo_R.csv"), mode='w')
        stereo_L.to_csv(str(input_filename[:-4] + "_Output_stereo_L.csv"), mode='w')
        wavData.to_csv("Output_stereo_RL.csv", mode='w')
        #print('Save is done ' + str(input_filename[:-4]) + '_Output_stereo_R.csv , '+ str(input_filename[:-4]) + '_Output_stereo_L.csv')

    elif len(wavData.columns) == 1:
        #print('Mono .wav file\n')
        wavData.columns = ['M']
        wavData.to_csv(str(input_filename[:-4] + ".csv"), mode='w')
        #print('Save is done ' + str(input_filename[:-4]) + '_Output_mono.csv')

    else:
        #print('Multi channel .wav file\n')
        #print('number of channel : ' + len(wavData.columns) + '\n')
        wavData.to_csv(str(input_filename[:-4] + ".csv"), mode='w')
        #print('Save is done ' + str(input_filename[:-4]) + '.csv')



#this function changes the frequency and pitch of a given wav file
#argunents: string: the 64bit string to be converted into a wav file to process. shift: how much the frequency should change (Positive: shift up. negative: shift down)
#output: python dictionary containing the shifted audio file in both csv and string base64 format
def frequency_modulator(filename, shift):
    #bytes_wav = bytes()
    #byte_io = BytesIO(bytes_wav)
    #wav_file.write(decode_string)
    #wavfile.write(byte_io, frequency, arr)
    #wav_file.close()
    #wav_bytes = byte_io.read()
    CHANNELS = 1
    swidth = 2
    spf = wave.open(filename, 'rb')
    #spf = wave.open("temp.wav", 'rb')
    #spf = wave.open(file)
    RATE=spf.getframerate()
    signal = spf.readframes(-1)
    #wf = wave.open(("changed "+ filename), 'wb')
    wf = wave.open('new.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(swidth)
    if (shift > 0):
        wf.setframerate(RATE*shift)
    if (shift < 0):
        shift = abs(shift)
        wf.setframerate(RATE/shift)
    wf.writeframes(signal)
    wf.close()
    #wav_string = base64.b64encode(open("changed "+ filename).read())
    wav_string = base64.b64encode(open('new.wav', 'rb').read() )
    array = wav_to_array('new.wav')

    dictionary = {
        "string": wav_string,
        "array": array
    }

    return(dictionary)


    
#this function creates a robot-like effect on audio files by overlaying several of the same file with slight offsets
#arguments: input_filename: name of wav file to apply effect. level: the amount of overlays
#output: python dctionairy containing the changed audio file in both csv and string base64 format
def roboticize_string(input_filename, level):
    while(input_filename[-4:] != ".wav"):
            file = input("file name must end in '.wav' ")

    audio = AudioSegment.from_file(input_filename)

    for i in range (level):
        audio = audio.overlay(audio, position = 5)        

    audio.export("robot_" + input_filename, format='wav') #export mixed  audio file

    wav_string = base64.b64encode(open("robot_" + input_filename).read())
    array = wav_to_array("robot_" + input_filename)

    dictionary = {
        "string": wav_string,
        "array": array
    }

    return(dictionary)



#array = wav_to_array("taunt.wav")
#spf = wave.open("taunt.wav", 'rb')
#RATE=spf.getframerate()
#frequency_modulator(array, RATE, 2)
#CHANNELS = 1
#swidth = 2
#spf = wave.open("taunt.wav")
#RATE=spf.getframerate()
#signal = spf.readframes(-1)
#freq = RATE*2
#wavfile.write('x.wav', freq, signal)

        


        
