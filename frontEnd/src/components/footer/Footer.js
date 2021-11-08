import { waitForElementToBeRemoved } from "@testing-library/react";
import React from "react";
import "./Footer.style.css";

const Footer = () => {
  return (
    <div class="footer">
      <p className="font">
        499 Capstone Project: Dylan Olk, Seth Spiegel, Eric Li, Kevin
        Markman-Lopez
      </p>
    </div>
  );
};

export default Footer;
