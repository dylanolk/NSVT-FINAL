import matplotlib.pyplot as plt
from math import sqrt, ceil
import numpy as np
import os
from scipy import nanmean
from scipy.io import wavfile
from scipy.fft import *
from scipy.signal import resample


def generate_signal(len_sec, sampling_rate, frequencies_list, func="sin", add_noise=0, plot=False):
    
    frequencies_list = np.array(frequencies_list, dtype=object)

    expanded = False
    if isinstance(frequencies_list[0], int):
        frequencies_list = np.expand_dims(frequencies_list, axis=0)
        expanded = True
        
    npnts = sampling_rate*len_sec  # number of time samples
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


def simple_downsample(data, downsample_factor = 1):
    pad_size = ceil(float(data.size)/downsample_factor)*downsample_factor - data.size
    data_pad = np.append(data, np.zeros(pad_size)*np.NaN)
    interp = nanmean(data_pad.reshape(-1,downsample_factor), axis=1)
    return interp


#from stack overflow
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(sqrt(n)) + 1

    for d in range(3, sqr, 2):
        if n % d == 0:
            return False
        
    return True

def fft_(data, rfft_use = False):
    N = len(data)
    y = data
    
    # efficiency check
    if is_prime(N):
        N.append(0)
    
    if rfft_use:
        Y_k_pos = np.abs(np.fft.rfft(y))/N
    else:
        # has real negative imagin -> squash to only quad 1
        Y_k = np.fft.fft(y)[0:int(N/2)]/N # FFT + norm
        Y_k[1:] = 2*Y_k[1:] # single-sided spectrum only
        Y_k_pos = np.abs(Y_k) # only real part
    
    return Y_k_pos

def fft_filter(data, threshold_pre = 99):
    threshold = np.percentile(data, threshold_pre)
    threshold_indices = data < threshold
    data[threshold_indices] = 0
    
    return data

def find_ny(fdata):
    min_sample_rate = np.max(np.nonzero(fdata))*2+1
    return min_sample_rate

def resample_(data, duration, new_rate = -1):
    #print(new_rate, type(new_rate))
    return resample(data, int(new_rate*duration))

def ifft_(fdata):
    return np.fft.ifft(fdata)

def resample_summary(data, original_rate, new_rate = 0, threshold = 99):
    
    duration = len(data)/original_rate
    
    def channel_summary(c):
        ret = {}
        ret["fdata"] = fft_(c)
        ret["ffdata"] = fft_filter(ret["fdata"], threshold)
        ret["ny_rate"] = find_ny(ret["ffdata"])
        ret["ifftdata"] = ifft_(ret["fdata"])
        
        if new_rate == 0:
            new_data = resample_(data, duration, ret["ny_rate"])
        else:
            new_data = resample_(data, duration, new_rate)
        ret["data"] = new_data
        return ret
        
        
    channels = []
    if type(data[0]) == list:
        x,y = map(list, zip(*data))
        channels = [x,y]
    else:
        channels = [data]
        
    resampled_channels = [] 
    for each in channels:
        resampled_channels.append(channel_summary(each))
    
    return resampled_channels
           
    
    