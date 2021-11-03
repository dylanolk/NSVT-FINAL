import React, { useEffect } from "react";
import "./HomeScreen.style.css";
import Header from "../../components/Header/Header";
import FolderDialog from "../../components/FolderDialog/FolderDialog";
import Canvas from "../../components/canvas/Canvas";
import Footer from "../../components/footer/Footer";
import HomeScreenText from "../../components/text/HomeScreenText";
import axios from 'axios'

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
  constructor(props){
	  super(props);
	  this.state={
		  arrays:[],
	  };
	 
	  this.changeArrays = this.changeArrays.bind(this);
  }
  
  changeArrays(new_arrays){
	  this.setState({arrays: new_arrays});
	  console.log(this.state.arrays)
  }

	render(){
		
		return (
		<body>
		  <Header />
		  {/* <HomeScreenText /> */}
		  <div styles={{padding: "0px"}}>
			<FolderDialog changeArrays={this.changeArrays}/>
		  </div>
		  <div>
			<Canvas data={this.state.arrays} />
		  </div>
		  <Footer />
		</body>
		);
	}
}

export default HomeScreen;
