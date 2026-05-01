import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import UploadMeterPage from './pages/UploadMeterPage';
import InsightsPage from './pages/InsightsPage';
import ChatAssistantPage from './pages/ChatAssistantPage';
import './styles/App.css';

function App() {
  return (
    <Router>
      <div className="app-shell">
        <header>
          <h1>Smart Electricity Bill Predictor & Analyzer</h1>
          <nav>
            <Link to="/">Dashboard</Link>
            <Link to="/upload">Upload Meter</Link>
            <Link to="/insights">Insights</Link>
            <Link to="/chat">Chat Assistant</Link>
          </nav>
        </header>

        <main>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/upload" element={<UploadMeterPage />} />
            <Route path="/insights" element={<InsightsPage />} />
            <Route path="/chat" element={<ChatAssistantPage />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
