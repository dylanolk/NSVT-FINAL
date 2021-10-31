import React, { useRef, useEffect } from "react";
import { convertToObject } from "typescript";

const Canvas = (props) => {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const context = canvas.getContext("2d");
    canvas.width = 680;
    canvas.height = 400;
    context.beginPath();
    context.rect(0, 0, 680, 400);
    context.fillStyle = "white";
    context.fill();
    context.font = "bold 30px Arial";
    context.strokeText("This is where the visualization will appear!", 10, 50);

    // context.moveTo(200, 0);
    // context.lineTo(200, 100);
    // context.stroke();
    // context.moveTo(0, 50);
    // context.lineTo(200, 50);
    // context.stroke();
  }, []);
  return <canvas ref={canvasRef} {...props} />;
};

export default Canvas;
