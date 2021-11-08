<<<<<<< HEAD
from flask import Flask, render_template, request, make_response, url_for, redirect
=======
from flask import Flask, render_template, request, make_response, url_for, send_file
>>>>>>> 9ffd43c01f325bac2fc568430a8f0a77c9c3435b
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
	temparray=[]
	for i in range(0,len(returnarray)-scale,scale):
		min=0;
		max=0;
		for j in range(scale):
			if returnarray[i+j] > max:
				max = returnarray[i+j]
			elif returnarray[i+j] < min:
				min = returnarray[i+j]
		temparray.append(max)
		temparray.append(min)
	return temparray;

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/process", methods = ['POST','GET'])
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

		bytes_wav = bytes()
		byte_io = BytesIO(bytes_wav)
<<<<<<< HEAD

		#wavfile.write(byte_io, sampFreq, sound)

		newsound = resample_(sound)
		print(newsound[1])

		wavfile.write(byte_io, newsound[1], newsound[0])

		wav_bytes = byte_io.read()
		audio_data = base64.b64encode(wav_bytes).decode('UTF-8')
=======
>>>>>>> 9ffd43c01f325bac2fc568430a8f0a77c9c3435b

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
		# print(newsound)

		# wavfile.write(byte_io, newsound[1], newsound[0])

		# wav_bytes = byte_io.read()
		# audio_data = base64.b64encode(wav_bytes).decode('UTF-8')
		wave_file=wave.open(request.files['file'], mode='rb')
		sound=[sound.tolist()]
		newsound=[newsound.tolist()]
		print(len(newsound[0]))
		print(len(sound[0]))
		
		while len(sound[len(sound)-1])> 2:
			print("GOOD");
			sound.append(compress(sound[len(sound)-1],20))
		
		while len(newsound[len(newsound)-1])> 2:
			newsound.append(compress(newsound[len(newsound)-1],20))		
		
		return str([[[pow(8,wave_file.getsampwidth())]], sound, newsound, change])
		
	else:
		print('false')


	return render_template("home.html")
	
	
	
	
	
	