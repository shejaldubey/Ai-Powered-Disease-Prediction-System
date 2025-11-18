import PredictionForm from "../components/PredictionForm";
import { useNavigate } from "react-router-dom";

export default function Predict() {
  const navigate = useNavigate();

  // Function to scroll smoothly to the prediction form container (using its ID)
  const handleScrollToForm = () => {
    document.getElementById('prediction-form').scrollIntoView({ behavior: 'smooth' });
  };

  // Function to navigate to the About page
  const handleKnowMore = () => {
    navigate("/about");
  };

  return (
    <div className="predict-page"> 
      <div className="predict-banner">
        <div className="banner-content">
          <h1>EXAMINING YOUR HEARTS !</h1>
          <p>
            The goal of this project is to train a machine learning model to accurately 
            predict whether a sample patient has been diagnosed with heart disease, 
            with higher accuracy possible.
          </p>

          <div className="banner-buttons">
            <button className="btn-danger" onClick={handleScrollToForm}>CHECK YOUR HEART</button>
            <button className="btn-warning" onClick={handleKnowMore}>KNOW MORE</button>
          </div>
        </div>
      </div>

      <PredictionForm />
    </div>
  );
}