import pyaudio
import numpy as np
import threading

class WavePlayerLoop(threading.Thread) :
  """
  A simple class based on PyAudio to play sine wave at certain frequency.
  It's a threading class. You can play audio while your application
  continues to do stuff.
  """

  def __init__(self, freq=440., length=1., volume=0.5):
    threading.Thread.__init__(self)
    self.p = pyaudio.PyAudio()

    self.volume = volume     # range [0.0, 1.0]
    self.fs = 44100          # sampling rate, Hz, must be integer
    self.duration = length   # in seconds, may be float
    self.f = freq            # sine frequency, Hz, may be float

  def run(self) :
    """
    Just another name for self.start()
    """
    # generate samples, note conversion to float32 array
    self.samples = (np.sin(2*np.pi*np.arange(self.fs*self.duration)*self.f/self.fs)).astype(np.float32)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    self.stream = self.p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=self.fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively) 
    self.stream.write(self.volume*self.samples)

    self.stream.stop_stream()
    self.stream.close()

    self.p.terminate()

s = WavePlayerLoop(freq=440., length=10., volume=0.5)
s.run()
print ('this should print while there is a beep sound')

objs = []
number_of_threads = 10

print ('Creating thread objects')
for i in range(number_of_threads):
    objs.append(WavePlayerLoop(freq=440 * i, length=10., volume=0.1 * i))

print ('Starting thread objects')
for i in range(number_of_threads):
    objs[i].start()

print ('Waiting for threads to finish')
for i in range(number_of_threads):
    objs[i].join()

print ('Finishing program')


import pyaudio
import numpy as np
import threading

class WavePlayerLoop(threading.Thread) :
  """
  A simple class based on PyAudio to play sine wave at certain frequency.
  It's a threading class. You can play audio while your application
  continues to do stuff.
  """

  def __init__(self, freq=440., length=1., volume=0.5):
    threading.Thread.__init__(self)
    self.p = pyaudio.PyAudio()

    self.volume = volume     # range [0.0, 1.0]
    self.fs = 44100          # sampling rate, Hz, must be integer
    self.duration = length   # in seconds, may be float
    self.f = freq            # sine frequency, Hz, may be float

  def run(self) :
    """
    Just another name for self.start()
    """
    # generate samples, note conversion to float32 array
    self.samples = (np.sin(2*np.pi*np.arange(self.fs*self.duration)*self.f/self.fs)).astype(np.float32)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    self.stream = self.p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=self.fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively) 
    self.stream.write(self.volume*self.samples)

    self.stream.stop_stream()
    self.stream.close()

    self.p.terminate()

s = WavePlayerLoop(freq=440., length=10., volume=0.5)
s.run()
print ('this should print while there is a beep sound')

objs = []
number_of_threads = 10

print ('Creating thread objects')
for i in range(number_of_threads):
    objs.append(WavePlayerLoop(freq=440 * i, length=10., volume=0.1 * i))

print ('Starting thread objects')
for i in range(number_of_threads):
    objs[i].start()

print ('Waiting for threads to finish')
for i in range(number_of_threads):
    objs[i].join()

print ('Finishing program')
