function SuggestionsPanel({ prediction, anomaly, suggestions }) {
  return (
    <div className="card">
      <h2>Smart Suggestions</h2>
      {prediction ? (
        <div>
          <p>Estimated bill: ₹{prediction.estimate}</p>
          <p>Try to keep usage under the recommended slab.</p>
        </div>
      ) : (
        <p>Get a prediction to see personalized suggestions.</p>
      )}

      <ul>
        {suggestions?.map((suggestion, index) => (
          <li key={index}>{suggestion}</li>
        ))}
      </ul>

      {anomaly && anomaly.abnormal && (
        <div className="warning">
          <p>Abnormal usage detected. Review the reported pattern carefully.</p>
        </div>
      )}
    </div>
  );
}

export default SuggestionsPanel;
