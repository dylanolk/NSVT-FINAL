import React, { useEffect, useState } from "react";
import "./HomeScreen.style.css";
import Header from "../../components/Header/Header";
import FolderDialog from "../../components/FolderDialog/FolderDialog";
import Canvas from "../../components/canvas/Canvas";
import Footer from "../../components/footer/Footer";
import Button from "../../components/buttons/Button";
import ShowChooseFolder from "../../components/ShowChooseFolder";
import ShowCanvas from "../../components/ShowCanvas";
import HomeScreenText from "../../components/text/HomeScreenText";
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
    };

    this.changeArrays = this.changeArrays.bind(this);
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

  render() {
    return (
      <body>
        {/* <Header /> */}
        {/* <HomeScreenText /> */}
        <HomeScreenText />
        <div class="folderContainer">
          <ShowChooseFolder title="Show Child">
            <FolderDialog changeArrays={this.changeArrays} />
          </ShowChooseFolder>
        </div>
        <div class="canvasContainer">
          <ShowCanvas title="Show Child">
            <Canvas data={this.state.arrays} />
          </ShowCanvas>
        </div>
        <Footer />
      </body>
    );
  }
}

export default HomeScreen;
