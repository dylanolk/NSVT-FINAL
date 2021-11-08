import React, { useState } from "react";
import "./FolderDialog.style.css";
import Button from "../buttons/Button";

import SoundWave from "../SoundWave";
import axios from "axios";
axios.defaults.headers.common["Access-Control-Allow-Origin"] = "*";

class FolderDialog extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedFile: "",
      isFilePicked: false,
    };
    this.postSelectedFile = this.postSelectedFile.bind(this);
    this.changeHandler = this.changeHandler.bind(this);
  }
  // const [selectedFile, setSelectedFile] = useState();
  // const [isFilePicked, setIsFilePicked] = useState(false);

  changeHandler(event) {
    this.setState({ selectedFile: event.target.files[0] });
    this.setState({ isFilePicked: true });
    console.log(event.target.files[0]);
  }

  async postSelectedFile(selectedFile) {
    const formData = new FormData();
    formData.append("file", selectedFile);
    var temparray = [];
    await axios
      .post("http://127.0.0.1:5000/process", formData)
      .then(function (response) {
        return response;
      })
      .then(function (text) {
        temparray = text.data;
      });
    console.log(temparray);
    this.props.changeArrays(temparray);
    this.setState({ isFilePicked: false });
  }

  render() {
    return (
      <div class="cards">
        <div>
          <h5>Select File:</h5>
          <p>Choose the sound file you want to run through the visualizer.</p>

          {!this.state.isFilePicked ? (
            <input type="file" name="file" onChange={this.changeHandler} />
          ) : (
            <Button
              title="Convert File"
              handleSubmission={() =>
                this.postSelectedFile(this.state.selectedFile)
              }
            />
          )}
        </div>
      </div>
    );
  }
}
export default FolderDialog;
