# Nyquist-Shannon-Visualizer 
(A CSCI-499 Capstone Project by Dylan Olk, Eric Li, Seth Spiegal, and Kevin Markman-Lopez 

Our project is a sine-wave visualizer designed to take in a wav file uploaded by a user, and output a visualization of the difference between the original waveform and the waveform that has been processed using the Nyquist-Shannon Theorem. A new .wav file will also be returned which will contained a smaller yet audibly identical .wave file. 

Our project is built with a React front end and a Python Flask back end. 

Here are some guidelines on how to download and run our project. These guidelines assume you have all the necessary files installed on your computer as well as a IDE (Integrated Virtual Enviroment) such as VS code installed on your computer. If this isn't the case, we recommend visiting the following links and getting that set up. 
              React -- https://reactjs.org/docs/getting-started.html
              Python -- https://www.python.org/downloads/
              VS Code -- https://code.visualstudio.com/       ---> (VS code also provides excellent documentation on setting up your enviroment for writing React,                                                                       and Python code) 
1. Create a directory on your desktop (or wherever you prefer to download the project to on your computer) and download the repository files into it. 
2. Fire up the React Server: Open terminal or command prompt and cd your way into the frontEnd directory. If you're having trouble finding your way into the directory, we recommend locating it in Finder (mac) or File Explorer (P.C.) right clicking and copying the file path. Go back to terminal or command prompt and type cd, then paste the file path after it. (Don't forget a space between cd and the file path). Type 'npm start' into the terminal/command prompt window to start the server. 
          Tip: Open a new command window or tab so that you can easily switch between the two. Furthermore, both the back and 
          Front end servers will need to be running in order for our project to work. 
3. Fire up the Flask server: same deal. This time locate the nyquist-test folder, which is where the back end runs from. Once you've cd'ed your way into the folder type 'flask run' into the terminal/command prompt window 
4. You'll want to make sure all the dependencies are up to date so run 'npm install' to update react dependencies.

========= Web Page Instructions =========

5. Now that you've got everything set up, mosey over to the webpage opened up when you ran 'npm start'. 
6. Use the file dialog to upload a wav file of your choice. While this project is still in it's earlier stages, we recommend using wav files no longer than a few seconds.
7. Click convert. 
8. The visualization will appear below the Folder Dialog and you'll notice you can use your mouse wheel to zoom through the visualization.
9. At the bottom of the visualization you can toggle between showing the original, processed, or both wavforms. 
10. Finally, you'll be able to hear both the original and processed versions of the wav file and both will be available for download. 

Thanks for using our tool! We hope that is provides  you with some valuable insight into the applicaiton of the Shannon-Nyquist Theorem! 
