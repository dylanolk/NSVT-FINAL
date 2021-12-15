from pydub import AudioSegment
from pydub.playback import play



file = input("enter wav file to roboticize")
while(file[-4:] != ".wav"):
        file = input("file name must end in '.wav' ")
          
overlay = int(input("enter level of robotishness"))

audio = AudioSegment.from_file(file) #your first audio file

for i in range (overlay):
    audio = audio.overlay(audio, position = 5)          #combine , superimpose audio files

#If you need to save mixed file
audio.export("mixed.wav", format='wav') #export mixed  audio file
play(audio)                             #play mixed audio file
