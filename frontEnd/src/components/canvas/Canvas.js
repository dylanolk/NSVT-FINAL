import React, { useRef, useEffect } from "react";
import { convertToObject } from "typescript";

class Canvas extends React.Component {
	constructor(props){
		super(props);
		this.state={
			ARR_NUM : this.props.data[1].length-4, 
			MOUSE_POS: 0,
			SCALE_FACTOR: 1,
		};
		this.getMax=this.getMax.bind(this);
		this.display=this.display.bind(this);
		this.wheelZoom=this.wheelZoom.bind(this);
		this.mouseMove=this.mouseMove.bind(this);
	}


	getMax(x,arraynum,data){

		var max=[x,0,0] 
		for(var i=0; i<(this.state.SCALE_FACTOR); i++){
			max[0]=x
			if(data[arraynum][this.state.ARR_NUM][x]>max[1])
				max[1]=data[arraynum][this.state.ARR_NUM][x]

			else if(data[arraynum][this.state.ARR_NUM][x]<max[2])
				max[2]=data[arraynum][this.state.ARR_NUM][x]
			x++
		}
		return max
	}


	display(){
		var canvas=this.refs.canvas;
		var c=canvas.getContext('2d');
		var data=this.props.data;
		
		var SCALE_FACTOR= this.state.SCALE_FACTOR
		
		c.canvas.width=1920
		c.moveTo(0, 250)
		c.lineTo(1920, 250)
		c.stroke();
		
		for(var i = 1; i<data.length; i++){
			var x_coordinate=0;
			c.beginPath();
			var lines=0;
			var max=0;
			
			for(var x = 0; x<data[i][this.state.ARR_NUM].length; x++){
				
				if(lines>=1920) break;

				if(SCALE_FACTOR>1){
					var y = this.getMax(x,i,data)
						
							c.moveTo(x_coordinate,(0-y[2])/data[0][0]+250) 
							c.lineTo(x_coordinate, (0-y[1])/data[0][0]+250)
				}
				else if (SCALE_FACTOR<0) {
					c.moveTo(x_coordinate*Math.abs(SCALE_FACTOR), 250) 
					c.lineTo(x_coordinate*Math.abs(SCALE_FACTOR), (0-data[i][this.state.ARR_NUM][x]/data[0][0][0])+250)
					var y=[x,0,0]
				}
				else{
					c.moveTo(x_coordinate, 250) 
					c.lineTo(x_coordinate, (0-data[i][this.state.ARR_NUM][x]/data[0][0][0])+250)
					var y=[x,0,0]
				}

				lines++;
				
				x_coordinate+=1;
				x=y[0]
				max=x;
			}
			// console.log(max,"***");
			var colors = ['red', 'green', 'blue']
			c.strokeStyle=colors[i];
			c.stroke();
			c.closePath();
		}
		// console.log(max);
		// console.log(lines);
			
	}
	wheelZoom(event){
		event.preventDefault();

		this.state.SCALE_FACTOR= this.state.SCALE_FACTOR+=Math.floor(event.deltaY/102);
		
		
	
		if(this.state.SCALE_FACTOR > 19 && this.state.ARR_NUM<this.props.data.length){
			this.state.SCALE_FACTOR=2;
			this.state.ARR_NUM++;
		}
		else if(this.state.SCALE_FACTOR <= 1 && this.state.ARR_NUM>=1){
			this.state.SCALE_FACTOR=19;
			this.state.ARR_NUM--;
		}
		console.log(this.state.SCALE_FACTOR, this.state.ARR_NUM);
		this.display();
	}
	mouseMove(event){
		var canvas=this.refs.canvas;
		var cRect = canvas.getBoundingClientRect();
		this.state.MOUSE_POS = Math.round(event.clientX - cRect.left);
	}
	componentDidMount(){
		const canvas= this.refs.canvas;
		const c= canvas.getContext("2d")
		c.clearRect(0, 0, canvas.width, canvas.height);
		canvas.addEventListener("wheel", this.wheelZoom);
		canvas.addEventListener("mousemove", this.mouseMove);
		// this.display();
		
		c.moveTo(0, 250)
		c.lineTo(1920, 250)
		c.stroke()
		
	}
   componentDidUpdate() {
	   console.log("update");
	   const canvas= this.refs.canvas;
		const c= canvas.getContext("2d")
		c.clearRect(0, 0, canvas.width, canvas.height);
		if(this.props.data.length > 0)
			this.display();
		
	}
  render(){
	  console.log("rendered");
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
