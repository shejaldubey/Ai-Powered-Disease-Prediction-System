import { Link } from "react-router-dom";

export default function Hero() {
  return (
    <div className="hero-modern">

      <div className="hero-content">
        <h1>AI-Powered Heart<br />Disease Prediction System </h1>

        <p>
          A smart, ML-driven health assistant designed to help assess your
          risk of heart disease with maximum accuracy and reliability.
        </p>

        <Link to="/predict">
          <button className="hero-btn">Start Prediction</button>
        </Link>
      </div>

    </div>
  );
}