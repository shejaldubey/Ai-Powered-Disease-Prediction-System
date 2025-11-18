export default function ResultCard({ result }) {
  return (
    <div className="result-card">
      <h2>Prediction Result</h2>

      <h3>
        {result.prediction === 1
          ? "⚠ High Risk of Cardiovascular Disease"
          : "✔ Low Risk — You're Safe"}
      </h3>

      <p>Model Confidence: {result.confidence}%</p>
    </div>
  );
}
