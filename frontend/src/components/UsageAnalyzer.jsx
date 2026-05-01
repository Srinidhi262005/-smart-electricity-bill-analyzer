import { useState } from 'react';
import { analyzeUsage } from '../api/api';

function UsageAnalyzer({ onResult }) {
  const [history, setHistory] = useState('');
  const [report, setReport] = useState(null);
  const [error, setError] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError('');
    try {
      const values = history
        .split(',')
        .map((value) => Number(value.trim()))
        .filter((value) => !Number.isNaN(value));
      if (values.length === 0) {
        setError('Please enter at least one numeric usage value.');
        return;
      }
      const response = await analyzeUsage(values);
      const anomalyReport = response.data.anomaly_report;
      setReport(anomalyReport);
      onResult({ ...anomalyReport, history: values });
    } catch {
      setError('Unable to analyze usage.');
    }
  };

  return (
    <div className="card">
      <h2>Usage Analyzer</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="history">Recent units (comma-separated)</label>
        <input
          id="history"
          value={history}
          onChange={(e) => setHistory(e.target.value)}
          placeholder="e.g. 120, 135, 150, 180"
          required
        />
        <button type="submit">Detect Abnormality</button>
      </form>
      {error && <p className="error">{error}</p>}
      {report && (
        <div className="summary">
          <p>{report.abnormal ? 'Abnormal usage detected' : 'Usage is normal'}</p>
          <p>Average: {report.mean} units</p>
          <p>Latest: {report.latest} units</p>
          <ul>
            {report.pattern.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default UsageAnalyzer;
