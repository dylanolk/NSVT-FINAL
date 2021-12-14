from flask import Flask, render_template, request, make_response, url_for, send_file
from scipy.io import wavfile
from thm import *
from io import StringIO, BytesIO
import base64
from flask import jsonify
import json
from flask_cors import CORS
import wave

app = Flask(__name__)
CORS(app)


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


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/process", methods=['POST', 'GET'])
def process():
    print("here")
    print(request.files)
    if 'file' in request.files:
        print('true')
        try:
            sampFreq, sound = wavfile.read(request.files['file'])
        except:
            return redirect("/")

        print(sampFreq, sound)
        print(len(sound))

        def create_aud_buf(audio, freq):
            bytes_wav = bytes()
            byte_io = BytesIO(bytes_wav)
            wavfile.write(byte_io, freq, audio)
            wav_bytes = byte_io.read()

            audio_data = base64.b64encode(wav_bytes)
            return audio_data

        audio_data = create_aud_buf(sound, sampFreq)

        if sound.ndim > 1:
            sound = sound[1:, 0]
            print("test1")
        sound = sound[1:100000]



        audio_out = resample_summary(sound, sampFreq)
        print(audio_out)

        if len(audio_out) == 1:
            newsound = audio_out[0]["data"]
        else:
            newsound = sound

        change = sampFreq/audio_out[0]["ny_rate"]

        audio_data_out = create_aud_buf(newsound, audio_out[0]["ny_rate"])


        wave_file = wave.open(request.files['file'], mode='rb')
        sound = [sound.tolist()]
        newsound = [newsound.tolist()]

        print("===")
        print(type(sound))
        print(type(newsound))
        print("===")
        print(len(newsound[0]))
        print(len(sound[0]))

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


        # return render_template("home.html", value = audio_transf, vlen = len(audio_transf) -1 )
        return response

    else:
        print('false')

    return render_template("home.html")

def process_defaults(filepath):

        sampFreq, sound = wavfile.read(filepath)
        print(sampFreq, sound)
        print(len(sound))

        def create_aud_buf(audio, freq):
            bytes_wav = bytes()
            byte_io = BytesIO(bytes_wav)
            wavfile.write(byte_io, freq, audio)
            wav_bytes = byte_io.read()

            audio_data = base64.b64encode(wav_bytes)
            return audio_data

        audio_data = create_aud_buf(sound, sampFreq)

        if sound.ndim > 1:
            sound = sound[1:, 0]
            print("test1")
        sound = sound[1:100000]



        audio_out = resample_summary(sound, sampFreq)


        if len(audio_out) == 1:
            newsound = audio_out[0]["data"]
        else:
            newsound = sound

        change = sampFreq/audio_out[0]["ny_rate"]

        audio_data_out = create_aud_buf(newsound, audio_out[0]["ny_rate"])


        wave_file = wave.open(filepath, mode='rb')
        sound = [sound.tolist()]
        newsound = [newsound.tolist()]

        print("===")
        print(type(sound))
        print(type(newsound))
        print("===")
        print(len(newsound[0]))
        print(len(sound[0]))

        while len(sound[len(sound)-1]) > 2:
            print("GOOD")
            sound.append(compress(sound[len(sound)-1], 20))

        while len(newsound[len(newsound)-1]) > 2:
            newsound.append(compress(newsound[len(newsound)-1], 20))

        data = str([[[pow(8, wave_file.getsampwidth())]],
                    sound, newsound, change])

    
        return {"audio_in": str(audio_data), "data": data, "audio_out": str(audio_data_out)}

     


        # return render_template("home.html", value = audio_transf, vlen = len(audio_transf) -1 )
        

	
@app.route("/defaults" )
def defaults():
	return {"cantina": process_defaults("./cantina.wav"), "sine": process_defaults("./sine.wav"), "star_wars" : process_defaults("./StarWars3.wav"), "taunt": process_defaults("taunt.wav")}
	
