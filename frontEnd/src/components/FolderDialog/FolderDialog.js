import React, { useState } from "react";
import "./FolderDialog.style.css";
import Button from "../buttons/Button";
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

  changeHandler(event) {
    this.setState({ selectedFile: event.target.files[0] });
    this.setState({ isFilePicked: true });
    console.log(event.target.files[0]);
  }

  async postSelectedFile(selectedFile) {
    const formData = new FormData();
    formData.append("file", selectedFile);
    var tempArray = [];

    await axios
      .post("http://127.0.0.1:5000/process", formData)

      .then((response) => {
        console.log("this is response", response);
        this.props.changeAudio(
          response.data.audio_in.substring(2, response.data.audio_in.length - 1),
		  response.data.audio_out.substring(2, response.data.audio_out.length - 1)
        );
	
        console.log(
          "comparison",
          response.data.audio_out.substring(2, response.data.audio_out.length - 1).length,
		  response.data.audio_in.substring(2, response.data.audio_in.length - 1).length
        );
        return response;
      })

      .then(function (text) {
        tempArray = JSON.parse(text.data.data);
      });

    this.props.changeArrays(tempArray);

    this.setState({ isFilePicked: false });
  }

  render() {
    return (
      <div class="cards">
        <div>
          <h5>Select File:</h5>
          <p>Choose the sound file you want to run through the visualizer.</p>

          {!this.state.isFilePicked ? (
            <input type="file" name="file" class="button" onChange={this.changeHandler} />
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
