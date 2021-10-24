from flask import Flask, render_template, request, make_response
from scipy.io import wavfile
from thm import freq
from io import StringIO, BytesIO
import base64

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/process", methods = ['POST','GET'])
def process():
	print("here")
	print(request.files)
	if 'file' in request.files:
		print('true')
		sampFreq, sound = wavfile.read(request.files['file'])
		print(sampFreq, sound)
		print(len(sound))

		bytes_wav = bytes()
		byte_io = BytesIO(bytes_wav)
		wavfile.write(byte_io, sampFreq, sound)
		wav_bytes = byte_io.read()
		audio_data = base64.b64encode(wav_bytes).decode('UTF-8')

		return render_template("home.html", value = audio_data, arr = sound)
	else:
		print('false')


	return render_template("home.html")