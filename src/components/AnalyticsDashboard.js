import React from "react";
import "./Analytics.css";
import { Layout } from "../Layout";

const AnalyticsDashboard = () => {
 
  const imageStyle = {
		display: "block", // Set images to display as blocks to stack them vertically
		margin: "10px 0 40px 0", // Add some margin between images
		width: "60%", // Set the width of the images
		height: "auto", // Automatically adjust the height while maintaining aspect ratio
    	marginLeft: "250px",
    
	};
  return (
		<Layout>
			<div className="dashboard-container">
				<h1 style={{textAlign:"center"}}>Sentimental Analysis Dashboard</h1>
				<div className="image-container">
					<img
						src="/sentiment_analysis.gif"
						alt="Chart"
						className="image-chart"
						style={imageStyle}
					/>

					<img
						src={"/new_sentiment_analysis_plot.png"}
						alt="Accuracy"
						className="image-accuracy"
						style={imageStyle}
					/>

					<img
						src={"/sentiment_analysis_trace_sim.gif"}
						alt="Accuracy"
						className="image-accuracy"
						style={imageStyle}
					/>
				</div>
			</div>
		</Layout>
	);
};

export default AnalyticsDashboard;
