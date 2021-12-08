import React, { useState, useEffect } from "react";
import ReactAudioPlayer from "react-audio-player";
import AudioPlayer from "react-h5-audio-player";
import "react-h5-audio-player/lib/styles.css";
import { isPropertySignature } from "typescript";
import { WaveFile } from "wavefile";

class PlayAudio extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <div class="container">
          <p>This is the original.</p>
          {this.props.audio && (
            <audio
              controls
              src={"data:audio/wav;base64," + this.props.audio}
            ></audio>
          )}
        </div>
        <div class="container">
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
