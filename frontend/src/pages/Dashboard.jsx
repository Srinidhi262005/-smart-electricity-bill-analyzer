import { useState } from 'react';
import BillPredictor from '../components/BillPredictor';
import UsageAnalyzer from '../components/UsageAnalyzer';

function Dashboard() {
  const [prediction, setPrediction] = useState(null);
  const [usageReport, setUsageReport] = useState(null);
  const [suggestions, setSuggestions] = useState([]);

  return (
    <div className="page-grid">
      <section className="card card-large dashboard-hero">
        <div>
          <h2>Dashboard</h2>
          <p>Track your electricity consumption, get accurate bill forecasts, and detect abnormal usage patterns all from one intelligent workspace.</p>
        </div>

        <div className="dashboard-metrics">
          <div className="metric-card">
            <h3>Predicted bill</h3>
            {prediction ? (
              <div className="metric-value">
                <span>₹{prediction.estimate}</span>
              </div>
            ) : (
              <div className="metric-value">
                <span>Awaiting input</span>
              </div>
            )}
            {prediction && <p className="metric-label">Range: ₹{prediction.low} - ₹{prediction.high}</p>}
          </div>

          <div className="metric-card">
            <h3>Usage summary</h3>
            {usageReport ? (
              <div className="metric-value">
                <span>{usageReport.abnormal ? 'Abnormal' : 'Normal'}</span>
              </div>
            ) : (
              <div className="metric-value">
                <span>No data yet</span>
              </div>
            )}
            {usageReport && <p className="metric-label">Latest: {usageReport.latest} units</p>}
          </div>
        </div>
      </section>

      <section className="page-grid-inner">
        <BillPredictor onResult={setPrediction} onSuggestions={setSuggestions} />
        <UsageAnalyzer onResult={setUsageReport} />
      </section>

      <section className="card">
        <h2>Actionable recommendations</h2>
        {suggestions.length > 0 ? (
          <ul className="tip-list">
            {suggestions.map((suggestion, index) => (
              <li key={index}>{suggestion}</li>
            ))}
          </ul>
        ) : (
          <p>Get a bill estimate to unlock targeted energy-saving tips.</p>
        )}
      </section>
    </div>
  );
}

export default Dashboard;
