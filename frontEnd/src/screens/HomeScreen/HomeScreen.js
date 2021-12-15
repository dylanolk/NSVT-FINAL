import React, { useEffect, useState } from "react";
import "./HomeScreen.style.css";
import Header from "../../components/Header/Header";
import FolderDialog from "../../components/FolderDialog/FolderDialog";
import Canvas from "../../components/canvas/Canvas";
import Footer from "../../components/footer/Footer";
import Button from "../../components/buttons/Button";
import SampleDropdown from "../../components/SampleDropdown";
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
	  defaults: {},
    };

    this.changeArrays = this.changeArrays.bind(this);
    this.changeAudio = this.changeAudio.bind(this);
  }

  // constructor(props){
  //   super(props);
  //   this.state ={
  //     clicked:false
  //   }
  //   this.handleClick = this.handleClick.bind(this);
  // };
   async componentDidMount(){
    var temparray = [];
    await axios
      .get("http://127.0.0.1:5000/defaults")
      .then(function (response) {
        return response;
      })
      .then(function (text) {
        temparray = text.data;
      });
    console.log(temparray);
    this.setState({defaults:temparray});
	console.log(this.state.arrays);
  }

  changeArrays(new_arrays) {
    this.setState({ arrays: new_arrays });
    console.log(this.state.arrays);
  }

  changeAudio(newAudio, newProcessed) {
    this.setState({ audio: newAudio });
    this.setState({ processed: newProcessed });
  }


  render() {
    return (
      <body>
        {/* <Header /> */}
        {/* <HomeScreenText /> */}
>
		<div>
			<FolderDialog
			  changeArrays={this.changeArrays}
			  changeAudio={this.changeAudio}
			/>
			<PlayAudio
			  audio={this.state.audio}
			  processed={this.state.processed}
			  data={this.state.arrays["data"]}
			/>
		</div>
		<SampleDropdown changeArrays={this.changeArrays} changeAudio={this.changeAudio} defaults={this.state.defaults} class="dropdown"/>
        <Canvas data={this.state.arrays} />

        
        {/* <div class="folderContainer">
          <ShowChooseFolder title="Show Child"></ShowChooseFolder>
        </div>
        <div class="canvasContainer"></div> */}
      </body>
    );
  }
}

export default HomeScreen;
