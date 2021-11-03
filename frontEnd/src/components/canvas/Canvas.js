import React, { useRef, useEffect } from "react";
import { convertToObject } from "typescript";

class Canvas extends React.Component {
	constructor(props){
		super(props);
		this.state={
			ARR_NUM : 1, 
			MOUSE_POS: 0,
			SCALE_FACTOR: 1,
		};
		this.getMax=this.getMax.bind(this);
		this.display=this.display.bind(this);
	}


	getMax(x){

		var max=[x,0,0] 
		for(var i=0; i<(this.state.SCALE_FACTOR); i++){
			max[0]=x
			if(this.props.data[this.state.ARR_NUM][x]>max[1])
				max[1]=this.props.data[this.state.ARR_NUM][x]

			else if(this.props.data[this.state.ARR_NUM][x]<max[2])
				max[2]=this.props.data[this.state.ARR_NUM][x]
			x++
		}
		return max
	}
	display(){
		console.log("hello!")
		const canvas = this.refs.canvas
		const c= canvas.getContext("2d")
		console.log(c);
		var x_coordinate=0;
		var lines=0;
		c.beginPath();
		c.moveTo(0, 250)
		c.lineTo(1920, 250)
		c.stroke();
		
		//weird starting variable for zooming
		for(var x = Math.floor(this.state.MOUSE_POS*(20-this.state.SCALE_FACTOR)/Math.pow(20, this.state.ARR_NUM)); x<this.props.data[this.state.ARR_NUM].length; x++){
			console.log("WOOO!")
			if(lines>=1920) break;
			if(this.state.SCALE_FACTOR>1){
				var y = this.getMax(x)
				c.moveTo(x_coordinate*2,0-y[2]+250) 
				c.lineTo(x_coordinate, 0-y[1]+250)
			}
			else{
				c.moveTo(x_coordinate*5, 250) 
				c.lineTo(x_coordinate*5, ((0-this.props.data[this.state.ARR_NUM][x])/this.props.data[0])+250)
				y=[x,0,0]
			}
			lines++;
			x_coordinate++;
			x=y[0]
			c.stroke();
			
		}
		c.closePath();
			
	}
	componentDidMount(){
		const canvas= this.refs.canvas;
		const c= canvas.getContext("2d")
		
		// c.moveTo(0, 250)
		// c.lineTo(1920, 250)
		// c.stroke()
		
	}
   componentDidUpdate() {
	   const canvas= this.refs.canvas;
		const c= canvas.getContext("2d")
		if(this.props.data.length > 0)
			this.display();
		
	}
  render(){
	const styles={
		border: "1px solid black"
		
	};
	return (
	 <div
		style={{
       
       
    }}>
	
		<canvas ref="canvas" width={1920} height={500} style={styles}/>
	</div>
	);
  }
};

export default Canvas;
