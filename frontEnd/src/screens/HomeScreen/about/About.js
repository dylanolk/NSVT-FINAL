import React from "react";
import "./About.style.css";
import ReactPlayer from "react-player";

const About = () => {
  return (
    <div>
      <div class="aboutcontainer">
        <p>So what's the deal with the Nyquist Shannon Theorem?</p>
        <ReactPlayer url="https://www.youtube.com/watch?v=FcXZ28BX-xE&t=330s&ab_channel=SteveBrunton" />
      </div>
    </div>
  );
};

export default About;
