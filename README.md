# Smart Electricity Bill Predictor & Analyzer

A comprehensive full-stack solution designed to empower users with insights into their energy consumption. This application leverages React, Flask, and Machine Learning to provide predictive billing, anomaly detection, and OCR-based meter reading.

## ✨ Key Features
- **Bill Prediction**: Estimate monthly costs based on unit consumption.
- **Anomaly Detection**: Identifies unusual usage spikes or inefficient consumption patterns using statistical analysis.
- **OCR Integration**: Extract meter readings directly from images using Tesseract OCR.
- **Smart Suggestions**: Context-aware energy-saving tips based on consumption levels.
- **Multilingual Chatbot**: Interactive support available in English and Telugu.

## 🚀 Tech Stack
- **Frontend**: React, Vite, Tailwind CSS
- **Backend**: Flask, SQLite
- **Database ORM**: SQLAlchemy
- **AI/ML**: NumPy (Statistical Analysis), Tesseract OCR

## 📂 Project Structure

- `backend/` - Flask API, ML prediction service, OCR integration, SQLite persistence
- `frontend/` - React + Vite user interface with bill prediction, usage analyzer, OCR upload, and chatbot

## 🛠️ Getting Started

### Backend + frontend single-host setup

1. Open `frontend/`
2. Install frontend dependencies and build the production app:
   ```bash
   npm install
   npm run build
   ```
3. Return to the project root, activate the Python virtual environment, and install backend dependencies:
   ```bash
   cd ..
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   python -m pip install -r backend\requirements.txt
   ```
4. Run the backend, which serves the built frontend from the same host:
   ```bash
   cd backend
   python app.py
   ```

The application will be available at: `http://localhost:5001`

### Optional: use a different port

If port `5001` is already in use, start the app on another port:
```bash
$env:PORT=5002
python app.py
```

## Notes

- The Flask backend serves the built React app from `frontend/dist`.
- This means the full application runs from a single host and single origin.
- OCR requires the native Tesseract binary to be installed separately on your OS.
