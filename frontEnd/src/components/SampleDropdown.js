import React, { useRef, useEffect } from "react";
import { convertToObject } from "typescript";

class Canvas extends React.Component {
	constructor(props){
		super(props);
		this.state = {
		  file: "",
		  value: "",
		  
		};
		this.handleChange=this.handleChange.bind(this);
	}
	
	handleChange(event){
		this.props.changeArrays(JSON.parse(this.props.defaults[event.target.value]["data"]));
		this.props.changeAudio(this.props.defaults[event.target.value]["audio_in"].substring(2, this.props.defaults[event.target.value]["audio_in"].length - 1),this.props.defaults[event.target.value]["audio_out"].substring(2, this.props.defaults[event.target.value]["audio_out"].length - 1))
		console.log(this.props.defaults[event.target.value]["audio_in"])
		this.setState({value: event.target.value});
	}
	
  render(){
	  console.log("rendered");
	const styles={
		border: "1px solid black"
		
	};
	return (
	 <div>
		<select value={this.state.value} onChange={this.handleChange} >
		<option value="sine"> Sine </option>
		<option value="cantina"> Cantina </option>
		<option value="star_wars"> Star Wars </option>
		<option value= "taunt"> Taunt </option>
		
		</select>
	</div>

	);
  }
};

export default Canvas;
