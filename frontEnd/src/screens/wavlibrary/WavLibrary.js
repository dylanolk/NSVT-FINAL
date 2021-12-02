import React from "react";
import { Link } from "react-router-dom";
import "./WavLibrary.style.css";
// import "../../photos/lightpattern.jpeg";

const WavLibrary = () => {
  return (
    <div class="centered">
      <h1>Sample Library</h1>
      <div class="center-text">
        <p>This is a little library of sample .wav files</p>
      </div>
      <div class="row">
        <div class="column">
          <div class="card bg-dark mb-3">
            <h3>Cantina</h3>
            <audio
              type="audio/mpeg"
              src="./cantina.wav"
              controls
              autoplay
              autostart="false"
            ></audio>
            <Link to="/cantina.wav" target="_blank" download>
              Download
            </Link>
          </div>
        </div>
        <div class="column">
          <div class="card bg-dark mb-3">
            <h3>Star Wars </h3>
            <audio
              type="audio/mpeg"
              src="./StarWars3.wav"
              controls
              autoplay
              autostart="false"
            ></audio>
            <Link to="/StarWars3.wav" target="_blank" download>
              Download
            </Link>
          </div>
        </div>
        <div class="column">
          <div class="card bg-dark mb-3">
            <h3>Taunt</h3>
            <audio
              type="audio/mpeg"
              src="./taunt.wav"
              controls
              autoplay
            ></audio>
            <Link to="/taunt.wav" target="_blank" download>
              Download
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default WavLibrary;
