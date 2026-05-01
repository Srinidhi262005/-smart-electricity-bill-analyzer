import { useState } from 'react';
import UploadOCR from '../components/UploadOCR';

function UploadMeterPage() {
  const [extractedText, setExtractedText] = useState('');
  const [detectedUnits, setDetectedUnits] = useState(null);

  const handleResult = ({ text, units }) => {
    setExtractedText(text);
    setDetectedUnits(units);
  };

  return (
    <div className="page-grid">
      <section className="card card-large">
        <h2>Upload Meter Reading</h2>
        <p>Upload an image of your electricity meter and extract the detected values.</p>
        <UploadOCR onResult={handleResult} />
      </section>

      <section className="card card-large">
        <h3>Extracted result</h3>
        {extractedText ? (
          <div className="summary">
            <p>
              <strong>Detected units:</strong> {detectedUnits ?? 'Not found'}
            </p>
            <p>
              <strong>OCR text:</strong>
            </p>
            <pre>{extractedText}</pre>
          </div>
        ) : (
          <p>No meter image processed yet.</p>
        )}
      </section>
    </div>
  );
}

export default UploadMeterPage;
