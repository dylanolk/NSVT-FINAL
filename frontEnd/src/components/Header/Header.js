import React from "react";
import "./header.style.css";

function Header() {
  return (
  <div class="navbar_wrapper">
   <div class="my_navbar">
   <button>
      <a class="navbar-brand" href="/">
        Nyquist Shannon Theorem Visualizer
      </a>
	</button>
    <button>
            <a class="nav-link" href="/about">
                About The Theorem <span class="sr-only">(current)</span>

            </a>
	</button>
  </div>
  </div>
  );
}

export default Header;
