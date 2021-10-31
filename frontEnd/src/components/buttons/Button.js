import React from "react";
import "./buttons.style.css";

const Button = ({ title, handleSubmission }) => {
  return (
    <button class="sub-button" onClick={handleSubmission}>
      {title}
    </button>
  );
};

export default Button;
