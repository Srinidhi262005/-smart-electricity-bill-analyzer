import { useState } from 'react';
import { getSuggestions } from '../api/api';

const baselineTips = [
  '💡 Replace incandescent bulbs with LED: saves 80% energy and lasts 25x longer.',
  '❄️ Set AC to 24-26°C: every degree higher saves 3-5% on your bill.',
  '🔌 Unplug phantom loads: chargers, printers, and standby devices waste 5-10W continuously.',
  '⏰ Run heavy appliances off-peak: washing machines and water heaters use 30-40% of daily energy.',
  '🌬️ Use ceiling fans instead of AC when possible: consume 99% less energy.',
  '🚿 Take shorter showers: reduces water heating energy by 5-10% monthly.',
  '🧊 Keep your fridge clean and defrosted: frost buildup increases energy use by 20%.',
  '📊 Monitor weekly meter readings: catch spikes early and identify problem appliances.',
];

function InsightsPage() {
  const [units, setUnits] = useState('');
  const [history, setHistory] = useState('');
  const [suggestions, setSuggestions] = useState([]);
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    setLoading(true);
    setError('');
    setSuggestions([]);
    try {
      const historyValues = history
        .split(',')
        .map((value) => Number(value.trim()))
        .filter((value) => !Number.isNaN(value));

      const response = await getSuggestions(Number(units), historyValues);
      setSuggestions(response.data.suggestions);
      setReport(response.data.anomaly_report);
    } catch {
      setError('Unable to fetch insights. Please verify your input and try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-grid">
      <section className="card card-large">
        <h2>Insights</h2>
        <p>Review smart tips and customized suggestions to reduce your electricity bill.</p>

        <div className="panel-row-soft">
          <div className="panel-block">
            <h3>Quick energy tips</h3>
            <ul>
              {baselineTips.map((tip, index) => (
                <li key={index}>{tip}</li>
              ))}
            </ul>
          </div>

          <div className="panel-block">
            <h3>Personalized suggestions</h3>
            <form onSubmit={handleSubmit} className="form-grid">
              <label>
                Units consumed
                <input
                  type="number"
                  min="0"
                  value={units}
                  onChange={(e) => setUnits(e.target.value)}
                  placeholder="e.g. 210"
                  required
                />
              </label>
              <label>
                Recent history
                <input
                  value={history}
                  onChange={(e) => setHistory(e.target.value)}
                  placeholder="e.g. 120, 135, 150"
                />
              </label>
              <button type="submit" disabled={loading}>
                {loading ? 'Loading...' : 'Fetch suggestions'}
              </button>
            </form>
            {error && <p className="error">{error}</p>}
            {report && (
              <div className="summary">
                <p>Usage pattern: {report.abnormal ? 'Abnormal' : 'Normal'}</p>
              </div>
            )}
            {suggestions.length > 0 && (
              <ul className="tip-list">
                {suggestions.map((item, index) => (
                  <li key={index}>{item}</li>
                ))}
              </ul>
            )}
          </div>
        </div>
      </section>
    </div>
  );
}

export default InsightsPage;
