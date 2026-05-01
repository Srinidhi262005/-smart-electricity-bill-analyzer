import { useState } from 'react';
import { uploadOCR } from '../api/api';

function UploadOCR({ onText }) {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError('');
    if (!file) {
      setError('Please choose an image file first.');
      return;
    }
    setLoading(true);
    try {
      const response = await uploadOCR(file);
      setResult(response.data.text);
      onText(response.data.text);
    } catch (exception) {
      setError('OCR extraction failed. Please try a clearer image.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>Meter OCR</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="file"
          accept="image/*"
          onChange={(e) => setFile(e.target.files?.[0] ?? null)}
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Processing...' : 'Extract Text'}
        </button>
      </form>
      {error && <p className="error">{error}</p>}
      {result && (
        <div className="summary">
          <p>Detected Text:</p>
          <pre>{result}</pre>
        </div>
      )}
    </div>
  );
}

export default UploadOCR;
