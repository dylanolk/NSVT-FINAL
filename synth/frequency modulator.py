import wave

CHANNELS = 1
swidth = 2
#Change_RATE = 2
Change_RATE = int(input("enter new speed"))

file = input("enter wav file name")
#outfile = input("enter output file name")
#spf = wave.open(file, 'rb')
spf = wave.open('gettysburg10.wav', 'rb')
RATE=spf.getframerate()
signal = spf.readframes(-1)

#wf = wave.open(("changed "+ file), 'wb')
wf = wave.open('new_gettysburg.wav', 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(swidth)
#wf.setframerate(RATE*Change_RATE)
#wf.setframerate(RATE/Change_RATE)
wf.writeframes(signal)
wf.close()
