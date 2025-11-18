import { useState } from "react";
import { Heart } from "lucide-react";
import axios from "axios";

export default function PredictionForm() {

  const [formData, setFormData] = useState({
    age: "",
    sex: "",
    chestPain: "",
    restingBP: "",
    cholesterol: "",
    fbs: "",
    restingECG: "",
    maxHeartRate: "",
    exerciseAngina: "",
    oldpeak: "",
    stSlope: ""
  });

  const handleChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  return (
    <div className="predict-form-container" id="prediction-form">

      <h2 className="form-title">HEART'S DATA</h2>
      <p className="form-subtitle">Input your data here</p>

      {/* GRID */}
      <div className="form-grid">

        {[
          ["age", "Age"],
          ["sex", "Sex"],
          ["chestPain", "Chest pain"],
          ["restingBP", "Blood pressure"],
          ["cholesterol", "Serum cholesterol"],
          ["fbs", "Fasting blood sugar"],
          ["restingECG", "Electrocardiographic"],
          ["maxHeartRate", "Max heart rate"],
          ["exerciseAngina", "Induced angina"],
          ["oldpeak", "ST depression"],
          ["stSlope", "Slope"],
          ["vessels", "Vessels"]
        ].map(([name, placeholder]) => (
          <div className="input-box" key={name}>
            <Heart size={18} className="heart-icon" />
            <input
              name={name}
              placeholder={placeholder}
              onChange={handleChange}
            />
          </div>
        ))}

      </div>

      <button className="analyze-btn">ANALYZE</button>
    </div>
  );
}