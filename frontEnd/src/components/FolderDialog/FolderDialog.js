import React, { useState } from "react";
import "./FolderDialog.style.css";
import Button from "../buttons/Button";

import SoundWave from "../SoundWave";

const FolderDialog = () => {
  const [selectedFile, setSelectedFile] = useState();
  const [isFilePicked, setIsFilePicked] = useState(false);

  const changeHandler = (event) => {
    setSelectedFile(event.target.files[0]);
    setIsFilePicked(true);
    console.log(event.target.files[0]);
  };

  const postSelectedFile = async () => {
    const formData = new FormData();
    formData.append("file", selectedFile);
    const response = await fetch("http://127.0.0.1:5000/process", {
      method: "POST",
      body: formData,
      headers: {
        "content-type": "base64",
      },
    });
    const resData = await response.json();
    console.log(resData, "line 28");
    console.log(resData, "this is the response Data");
    // } catch (error) {
    //   console.log(error, "you messed something up");
    // }
  };

  return (
    <div class="cards">
      <div>
        <h5>Select File:</h5>
        <p>Choose the sound file you want to run through the visualizer.</p>
        {isFilePicked && <SoundWave />}
        {!isFilePicked ? (
          <input type="file" name="file" onChange={changeHandler} />
        ) : (
          <Button title="Convert File" handleSubmission={postSelectedFile} />
        )}
      </div>
    </div>
  );
};
export default FolderDialog;
