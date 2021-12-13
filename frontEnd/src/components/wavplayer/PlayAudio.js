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

    // let wav = new WaveFile();
    // console.log("this.props.data", this.props.data);
    // if (this.props.data) {
    //   console.log("inside if ", JSON.parse(this.props.data)[1][0]);
    //   wav.fromScratch(1, 44100, "8", JSON.parse(this.props.data)[1][0]);
    //   console.log("audioFile wav :", wav);
    // }

    // wav.toSampleRate(22050);

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
