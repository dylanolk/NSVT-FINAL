import React, { useRef, useEffect } from "react";
import { convertToObject } from "typescript";
import "./Canvas.style.css";

class Canvas extends React.Component {
	constructor(props){
		super(props);
		this.state={
			ARR_NUM : 0, 
			MOUSE_POS: 0,
			SCALE_FACTOR: 1,
			DISPLAY_TRANSFORM: 3, 
			DISPLAY_ORIGINAL: 1,
			checked1:true,
			checked2:true,
			checked3: true,
			SHIFT: 0,
			vertical_scale:1,
			
		};
		this.getMax=this.getMax.bind(this);
		this.display=this.display.bind(this);
		this.wheelZoom=this.wheelZoom.bind(this);
		this.mouseMove=this.mouseMove.bind(this);
		this.displayTransform= this.displayTransform.bind(this);
		this.displayOriginal = this.displayOriginal.bind(this);
		this.displayLines = this.displayLines.bind(this);
	}

//Takes in current position in array, array number, and data. Returns local max and mins within a window of size SCALE_FACTOR
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

//Main display function, called on every zoom/ update. Should not be called when there is no data. 
	display(){
		var canvas=this.refs.canvas;
		var c=canvas.getContext('2d');
		var data=this.props.data;
		
		var SCALE_FACTOR= this.state.SCALE_FACTOR
		c.canvas.width=1920
		c.moveTo(0, 250)
		c.lineTo(1920, 250)
		c.stroke();
		console.log(this.props.data);
		if(this.props.data.length==0 || !this.props.data)
			return;
		for(var i = this.state.DISPLAY_ORIGINAL; i<this.state.DISPLAY_TRANSFORM; i++){
			
			var change=1;
			if (i==2)
				change= this.props.data[3]
			// console.log(change);
			var x_coordinate=0;
			c.beginPath();
			var lines=0;
			var max=0;
			if (this.state.checked3){
				for(var x = Math.floor(this.state.SHIFT/Math.pow(10,this.state.ARR_NUM)/change); x<data[i][this.state.ARR_NUM].length; x++){
					
					if(lines>=1920) break;

					if(SCALE_FACTOR>1){
						var y = this.getMax(x,i,data)
								c.moveTo(Math.floor(x_coordinate*change),((0-y[2])*this.state.vertical_scale/data[0][0]+250)) 
								c.lineTo(Math.floor(x_coordinate*change), ((0-y[1])*this.state.vertical_scale/data[0][0]+250))
					}
					else if (SCALE_FACTOR<0) {
						c.moveTo(x_coordinate*Math.abs(SCALE_FACTOR)*change, 250) 
						c.lineTo(x_coordinate*Math.abs(SCALE_FACTOR)*change, ((0-data[i][this.state.ARR_NUM][x]*this.state.vertical_scale/data[0][0][0])+250))
						var y=[x,0,0]
					}
					else{
						c.moveTo(x_coordinate*change, 250) 
						c.lineTo(x_coordinate*change, ((0-data[i][this.state.ARR_NUM][x]*this.state.vertical_scale/data[0][0][0])+250))
						var y=[x,0,0]
					}

					lines++;
					
					x_coordinate+=1;
					x=y[0]
					max=x;
				}
			}
			else{
				for(var x = Math.floor(this.state.SHIFT/Math.pow(10,this.state.ARR_NUM)/change); x<data[i][this.state.ARR_NUM].length; x++){
					
					if(lines>=1920) break;

					if(SCALE_FACTOR>1){
						var y = this.getMax(x,i,data)
								c.fillRect(Math.floor(x_coordinate*change),(0-y[2])/data[0][0]+250,2,2) 
								c.fillRect(Math.floor(x_coordinate*change), (0-y[1])/data[0][0]+250,2,2)
					}
					else if (SCALE_FACTOR<0) {
						c.fillRect(x_coordinate*Math.abs(SCALE_FACTOR)*change, 250,2,2) 
						c.fillRect(x_coordinate*Math.abs(SCALE_FACTOR)*change, (0-data[i][this.state.ARR_NUM][x]/data[0][0][0])+250,2,2)
						var y=[x,0,0]
					}
					else{
						c.fillRect(x_coordinate*change, 250,2,2) 
						c.fillRect(x_coordinate*change, (0-data[i][this.state.ARR_NUM][x]/data[0][0][0])+250,2,2)
						var y=[x,0,0]
					}

					lines++;
					
					x_coordinate+=1;
					x=y[0]
					max=x;
				}
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
		if(Math.abs(event.deltaY/Math.abs(event.deltaY)) != 1){
			return
		}
		event.preventDefault();
		console.log(event);
		console.log(this.state.SHIFT);
		
		if(event.ctrlKey){
			this.state.SCALE_FACTOR= this.state.SCALE_FACTOR+=Math.floor(event.deltaY/Math.abs(event.deltaY));
			if(this.state.SCALE_FACTOR > 19 && this.state.ARR_NUM<this.props.data.length){
				this.state.SCALE_FACTOR=2;
				this.state.ARR_NUM++;
			}
			else if(this.state.SCALE_FACTOR <= 1 && this.state.ARR_NUM>=1){
				this.state.SCALE_FACTOR=19;
				this.state.ARR_NUM--;
			}
			console.log(this.state.SCALE_FACTOR, this.state.ARR_NUM);
		}
		
		else if(event.shiftKey){
			this.state.vertical_scale-=Math.floor(event.deltaY/Math.abs(event.deltaY));
			if(this.state.vertical_scale <=1)
				this.state.vertical_scale=1;
			console.log(this.state.vertical_scale);
		}
		
		else{
			this.state.SHIFT+=Math.floor(event.deltaY/Math.abs(event.deltaY))*500;
			if(this.state.SHIFT<=0){
				this.state.SHIFT=0;
			}
		}
		
		this.display();
	}
	
	//Stores current mouse position, useful for centering zoom on mouse, not yet implemented. 
	mouseMove(event){
		var canvas=this.refs.canvas;
		var cRect = canvas.getBoundingClientRect();
		this.state.MOUSE_POS = Math.round(event.clientX - cRect.left);
	}
	
	displayLines(event){
		this.setState({checked3: event.target.checked})
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
		this.display();
		
	}
	
	displayTransform(event){
		if(event.target.checked){
			this.setState({DISPLAY_TRANSFORM: 3})
		}
		else
			this.setState({DISPLAY_TRANSFORM: 2})
		this.display();
		this.setState({checked1: event.target.checked})
	}
	
	displayOriginal(event){
		if(event.target.checked)
			this.setState({DISPLAY_ORIGINAL: 1})
		else
			this.setState({DISPLAY_ORIGINAL: 2})
		this.display();
		this.setState({checked2: event.target.checked})
	}
	
  render(){
	  console.log("rendered");
	const styles={
		border: "1px solid black"
		
	};
	return (
	 <div>
		<canvas ref="canvas" class="my_canvas" width={1920} height={500} style={styles}/>
		<form onSubmit={this.handleSubmit}> 
		<div class="checkboxes">
		<div class="checkbox">
          <input type="checkbox" checked={this.state.checked1} onChange={this.displayTransform}/>
			{"Display Downsampled Waveform"}
		</div>
		<div class="checkbox">
			 <input type="checkbox" checked={this.state.checked2} onChange={this.displayOriginal}/>
			{"Display Original Waveform"}
		</div>
		<div class="checkbox">
			<input type="checkbox" checked={this.state.checked3} onChange={this.displayLines}/>
			{"Draw Lines to Samples"}
			</div>
			</div>
		</form>
	
	</div>

	);
  }
};

export default Canvas;
