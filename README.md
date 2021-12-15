# Nyquist-Shannon-Visualizer 
CSCI-499 Capstone Project 
by Dylan Olk, Eric Li, Seth Spiegal, and Kevin Markman-Lopez 

---------------------------------------
#### Introduction
Our project is a sine-wave visualizer designed to take in a wav file uploaded by a user, and output a visualization of the difference between the original waveform and the waveform that has been processed using the Nyquist-Shannon Theorem. A new .wav file will also be returned which will contained a smaller yet audibly identical .wave file. 

Our project is built with a React front end and a Python Flask back end. 

Here are some guidelines on how to download and run our project. We recommend visiting the following links and getting that set up. 
*  [React](https://reactjs.org/docs/getting-started.html)
*  [Python](https://www.python.org/downloads/)
*  [VS Code](https://code.visualstudio.com/)
              
---------------------------------------
#### Setup
1. Clone this repo into an appropriate folder 
2. Fire up the React Server: 
 `cd FrontEnd`

 `npm install`

 `npm start`

 Install the needed React dependencies and start it up. 

	Front end servers will need to be running in order for our project to work. 
Note that it runs from `localhost:3000`.

>Tip: Open a new command window or tab so that you can easily switch between the two. Furthermore, both the backend and front end needs to be running. 

3. Fire up the Flask server: same deal. 
`cd nyquist-test`

`pip install -r requirements.txt`

`export FLASK_APP=app`

`flask run`

This time locate the nyquist-test folder, which is where the back end runs from. Install the needed Python modules from requirements and run the server. Note that it runs from `localhost:5000`.
> Tip: It is recommended you use a virtual environment to not pollute your current Python setup. Before you `pip install` do this first:
> `python3 -m pip install --user virtualenv`

> `python3 -m venv env`

> `source env/bin/activate`

4. At this point, go to `localhost:3000` to view the page and interact.

---------------------------------------

#### Web Page Instructions

5. Now that you've got everything set up, mosey over to the webpage opened up when you ran `npm start`. 
6. Use the file dialog to upload a wav file of your choice. Note that browser restrictions may prevent wav files of certain sizes. 
7. Click convert. 
8. The visualization will appear below the Folder Dialog and you'll notice you can use your mouse wheel to zoom through the visualization.
9. At the bottom of the visualization you can toggle between showing the original, processed, or both wavforms. 
10. Finally, you'll be able to hear both the original and processed versions of the wav file and both will be available for download. 

---------------------------------------
#### Issues and Potential Concerns
- Firefox and Chrome are the preferred but based on settings and extensions, performance will vary
	- Extensions like Privacy Badger will break it!
- Use **[VLC](https://www.videolan.org/vlc/download-windows.html)** to play any downloaded audio files. 
	- We are using the default HTML audio tag, which based on browser and compatibility may run into issues. All functionality has been tested and shown to work with VLC. 


---------------------------------------
Thanks for using our tool! We hope that is provides  you with some valuable insight into the applicaiton of the Shannon-Nyquist Theorem! 
