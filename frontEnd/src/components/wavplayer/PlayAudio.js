import React, { useState, useEffect } from "react";
import ReactAudioPlayer from "react-audio-player";
import AudioPlayer from "react-h5-audio-player";
import "react-h5-audio-player/lib/styles.css";
import { isPropertySignature } from "typescript";

const PlayAudio = (props) => (
  <AudioPlayer
    autoPlay
    src={props}
    onPlay={(e) => console.log("onPlay")}
    // other props here
  />
);

export default PlayAudio;
