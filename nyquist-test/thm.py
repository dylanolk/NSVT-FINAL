import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.io import wavfile
from scipy.fft import *
from scipy.signal import resample


def generate_signal(length_seconds, sampling_rate, frequencies_list, func="sin", add_noise=0, plot=True):
    
    frequencies_list = np.array(frequencies_list, dtype=object)
    assert len(frequencies_list.shape) == 1 or len(frequencies_list.shape) == 2, "frequencies_list must be 1d or 2d python list"
    
    expanded = False
    if isinstance(frequencies_list[0], int):
        frequencies_list = np.expand_dims(frequencies_list, axis=0)
        expanded = True
        
    npnts = sampling_rate*length_seconds  # number of time samples
    time = np.arange(0, npnts)/sampling_rate
    signal = np.zeros((frequencies_list.shape[0],npnts))
    
    for channel in range(0,frequencies_list.shape[0]):
        for fi in frequencies_list[channel]:
            if func == "cos":
                signal[channel] = signal[channel] + np.cos(2*np.pi*fi*time)
            else:
                signal[channel] = signal[channel] + np.sin(2*np.pi*fi*time)
    
        # normalize
        max = np.repeat(signal[channel].max()[np.newaxis], npnts)
        min = np.repeat(signal[channel].min()[np.newaxis], npnts)
        signal[channel] = (2*(signal[channel]-min)/(max-min))-1
    
    if add_noise:        
        noise = np.random.uniform(low=0, high=add_noise, size=(frequencies_list.shape[0],npnts))
        signal = signal + noise

    if plot:
        plt.plot(time, signal.T)
        plt.show()
    
    if expanded:
        signal = signal[0]
        
    return signal

def freq(file):
    # Open the file and convert to mono
    sr, data = wavfile.read(file)
    if data.ndim > 1:
        data = data[:, 0]
    else:
        pass

    # Fourier Transform
    N = len(data)
    yf = rfft(data)
    xf = rfftfreq(N, 1 / sr)

    # frequency spectrum as a plot
    # plt.plot(xf, np.abs(yf))
    # plt.show()

    # Get the most dominant frequency and return it
    idx = np.argmax(np.abs(yf))
    freq = xf[idx]
    return freq


def downsample(data, sampling_rate, new_rate = 0):

    if new_rate <= 0:
        sampling_rate/2 

    number_of_samples = round(len(data) * float(new_rate) / sampling_rate)
    data2 = sps.resample(data, number_of_samples)
    return data2

