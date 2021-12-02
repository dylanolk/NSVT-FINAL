import React from "react";
import "./About.style.css";
import ReactPlayer from "react-player";

const About = () => {
  return (
    <div>
      <div class="aboutcontainer">
        <h2>So what's the deal with the Nyquist Shannon Theorem?</h2>
        <ul>
          <li>
            The Nyquist-Shannon Theorem is a technique to create a perfectly
            lossless representation of a sound wave using far less information.
          </li>
          <li>
            The Nyquist-Shannon Theorem states that as long as your number of
            sampling points is at least twice as great as the signal’s highest
            frequency, you can create a wave using only those points without
            losing any information at all.
          </li>
          <li>
            Our visualizer accepts a large audio file and reduces the amount of
            points without any audio loss or drop in quality.
          </li>
        </ul>
      </div>
      <div class="aboutvideo">
        <ReactPlayer url="https://www.youtube.com/watch?v=FcXZ28BX-xE&t=330s&ab_channel=SteveBrunton" />
      </div>
    </div>
  );
};

export default About;
