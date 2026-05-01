import { useState } from 'react';
import { sendChat } from '../api/api';

function Chatbot() {
  const [message, setMessage] = useState('');
  const [lang, setLang] = useState('en');
  const [reply, setReply] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError('');
    if (!message.trim()) {
      setError('Type a message to start chat.');
      return;
    }
    setLoading(true);
    try {
      const response = await sendChat(message, lang);
      setReply(response.data.response);
    } catch (exception) {
      setError('Chat service unavailable.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">
      <h2>Chatbot</h2>
      <form onSubmit={handleSubmit}>
        <div className="select-row">
          <label htmlFor="lang">Language</label>
          <select id="lang" value={lang} onChange={(e) => setLang(e.target.value)}>
            <option value="en">English</option>
            <option value="te">Telugu</option>
          </select>
        </div>
        <textarea
          rows="3"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Ask about bill prediction, usage, or savings"
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Sending...' : 'Send'}
        </button>
      </form>
      {error && <p className="error">{error}</p>}
      {reply && (
        <div className="summary">
          <p>{reply}</p>
        </div>
      )}
    </div>
  );
}

export default Chatbot;
