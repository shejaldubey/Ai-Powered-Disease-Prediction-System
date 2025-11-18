import React from 'react';

export default function About() {
  return (
    <div className="page-wrapper">
      {/* Top Banner Image with Title */}
      <div className="page-banner">
        <div className="banner-content-centered">
          <h1 style={{ fontSize: "50px", textTransform: "uppercase", letterSpacing: "1px" }}>
            AI Powered Heart Disease <br /> Prediction System
          </h1>
        </div>
      </div>

      {/* Detailed Information Section */}
      <div className="about-details-container">
        
        {/* Introduction Section */}
        <section className="about-section">
          <h2>Project Overview</h2>
          <h3>Introduction</h3>
          <p>
            Cardiovascular diseases (CVDs) remain one of the leading causes of mortality globally. 
            Early diagnosis and intervention are crucial for reducing fatality rates. This project, 
            developed as a Minor Project, implements a robust Machine Learning system designed to 
            predict the likelihood of heart disease in patients. By analyzing physiological data, 
            the system provides a real-time risk assessment, aiding healthcare professionals and 
            individuals in making informed health decisions.
          </p>
        </section>

        {/* Technical Architecture */}
        <section className="about-section">
          <h2>Technical Architecture: The Random Forest Model</h2>
          <p>
            The core engine of this prediction system is built upon the <strong>Random Forest Algorithm</strong>. 
            We chose this specific ensemble learning method for its superiority in medical diagnostics over single Decision Trees.
          </p>

          <h3>How it Works</h3>
          <p>
            The model constructs a multitude of decision trees at training time. For a classification task 
            like Heart Disease (Yes/No), the output is determined by the mode of the classes (voting) of the individual trees.
          </p>

          <h3>Why Random Forest?</h3>
          <ul className="feature-list">
            <li>
              <strong>Handling Overfitting:</strong> Unlike single decision trees, which often memorize data, 
              Random Forest averages multiple trees, reducing variance and ensuring the model generalizes well to new patients.
            </li>
            <li>
              <strong>Feature Importance:</strong> The algorithm effectively identifies which factors 
              (e.g., Chest Pain Type, Cholesterol levels) contribute most heavily to the prediction.
            </li>
            <li>
              <strong>Robustness:</strong> It maintains high accuracy even when there are missing values 
              or outliers in the medical data.
            </li>
          </ul>
        </section>

        {/* Data Sources */}
        <section className="about-section">
          <h2>Data Sources & Validation</h2>
          <p>
            To ensure the system is not biased toward a specific demographic and yields scientifically valid results, 
            the model was trained and validated on two major, disparate datasets:
          </p>

          <div className="data-source-card">
            <h3>UCI Machine Learning Repository</h3>
            <p>
              Utilized the renowned Cleveland Heart Disease dataset. Includes critical features such as Age, Sex, 
              Chest Pain Type (cp), Resting Blood Pressure (trestbps), Serum Cholesterol (chol), Fasting Blood Sugar (fbs), 
              and Resting Electrocardiographic results.
            </p>
          </div>

          <div className="data-source-card">
            <h3>IEEE DataPort Dataset</h3>
            <p>
              Used to supplement training data and test the model on a larger, more modern scale.
            </p>
          </div>

          <h3>Validation Strategy</h3>
          <p>
            The model utilizes Cross-Validation techniques. By training on subsets of these combined datasets 
            and testing on unseen data, we ensure that the "High Accuracy" and "Reliability" claims are 
            statistically significant and reproducible in real-world scenarios.
          </p>
        </section>

        {/* Key Features */}
        <section className="about-section">
          <h2>Key Project Features</h2>
          <ul className="check-list">
            <li><strong>Real-Time Risk Assessment:</strong> Users can input health metrics and receive an instant prediction regarding their cardiovascular risk status.</li>
            <li><strong>High Accuracy:</strong> Through hyperparameter tuning of the Random Forest model, the system achieves superior precision and recall compared to standard baseline models.</li>
            <li><strong>Scalable Design:</strong> The architecture allows for easy integration of new medical datasets in the future to further refine accuracy.</li>
          </ul>
        </section>

        {/* Contributors */}
        <section className="about-section team-section">
          <h2>Project Contributors</h2>
          <p>This system was developed as a Minor Project by a dedicated team of students.</p>
          
          <div className="team-grid">
            <div className="team-group">
              <h3>Team Members</h3>
              <ul>
                <li>Shreyansh Mishra</li>
                <li>Shejal Dubey</li>
                <li>Shivansh</li>
              </ul>
            </div>
            <div className="team-group guidance">
              <h3>Under the Guidance of</h3>
              <p className="prof-name">Prof. Vipin Tyagi</p>
            </div>
          </div>
        </section>

      </div>
    </div>
  );
}