import librosa
import soundfile as sf

file, sr = librosa.load("gettysburg10")

funny_file = librosa.effects.pitch_shift(y, sr, n_steps=4)

librosa.output.write_wav("pitched_up_gettysburg.wav", funny_file, sr)
