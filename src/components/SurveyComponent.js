// SurveyComponent.js
import React from "react";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import "./SurveyComponent.css";
import { Layout } from "../Layout";

function SurveyComponent() {
  const navigate = useNavigate();
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = (data) => {
    console.log(data);
    // Submit your data or perform any actions here
    navigate("/");
  };

  return (
    <Layout>
      <div className="main">
        <h1>Hello, folks!</h1>
        <p>Welcome to Citizen Council Connect Survey</p>
        <div className="form-container">
          <form onSubmit={handleSubmit(onSubmit)}>
            <label>Name:</label>
            <input type="text" {...register("name", { required: true })} />
            {errors.name && (
              <span className="error-message">Name is required</span>
            )}
            <br></br>
            <label>Email:</label>
            <input type="text" {...register("email", { required: true })} />
            {errors.email && (
              <span className="error-message">Email is required</span>
            )}
            <br></br>
            <label>Category:</label>
            <select {...register("category", { required: true })}>
              <option value="">Select a category</option>
              <option value="water">Water</option>
              <option value="traffic">Traffic</option>
              <option value="other">Other</option>
            </select>
            {errors.category && (
              <span className="error-message">Category is required</span>
            )}
            <br></br>
            <label>Rating:</label>
            <select {...register("rating", { required: true })}>
              <option value="">Select a rating</option>
              <option value="0">0</option>
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4</option>
              <option value="5">5</option>
            </select>
            {errors.rating && (
              <span className="error-message">Rating is required</span>
            )}
            <br></br>
            <label>Location:</label>
            <input type="text" {...register("location", { required: true })} />
            <label>Description:</label>
            <input type="text" className="description"{...register("description", { required: true })} />
            {errors.location && (
              <span className="error-message">Location is required</span>
            )}

            <div className="submitBtn">
              <input type="submit" value="Submit" />
            </div>
          </form>
        </div>
      </div>
    </Layout>
  );
}

export default SurveyComponent;
