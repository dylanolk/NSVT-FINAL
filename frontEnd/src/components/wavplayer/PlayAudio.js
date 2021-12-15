import React, { useState, useEffect } from "react";
import "react-h5-audio-player/lib/styles.css";
import { WaveFile } from "wavefile";
import fs from "fs";

class PlayAudio extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    const fileName = "processedAudio" + Date.now();
    const audioFile = new File([this.props.processed], `${fileName}.wav`, {
      type: "audio/wav",
      lastModified: Date.now(),
    });
    console.log("audioFile:", audioFile);

	
if(this.props.audio){
  // fetch("data:audio/wav;base64," + this.props.audio)
    // .then(res => res.blob())
    // .then(blob => {
      // console.log(blob);
      // var url = window.URL.createObjectURL(blob);
	  // console.log(url);
	  // window.location.assign(url);
    // });
	console.log("***",this.props.processed)
	console.log("***",this.props.audio)
	
  // fetch("data:audio/wav;base64," + this.props.processed)
    // .then(res => res.blob())
    // .then(blob => {
      // console.log(blob);
      // var url = window.URL.createObjectURL(blob);
	  // console.log(url);
	  // window.location.assign(url);
    // });
}
	
	
    return (
      <div>
        <div class="originalAudio">
          <p>This is the original.</p>
          {this.props.audio && (
            <audio
              controls
              src={"data:audio/wav;base64," + this.props.audio}
            ></audio>
          )}
        </div>
        <div class="compressedAudio">
          <p>This is the processed audio.</p>
          {this.props.audio && (
            <audio
              controls
              src={"data:audio/wav;base64," + this.props.processed}
            ></audio>
          )}
        </div>
      </div>
    );
  }
}

export default PlayAudio;
