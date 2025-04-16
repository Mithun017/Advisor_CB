// src/App.jsx
import { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import './app.css';

function App() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [userName, setUserName] = useState('');
  const inputRef = useRef();

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;

    setLoading(true);
    setResponse('');

    try {
      const res = await axios.post('http://localhost:5000/chat', {
        user_id: userName || 'guest',
        query: query,
      });
      setResponse(res.data.response);
      setHistory((prev) => [...prev, { query, response: res.data.response }]);
      setQuery('');
    } catch (err) {
      setResponse('⚠️ Unable to contact the AI agent. Please ensure the backend is running.');
    } finally {
      setLoading(false);
    }
  };

  const loadHistory = async () => {
    if (!userName) return;
    try {
      const res = await axios.get(`http://localhost:5000/history?user_id=${userName}`);
      setHistory(res.data.history || []);
    } catch (err) {
      console.error('Error loading history:', err);
    }
  };

  useEffect(() => {
    inputRef.current?.focus();
    if (userName) loadHistory();
  }, [userName]);

  return (
    <div className="app-wrapper bg-black text-light d-flex flex-column min-vh-100">
      <header className="d-flex justify-content-between align-items-center px-3 py-2 bg-dark shadow-sm w-100 position-relative" style={{ height: '60px' }}>
        <div className="d-flex align-items-center" style={{ width: '220px' }}>
          <input
            type="text"
            className="form-control form-control-sm bg-black text-light border-secondary"
            placeholder="Enter your name"
            value={userName}
            onChange={(e) => setUserName(e.target.value)}
          />
        </div>
        <div className="position-absolute top-50 start-50 translate-middle">
          <strong className="fs-6 text-light">🤖 Advisor Chatbot</strong>
        </div>
      </header>

      <main className="container-fluid flex-grow-1 d-flex flex-column justify-content-between px-3 py-3">
        <div className="flex-grow-1 overflow-auto">
          {history.map((entry, index) => (
            <div key={index} className="mb-3">
              <div className="text-info"><strong>You:</strong> <pre className="mb-0 text-info">{entry.query}</pre></div>
              <div className="text-light"><strong>Bot:</strong> <pre className="bg-dark p-2 rounded-2 text-light">{entry.response}</pre></div>
            </div>
          ))}
        </div>

        <form onSubmit={handleSubmit} className="bg-dark rounded-4 p-2 mt-3 shadow-lg d-flex align-items-center flex-wrap">
          <input
            type="text"
            className="form-control border-secondary bg-black text-light me-2 mb-2 mb-sm-0"
            placeholder="Type your question and press Enter..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            ref={inputRef}
            style={{ flex: 1 }}
          />
          <button className="btn btn-primary px-3" type="submit" disabled={loading}>
            {loading ? '...' : '➤'}
          </button>
        </form>
      </main>
    </div>
  );
}

export default App;