import React from "react";
import "./header.style.css";

function Header() {
  return (
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">
        <p>Nyquist Shannon Theorem Visualizer</p>
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        /<span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="#">
              <p>
                About The Theorem <span class="sr-only">(current)</span>
              </p>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              <p>Contact Us</p>
            </a>
          </li>
        </ul>
      </div>
    </nav>
  );
}

export default Header;
