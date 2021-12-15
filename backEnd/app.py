from flask import Flask, render_template, request, make_response, url_for, send_file, jsonify
from scipy.io import wavfile
from thm import *
from io import StringIO, BytesIO
import base64
import json
from flask_cors import CORS
import wave


app = Flask(__name__)


CORS(app) # remove for live site

'''
Compresses the given array
'''
def compress(returnarray, scale):
    temparray = []
    for i in range(0, len(returnarray)-scale, scale):
        min = 0
        max = 0
        for j in range(scale):
            if returnarray[i+j] > max:
                max = returnarray[i+j]
            elif returnarray[i+j] < min:
                min = returnarray[i+j]
        temparray.append(max)
        temparray.append(min)
    return temparray

'''
Default route to serve the web page
'''
@app.route("/")
def index():
    return render_template("home.html")


'''
Anonymous fxn inside process to facilitate creation of audio blobs
INPUT: array (floats), frequency (int)
OUTPUT: base64 representation
'''

def create_aud_buf(audio, freq):
    bytes_wav = bytes()
    byte_io = BytesIO(bytes_wav)
    wavfile.write(byte_io, freq, audio)
    wav_bytes = byte_io.read()

    audio_data = base64.b64encode(wav_bytes)
    return audio_data

'''
Does most of the heavy lifting
INPUT: Requires a POST file
OUTPUT: Downsampled file
'''
@app.route("/process", methods=['POST', 'GET'])
def process():

    #print("processing hit")

    print(request.files)
    if 'file' in request.files:
        #print('file exist')
        try:
            samp_freq, sound = wavfile.read(request.files['file'])

            if len(sound) > (1*(10**6)):
                # Conforms the sound into a manageable size 
                sound = sound[:100000]

        except:
            return redirect("/")

        # print(samp_freq, sound)
        # print(len(sound))

        # Audio buffer of the original
        audio_data = create_aud_buf(sound, samp_freq)

        # Checks the channels
        if sound.ndim > 1:
            sound = sound[1:, 0]
          
        # Bulk of the output with various dict outputs 
        audio_out = resample_summary(sound, samp_freq)
        print(audio_out)

        if len(audio_out) == 1:
            newsound = audio_out[0]["data"]
        else:
            newsound = sound


        # Get the rate of change from the original
        change = samp_freq/audio_out[0]["ny_rate"]

        # Audio buffer of modified
        audio_data_out = create_aud_buf(newsound, audio_out[0]["ny_rate"])


        # Prepare the file
        wave_file = wave.open(request.files['file'], mode='rb')
        sound = [sound.tolist()]
        newsound = [newsound.tolist()]


        while len(sound[len(sound)-1]) > 2:
            print("GOOD")
            sound.append(compress(sound[len(sound)-1], 20))

        while len(newsound[len(newsound)-1]) > 2:
            newsound.append(compress(newsound[len(newsound)-1], 20))

        data = str([[[pow(8, wave_file.getsampwidth())]],
                    sound, newsound, change])

        response = make_response(
            {"audio_in": str(audio_data), "data": data, "audio_out": str(audio_data_out)}, 
            200)

        audio_transf = str(audio_data)


        return response

    else:
        print('false')

    return {
        "message": "Failure"
    }



def process_defaults(filepath):

        samp_freq, sound = wavfile.read(filepath)
        # print(samp_freq, sound)
        # print(len(sound))

        audio_data = create_aud_buf(sound, samp_freq)

        if sound.ndim > 1:
            sound = sound[1:, 0]
            print("test1")
        sound = sound[1:100000]



        audio_out = resample_summary(sound, samp_freq)


        if len(audio_out) == 1:
            newsound = audio_out[0]["data"]
        else:
            newsound = sound

        change = samp_freq/audio_out[0]["ny_rate"]

        audio_data_out = create_aud_buf(newsound, audio_out[0]["ny_rate"])


        wave_file = wave.open(filepath, mode='rb')
        sound = [sound.tolist()]
        newsound = [newsound.tolist()]

        while len(sound[len(sound)-1]) > 2:
            print("GOOD")
            sound.append(compress(sound[len(sound)-1], 20))

        while len(newsound[len(newsound)-1]) > 2:
            newsound.append(compress(newsound[len(newsound)-1], 20))

        data = str([[[pow(8, wave_file.getsampwidth())]],
                    sound, newsound, change])

        return {"audio_in": str(audio_data), "data": data, "audio_out": str(audio_data_out)}

        

    
@app.route("/defaults" )
def defaults():
    return {"cantina": process_defaults("./cantina.wav"), "sine": process_defaults("./sine.wav"), "star_wars" : process_defaults("./StarWars3.wav"), "taunt": process_defaults("taunt.wav")}
    

if __name__ == '__main__':
    main()