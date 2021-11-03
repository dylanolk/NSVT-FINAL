from flask import Flask, render_template, request, make_response, send_file
from scipy.io import wavfile
from thm import freq
from io import StringIO, BytesIO
import base64
from flask import jsonify
import json
from flask_cors import CORS
import wave

app = Flask(__name__)
CORS(app)

print("dog")

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/process", methods = ['POST','GET'])
def process():
	print("here")
	print(request.files)
	list= []
	list.append(1)
	list.append(2)
	list.append(3)
	print(list)
	# return str(list)

	wav_bytes = -1
	if 'file' in request.files:
		print('true')
		sampFreq, sound = wavfile.read(request.files['file'])
		print(sampFreq, sound[:100])
		print(len(sound))
		wave_file=wave.open(request.files['file'], mode='rb')
		
		
		


		

		
		# bytes_wav = bytes()
		# byte_io = BytesIO(bytes_wav)
		# wavfile.write(byte_io, sampFreq, sound)
		
		# response = make_response(byte_io.read())
		
		# response.headers['Content-Type'] = 'audio/wav'
		# response.headers['Content-Disposition'] = 'attachment; filename=sound.wav'
		# return response

		# bytes_wav = bytes()
		# byte_io = BytesIO(bytes_wav)
		# wavfile.write(byte_io, sampFreq, sound)
		# wav_bytes = byte_io.read()
		# audio_data = base64.b64encode(wav_bytes).decode('UTF-8')

	return str([[pow(8,wave_file.getsampwidth())],sound.tolist()])
	# else:
		# print('false')


	# return render_template("home.html")
