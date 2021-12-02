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
<<<<<<< HEAD
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

        bytes_wav = bytes()
        byte_io = BytesIO(bytes_wav)

        #wavfile.write(byte_io, sampFreq, sound)
        if sound.ndim > 1:
            sound = sound[1:, 0]
            print("test1")
        sound = sound[1:100000]
        print("test2")
        aa = resample_summary(sound, sampFreq)
        print("test")

        if len(aa) == 1:
            newsound = aa[0]["data"]

        # else:
            # newsound = np.stack((aa[1]["data"],aa[0]["data"]), axis = 1)
            # newsound = np.asarray(newsound)

        change = sampFreq/aa[0]["ny_rate"]
        # print(newsound)

        # wavfile.write(byte_io, newsound[1], newsound[0])

        # wav_bytes = byte_io.read()
        # audio_data = base64.b64encode(wav_bytes).decode('UTF-8')
        wave_file = wave.open(request.files['file'], mode='rb')
        sound = [sound.tolist()]
        newsound = [newsound.tolist()]
        print(len(newsound[0]))
        print(len(sound[0]))

        while len(sound[len(sound)-1]) > 2:
            print("GOOD")
            sound.append(compress(sound[len(sound)-1], 20))

        while len(newsound[len(newsound)-1]) > 2:
            newsound.append(compress(newsound[len(newsound)-1], 20))

        return str([[[pow(8, wave_file.getsampwidth())]], sound, newsound, change])

    else:
        print('false')

    return render_template("home.html")
=======
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

		#wavfile.write(byte_io, sampFreq, sound)
		if sound.ndim > 1 :
			sound= sound[1:, 0]
			print("test1")
		sound=sound[1:100000]
		print("test2")
		aa = resample_summary(sound, sampFreq)
		print("test")
		
	

		if len(aa) == 1:
			newsound = aa[0]["data"]
			
		# else:
			# newsound = np.stack((aa[1]["data"],aa[0]["data"]), axis = 1)
			# newsound = np.asarray(newsound)
		

		change=sampFreq/aa[0]["ny_rate"]


		wave_file=wave.open(request.files['file'], mode='rb')
		sound=[sound.tolist()]
		newsound=[newsound.tolist()]

		print("===")
		print(type(sound))
		print(type(newsound))
		print("===")
		#audio_data2 = create_aud_buf(newsound, int(aa[0]["ny_rate"]))
		# print("===")
		# print(type(newsound))
		# print(type(aa[0]["ny_rate"]))
		# print("===")



		'''

		data: [[]]


		data
			data [[]]
			payload ...
			
		'''

		print(len(newsound[0]))
		print(len(sound[0]))
		
		while len(sound[len(sound)-1])> 2:
			print("GOOD");
			sound.append(compress(sound[len(sound)-1],20))
		
		while len(newsound[len(newsound)-1])> 2:
			newsound.append(compress(newsound[len(newsound)-1],20))		

		data = str([[[pow(8,wave_file.getsampwidth())]], sound, newsound, change])



		response = make_response({"payload": str(audio_data), "data": data}, 200)
		
		audio_transf = str(audio_data)
		# print(audio_transf)
		# print(type(audio_transf))

		#return render_template("home.html", value = audio_transf, vlen = len(audio_transf) -1 )
		return response
		
	else:
		print('false')


	return render_template("home.html")
	
	
	
	
	
	
>>>>>>> e0f11aa5c8f4b6075b0bb3ebd5f401d15d85baef
