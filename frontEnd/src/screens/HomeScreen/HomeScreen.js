import React, { useEffect, useState } from "react";
import "./HomeScreen.style.css";
import Header from "../../components/Header/Header";
import FolderDialog from "../../components/FolderDialog/FolderDialog";
import Canvas from "../../components/canvas/Canvas";
import Footer from "../../components/footer/Footer";
import Button from "../../components/buttons/Button";

import HomeScreenText from "../../components/text/HomeScreenText";
import PlayAudio from "../../components/wavplayer/PlayAudio";
import axios from "axios";

class HomeScreen extends React.Component {
  // const getData = async () => {
  // const response = await fetch("http://127.0.0.1:5000/", {
  // mode: "no-cors",
  // method: "GET",
  // });
  // const resData = await response;
  // console.log(resData, "damnn");
  // };

  // useEffect(() => {
  // getData();
  // console.log("hi");
  // }, []);

  constructor(props) {
    super(props);
    this.state = {
      arrays: [],
      audio: "",
      processed: "",
    };

    this.changeArrays = this.changeArrays.bind(this);
    this.changeAudio = this.changeAudio.bind(this);
    this.changeProcessed = this.changeProcessed.bind(this);
  }

  // constructor(props){
  //   super(props);
  //   this.state ={
  //     clicked:false
  //   }
  //   this.handleClick = this.handleClick.bind(this);
  // };

  changeArrays(new_arrays) {
    this.setState({ arrays: new_arrays });
    console.log(this.state.arrays);
  }

  changeAudio(newAudio) {
    this.setState({ audio: newAudio });
    console.log("audio ", this.state.audio);
  }
  changeProcessed(newAudio) {
    this.setState({ processed: newAudio });
  }

  render() {
    return (
      <body>
        {/* <Header /> */}
        {/* <HomeScreenText /> */}
        <HomeScreenText />

        <FolderDialog
          changeArrays={this.changeArrays}
          changeAudio={this.changeAudio}
          changeProcessed={this.changeProcessed}
        />

        <Canvas data={this.state.arrays} />

        <PlayAudio audio={this.state.audio} processed={this.state.audio} />
        {/* <div class="folderContainer">
          <ShowChooseFolder title="Show Child"></ShowChooseFolder>
        </div>
        <div class="canvasContainer"></div> */}
      </body>
    );
  }
}

export default HomeScreen;
