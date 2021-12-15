import React, { useState, useEffect } from "react";
import "react-h5-audio-player/lib/styles.css";
import { WaveFile } from "wavefile";
import fs from "fs";
import "./Play.Audio.style.css"

class PlayAudio extends React.Component {
  constructor(props) {
    super(props);
	
	this.downloadProcessed=this.downloadProcessed.bind(this);
	this.downloadAudio=this.downloadAudio.bind(this);
  }



	
	downloadProcessed(){
	  fetch("data:audio/wav;base64," + this.props.processed)
		.then(res => res.blob())
		.then(blob => {
		  console.log(blob);
		  var url = window.URL.createObjectURL(blob);
		  console.log(url);
		  window.location.assign(url);
		});
		console.log("***",this.props.processed)
		console.log("***",this.props.audio)
	}
	
	downloadAudio(){
	  fetch("data:audio/wav;base64," + this.props.audio)
		.then(res => res.blob())
		.then(blob => {
		  console.log(blob);
		  var url = window.URL.createObjectURL(blob);
		  console.log(url);
		  window.location.assign(url);
		});
		console.log("***",this.props.processed)
		console.log("***",this.props.audio)
	}
  render() {
	
    return (
      <div class="audio_player">
        <div class="originalAudio">
          <p>This is the original.</p>
          {this.props.audio && (
		  <div>
            <audio
              controls
              src={"data:audio/wav;base64," + this.props.audio}
            ></audio>
			<button onClick={this.downloadAudio}>
				Download
			</button>
			</div>
          )}
		  
        </div>
        <div class="compressedAudio">
          <p>This is the processed audio.</p>
          {this.props.audio && (
		  <div>
            <audio
              controls
              src={"data:audio/wav;base64," + this.props.audio}
            ></audio>
			<button onClick={this.downloadProcessed}>
				Download
			</button>
			 </div>
          )}
		 
        </div>
      </div>
    );
  }
}

export default PlayAudio;
