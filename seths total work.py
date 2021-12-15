#all of the semesters work
#author: Seth Spiegel
#note: this is simply the aggregation of all the code done for all of the functions located in one place for ease of viewing. While individually these functions work, this code is not fully functional as many of the functions will interfere with each other when placed together like this.
import matplotlib.pyplot as plt
import numpy as np
import numpy
import os
from scipy.io import wavfile
import struct
import sys
from scipy.signal import resample
import wave
import csv
import numpy as np
import pandas as pd
import librosa
import soundfile as sf
import time
import math
import itertools
import seaborn as sns
import matplotlib.pyplot as plt
import sys, os, os.path
from pydub import AudioSegment
from pydub.playback import play
import pyaudio
import threading
import base64
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

def basicFrequencyPlotter(filename):
    # WAV file reader and displayer 
    # edited from code by Eugene Klyshko, https://klyshko.github.io/teaching/2019-02-22-teaching
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['figure.figsize'] = (9, 7)
    sampFreq, sound = wavfile.read('taunt.wav')
    sound.dtype, sampFreq
    #(dtype('int16'), 44100)
    sound = sound / 2.0**15
    sound.shape(45568, 2)
    length_in_s = sound.shape[0] / sampFreq
    print(length_in_s)
    plt.subplot(2,1,1)
    plt.plot(sound[:,0], 'r')
    plt.xlabel("left channel, sample #")
    plt.subplot(2,1,2)
    plt.plot(sound[:,1], 'b')
    plt.xlabel("right channel, sample #")
    plt.tight_layout()

    #extract points from the plot. 
    #edited from https://stackoverflow.com/questions/9850845/how-to-extract-points-from-a-graph
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
    
    time = np.arange(sound.shape[0]) / sound.shape[0] * length_in_s
    
    plt.plot(time[6000:7000], signal[6000:7000])
    plt.xlabel("time, s")
    plt.ylabel("Signal, relative units")
    plt.show()
    
    #In[ ]:
    #In[ ]:


#sine Oscialltor Collection
# Function that processes values.
def some_function(value):
    time.sleep(1)
    return value * 2
# A generator expression
processed_values_gen = (some_function(i) for i in range(30))
next(processed_values_gen)
def generator_function():
    for i in range(30):
        yield some_function(i)
processed_values_gen = generator_function()
next(processed_values_gen)
sns.set_theme()
SR = 44_100 # Sample rate
figsize=(25, 6.25)
colors = "#323031", "#308E91", "#34369D","#5E2A7E", "#5E2A7E", "#6F3384"
def plot(xy, r=1,c=1,i=1,title="", xlabel="",ylabel="",yticks=None, xticks=None,**plot_kwargs):
    plt.subplot(r,c,i)
    plt.title(title)
    if len(xy) == 2:
        plt.plot(*xy, **plot_kwargs)
    else:
        plt.plot(xy, **plot_kwargs)
    if xticks is not None: plt.xticks(xticks)
    if yticks is not None: plt.yticks(yticks)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
def get_sin_oscillator(freq=1, sample_rate=512):
    increment = (2 * math.pi * freq)/ sample_rate
    return (math.sin(v) for v in itertools.count(start=0, step=increment))
def get_n(iterator, n):
    return [next(iterator)for i in range(n)]
# List comprehension to generate 512 samples.
fig = plt.figure(figsize=(8*2,4*2))
hz = 1
osc = get_sin_oscillator(freq=hz, sample_rate=512); 
wave = get_n(osc, 512)
plot(wave, label=f"{hz} Hz Sine Wave", xlabel="samples", ylabel="amplitude", color=colors[0])
plt.legend(loc='lower right')
plt.show()
fig.savefig("sine.jpg")
def get_sin_oscillator(freq=1, sample_rate=512, amp=1, phase=0):
    phase = (phase / 360) * 2 * math.pi
    increment = (2 * math.pi * freq)/ sample_rate
    return (math.sin(phase + v)*amp for v in itertools.count(start=0, step=increment))
# List comprehension to generate 512 samples.
fig = plt.figure(figsize=figsize)
plt.title("Different Frequencies")
for hz,c in zip([1,2,3,4],colors):
    osc = get_sin_oscillator(freq=hz, sample_rate=SR); 
    wave = get_n(osc, SR)
    plt.plot(wave, label=f"{hz} Hz", color=c)
plt.ylabel("amp")
plt.xlabel("samples")
plt.legend(loc='lower right')
plt.show()
fig.savefig("sine_freq.jpg")
# List comprehension to generate 512 samples.
fig = plt.figure(figsize=figsize)
plt.title("Different Amplitudes")
for amp,c in zip([1,0.75,0.5,0.25], colors):
    osc = get_sin_oscillator(freq=2, sample_rate=SR, amp=amp); 
    wave = get_n(osc, SR)
    plt.plot(wave, label=f"{amp}", color=c)
plt.ylabel("amp")
plt.xlabel("samples")
plt.legend(loc='lower right')
plt.show()
fig.savefig("sine_amp.jpg")
# List comprehension to generate 512 samples.
fig = plt.figure(figsize=figsize)
plt.title("Different Phases")
for phase,c in zip([0, 45, 90, 135],colors):
    osc = get_sin_oscillator(freq=2, sample_rate=SR, phase=phase); 
    wave = get_n(osc, SR)
    plt.plot(wave, label=f"{phase}°", color=c)
plt.ylabel("amp")
plt.xlabel("samples")
plt.legend(loc='lower right')
plt.show()
fig.savefig("sine_phase.jpg")

class Oscillator(ABC):
    def __init__(self, freq=440, phase=0, amp=1, \
                 sample_rate=44_100, wave_range=(-1, 1)):
        self._freq = freq
        self._amp = amp
        self._phase = phase
        self._sample_rate = sample_rate
        self._wave_range = wave_range
        
        # Properties that will be changed
        self._f = freq
        self._a = amp
        self._p = phase
    @property
    def init_freq(self):
        return self._freq
    @property
    def init_amp(self):
        return self._amp
    @property
    def init_phase(self):
        return self._phase
    @property
    def freq(self):
        return self._f
    @freq.setter
    def freq(self, value):
        self._f = value
        self._post_freq_set()
    @property
    def amp(self):
        return self._a
    @amp.setter
    def amp(self, value):
        self._a = value
        self._post_amp_set()
    @property
    def phase(self):
        return self._p
    @phase.setter
    def phase(self, value):
        self._p = value
        self._post_phase_set()
    def _post_freq_set(self):
        pass
    def _post_amp_set(self):
        pass
    def _post_phase_set(self):
        pass
    @abstractmethod
    def _initialize_osc(self):
        pass
    @staticmethod
    def squish_val(val, min_val=0, max_val=1):
        return (((val + 1) / 2 ) * (max_val - min_val)) + min_val
    @abstractmethod
    def __next__(self):
        return None
    def __iter__(self):
        self.freq = self._freq
        self.phase = self._phase
        self.amp = self._amp
        self._initialize_osc()
        return self

def get_val(osc, sample_rate=SR):
    return [next(osc) for i in range(sample_rate)]
def plot_osc(Osc, name=""):
    fig = plt.figure(figsize=figsize)
    f = 8
    plt.title(f"{f}Hz {name} Wave")
    for a,p,c in zip([1.0,0.9,0.8,0.7],[0,15,30,45],colors):
        osc = Osc(freq=f,amp=a,phase=p); iter(osc)
        plt.plot(get_val(osc), color=c, label=f"amp:{a}, phase:{p:02}°")
    plt.legend(loc='lower right')
    fig.savefig(f"{name.lower()}_all.jpg")
def get_seq(osc, notes=["C4", "E4", "G4"], note_lens=[0.5,0.5,0.5]):
    samples = []
    osc = iter(osc)
    for note, note_len in zip(notes, note_lens):
        osc.freq = librosa.note_to_hz(note)
        for _ in range(int(SR * note_len)):
            samples.append(next(osc))
    return samples
to_16 = lambda wav, amp: np.int16(wav * amp * (2**15 - 1))
def wave_to_file(wav, wav2=None, fname="temp.wav", amp=0.1):
    wav = np.array(wav)
    wav = to_16(wav, amp)
    if wav2 is not None:
        wav2 = np.array(wav2)
        wav2 = to_16(wav2, amp)
        wav = np.stack([wav, wav2]).T
    wavfile.write(fname, SR, wav)
class SineOscillator(Oscillator):
    def _post_freq_set(self):
        self._step = (2 * math.pi * self._f) / self._sample_rate
    def _post_phase_set(self):
        self._p = (self._p / 360) * 2 * math.pi
    def _initialize_osc(self):
        self._i = 0
    def __next__(self):
        val = math.sin(self._i + self._p)
        self._i = self._i + self._step
        if self._wave_range != (-1, 1):
            val = self.squish_val(val, *self._wave_range)
        return val * self._a
plot_osc(SineOscillator, "Sine")
osc = SineOscillator()
wav = get_seq(osc)
wave_to_file(wav, fname="c4_maj_sine.wav")
class SquareOscillator(SineOscillator):
    def __init__(self, freq=440, phase=0, amp=1, \
                 sample_rate=44_100, wave_range=(-1, 1), threshold=0):
        super().__init__(freq, phase, amp, sample_rate, wave_range)
        self.threshold = threshold
    def __next__(self):
        val = math.sin(self._i + self._p)
        self._i = self._i + self._step
        if val < self.threshold:
            val = self._wave_range[0]
        else:
            val = self._wave_range[1]
        return val * self._a
plot_osc(SquareOscillator, "Square")
osc = SquareOscillator()
wav = get_seq(osc)
wave_to_file(wav, fname="c4_maj_square.wav")
class SawtoothOscillator(Oscillator):
    def _post_freq_set(self):
        self._period = self._sample_rate / self._f
        self._post_phase_set
    def _post_phase_set(self):
        self._p = ((self._p + 90)/ 360) * self._period
    def _initialize_osc(self):
        self._i = 0
    def __next__(self):
        div = (self._i + self._p )/self._period
        val = 2 * (div - math.floor(0.5 + div))
        self._i = self._i + 1
        if self._wave_range != (-1, 1):
            val = self.squish_val(val, *self._wave_range)
        return val * self._a
plot_osc(SawtoothOscillator, "Sawtooth")
osc = SawtoothOscillator()
wav = get_seq(osc)
wave_to_file(wav, fname="c4_maj_saw.wav")
class TriangleOscillator(SawtoothOscillator):
    def __next__(self):
        div = (self._i + self._p)/self._period
        val = 2 * (div - math.floor(0.5 + div))
        val = (abs(val) - 0.5) * 2
        self._i = self._i + 1
        if self._wave_range is not (-1, 1):
            val = self.squish_val(val, *self._wave_range)
        return val * self._a
plot_osc(TriangleOscillator, "Triangle")
osc = TriangleOscillator()
wav = get_seq(osc)
wave_to_file(wav, fname="c4_maj_triangle.wav")
def fplot_xy(wave, fslice=slice(0,100), sample_rate=SR):
    fd = np.fft.fft(wave)
    fd_mag = np.abs(fd)
    x = np.linspace(0, sample_rate, len(wave))
    y = fd_mag * 2 / sample_rate
    return x[fslice], y[fslice]
freq = 100; fslice = slice(80,800)
fig = plt.figure(figsize=figsize)
osc = SineOscillator(freq=freq)
x,y = fplot_xy(get_val(iter(osc)), fslice)
plot((x,y), 1,4,1,"Sine Wave", "Hz", "energy", color=colors[0], xticks=[100,300,500,700])
osc = TriangleOscillator(freq=freq)
x,y = fplot_xy(get_val(iter(osc)), fslice)
plot((x,y), 1,4,2, "Triangle Wave", "Hz", color=colors[1], xticks=[100,300,500,700])
osc = SawtoothOscillator(freq=freq)
x,y = fplot_xy(get_val(iter(osc)), fslice)
plot((x,y), 1,4,3, "Sawtooth Wave", "Hz", color=colors[2], xticks=[100,200,300,400,500,600,700])
osc = SquareOscillator(freq=freq)
x,y = fplot_xy(get_val(iter(osc)), fslice)
plot((x,y), 1,4,4, "Square Wave", "Hz", color=colors[3], xticks=[100,300,500,700])
fig.savefig("freq_dom.jpg")
dur = 10
class WaveAdder:
    def __init__(self, *oscillators):
        self.oscillators = oscillators
        self.n = len(oscillators)
    
    def __iter__(self):
        [iter(osc) for osc in self.oscillators]
        return self
    
    def __next__(self):
        return sum(next(osc) for osc in self.oscillators) / self.n
osc = WaveAdder(
    SquareOscillator(27.5, amp=0.1),
    TriangleOscillator(55, amp=0.5),
    SineOscillator(110),
    SquareOscillator(220, amp=0.1),
    SineOscillator(440,amp=0.3),
    TriangleOscillator(880,amp=0.05),
)
wav = get_val(iter(osc), 44100 * dur)
osc2 = WaveAdder(
    SquareOscillator(27.5, amp=0.1),
    TriangleOscillator(55, amp=0.5),
    SineOscillator(115),
    SquareOscillator(220, amp=0.1),
    SineOscillator(440,amp=0.3),
    TriangleOscillator(880,amp=0.05),
)
wav2 = get_val(iter(osc2), 44100 * dur)
wave_to_file(wav, wav2, fname="ot_vibes.wav")
dur = 10
osc = WaveAdder(
    SineOscillator(librosa.note_to_hz("A2")),
    SineOscillator(librosa.note_to_hz("A2")+3),
    TriangleOscillator(librosa.note_to_hz("A4"),amp=0.6),
    TriangleOscillator(librosa.note_to_hz("E5"),amp=0.8),
)
wav = get_val(iter(osc), 44100 * dur)

osc2 = WaveAdder(
    SineOscillator(librosa.note_to_hz("A2")),
    SineOscillator(librosa.note_to_hz("A2")+3),
    TriangleOscillator(librosa.note_to_hz("C5"),amp=0.8),
    TriangleOscillator(librosa.note_to_hz("F5"),amp=0.6),
)
wav2 = get_val(iter(osc2), 44100 * dur)
wave_to_file(wav, wav2, fname="a_min6.wav")


    
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

    #if len(wavData.columns) == 2:
        #wavData.columns = ['R', 'L']
        #stereo_R = pd.DataFrame(wavData['R'])
        #stereo_L = pd.DataFrame(wavData['L'])

    if (len(wavData.columns) == 1):
        wavData.columns = ['M']

    return(wavData)


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

def csv_to_wav(input_filename):
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


#this function accepts a 64bit string, converts it into a wav file, adjusts the freuency for humorous affect, and then returns a dictionary containing the new 64bit string and a 2d array containing the sampling points to recreate the file
def frequency_modulator(string):
    wav_file = open('temp.wav', 'wb')
    decode_string = base64.b64decode(string)
    wav_file.write(decode_string)
    CHANNELS = 1
    swidth = 2
    spf = wave.open('temp.wav')
    RATE=spf.getframerate()
    signal = spf.readframes(-1)
    wf = wave.open('new.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(swidth)
    wf.setframerate(RATE*2)
    wf.writeframes(signal)
    wf.close()

    wav_string = base64.b64encode(open('new.wav', 'rb').read())
    array = wav_to_array('new.wav')
    #print(array)

    dictionary = {
        "string": wav_string,
        "array": array
    }
    

    
#this function creates a robot-like effect on audio files by overlaying several of the same file with slight offsets
#arguments: input_filename: name of wav file to apply effect. level: the amount of overlays
#output: python dctionairy containing the changed audio file in both csv and string base64 format
def roboticize(input_filename, level):
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

def VolumeModulator(filename, value):
    file = open(filename)
    csv_file = csv.reader(file)
    temp_csv = []
    new_csv = []
    for row in csv_file:
        temp_csv.append(row)
    for row in temp_csv[1:]:
        row[1] = str(int(row[1]) + value)
        #new_csv.append(row)
    #outfile = np.asarray(new_csv)
    outfile = np.asarray(temp_csv)
    np.savetxt( (filename[:-4] + "added.csv"), outfile, delimiter=',', fmt = '%s')


        
