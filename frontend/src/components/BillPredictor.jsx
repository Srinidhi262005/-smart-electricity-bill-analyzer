import { useState } from 'react';
import { predictBill, getSuggestions } from '../api/api';

function BillPredictor({ onResult, onSuggestions = () => {} }) {
  const [units, setUnits] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError('');
    setLoading(true);
    try {
      const response = await predictBill(Number(units));
      const payload = response.data.predicted_bill;
      setResult(payload);
      onResult(payload);

      const suggestionsResponse = await getSuggestions(Number(units));
      const suggestionsData = suggestionsResponse.data;
      onSuggestions(suggestionsData.suggestions || []);
    } catch (exception) {
      setError('Unable to fetch bill prediction.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>Bill Prediction</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="units">Units consumed</label>
        <input
          id="units"
          type="number"
          min="0"
          value={units}
          onChange={(e) => setUnits(e.target.value)}
          placeholder="Enter monthly units"
          required
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Estimating...' : 'Estimate Bill'}
        </button>
      </form>
      {error && <p className="error">{error}</p>}
      {result && (
        <div className="summary">
          <p>Estimated bill: ₹{result.estimate}</p>
          <p>Range: ₹{result.low} - ₹{result.high}</p>
        </div>
      )}
    </div>
  );
}

export default BillPredictor;
