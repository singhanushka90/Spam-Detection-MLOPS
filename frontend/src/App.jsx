import { useEffect, useState } from 'react'
import './App.css'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000'

function App() {
  const [mode, setMode] = useState('login')
  const [formData, setFormData] = useState({ username: '', email: '', password: '' })
  const [token, setToken] = useState(localStorage.getItem('token') || '')
  const [user, setUser] = useState(null)
  const [message, setMessage] = useState('')
  const [loading, setLoading] = useState(false)
  const [predictionText, setPredictionText] = useState('')
  const [predictionResult, setPredictionResult] = useState(null)
  const [history, setHistory] = useState([])
  const [historyLoading, setHistoryLoading] = useState(false)

  useEffect(() => {
    if (!token) return

    const fetchUser = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/auth/me`, {
          headers: { Authorization: `Bearer ${token}` },
        })

        if (response.ok) {
          const data = await response.json()
          setUser(data)
          fetchHistory(token)
        } else {
          localStorage.removeItem('token')
          setToken('')
        }
      } catch (error) {
        console.error(error)
      }
    }

    fetchUser()
  }, [token])

  const fetchHistory = async (authToken) => {
    setHistoryLoading(true)
    try {
      const response = await fetch(`${API_BASE_URL}/prediction/history`, {
        headers: { Authorization: `Bearer ${authToken}` },
      })
      if (response.ok) {
        const data = await response.json()
        setHistory(data)
      }
    } catch (error) {
      console.error(error)
    } finally {
      setHistoryLoading(false)
    }
  }

  const handleChange = (event) => {
    const { name, value } = event.target
    setFormData((prev) => ({ ...prev, [name]: value }))
  }

  const validateForm = () => {
    if (mode === 'register') {
      if (!formData.username.trim()) {
        throw new Error('Username is required')
      }
      if (formData.password.length < 8) {
        throw new Error('Password must be at least 8 characters long')
      }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
        throw new Error('Please enter a valid email address')
      }
    } else {
      if (!formData.email.trim()) {
        throw new Error('Email is required')
      }
      if (!formData.password) {
        throw new Error('Password is required')
      }
    }
  }

  const handleAuthSubmit = async (event) => {
    event.preventDefault()
    setLoading(true)
    setMessage('')

    try {
      validateForm()
      let response

      if (mode === 'login') {
        const body = new URLSearchParams({
          username: formData.email,
          password: formData.password,
        })

        response = await fetch(`${API_BASE_URL}/auth/login`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
          body,
        })
      } else {
        response = await fetch(`${API_BASE_URL}/auth/register`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            username: formData.username,
            email: formData.email,
            password: formData.password,
          }),
        })
      }

      const text = await response.text()
      let data = {}
      if (text) {
        data = JSON.parse(text)
      }

      if (!response.ok) {
        throw new Error(data.detail || 'Authentication failed')
      }

      if (mode === 'login') {
        localStorage.setItem('token', data.access_token)
        setToken(data.access_token)
        setMessage('Login successful')
      } else {
        setMode('login')
        setFormData({ username: '', email: '', password: '' })
        setMessage('Registration successful. Please log in now.')
      }
    } catch (error) {
      setMessage(error.message || 'Request failed. Please check the backend.')
    } finally {
      setLoading(false)
    }
  }

  const handlePrediction = async (event) => {
    event.preventDefault()
    if (!predictionText.trim()) {
      setMessage('Please enter a message first.')
      return
    }

    setLoading(true)
    setMessage('')
    setPredictionResult(null)

    try {
      const response = await fetch(`${API_BASE_URL}/prediction/predict`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ text: predictionText }),
      })

      const data = await response.json()
      if (!response.ok) {
        throw new Error(data.detail || 'Prediction failed')
      }

      setPredictionResult(data)
      setPredictionText('')
      fetchHistory(token)
      setMessage('Prediction completed successfully.')
    } catch (error) {
      setMessage(error.message || 'Prediction failed')
    } finally {
      setLoading(false)
    }
  }

  const handleLogout = () => {
    localStorage.removeItem('token')
    setToken('')
    setUser(null)
    setHistory([])
    setPredictionResult(null)
    setMessage('Logged out successfully')
  }

  return (
    <main className="app-shell">
      <section className="hero-card">
        <p className="eyebrow">Spam Detection MLOps</p>
        <h1>Full spam detection dashboard</h1>
        <p className="hero-text">
          Register, log in, test messages, and review your prediction history in one place.
        </p>
      </section>

      {!token ? (
        <section className="auth-card">
          <div className="mode-switch">
            <button type="button" className={mode === 'login' ? 'active' : ''} onClick={() => setMode('login')}>
              Login
            </button>
            <button type="button" className={mode === 'register' ? 'active' : ''} onClick={() => setMode('register')}>
              Register
            </button>
          </div>

          <form onSubmit={handleAuthSubmit} className="auth-form">
            {mode === 'register' && (
              <input name="username" type="text" placeholder="Username" value={formData.username} onChange={handleChange} required />
            )}
            <input name="email" type="email" placeholder="Email" value={formData.email} onChange={handleChange} required />
            <input name="password" type="password" placeholder="Password" value={formData.password} onChange={handleChange} required />
            <button type="submit" disabled={loading}>
              {loading ? 'Processing...' : mode === 'login' ? 'Login' : 'Register'}
            </button>
          </form>

          {message && <p className="message">{message}</p>}
        </section>
      ) : (
        <>
          <section className="dashboard-grid">
            <div className="panel">
              <div className="panel-header">
                <h2>Predict message</h2>
                <button type="button" className="ghost-btn" onClick={handleLogout}>Logout</button>
              </div>
              <form onSubmit={handlePrediction} className="predict-form">
                <textarea
                  value={predictionText}
                  onChange={(event) => setPredictionText(event.target.value)}
                  placeholder="Enter message to classify as spam or ham"
                  rows="6"
                />
                <button type="submit" disabled={loading}>
                  {loading ? 'Checking...' : 'Check message'}
                </button>
              </form>
              {message && <p className="message">{message}</p>}
              {predictionResult && (
                <div className="result-card">
                  <h3>{predictionResult.prediction}</h3>
                  <p>{predictionResult.text}</p>
                </div>
              )}
            </div>

            <div className="panel">
              <div className="panel-header">
                <h2>Prediction history</h2>
                <span>{user ? user.username : ''}</span>
              </div>
              {historyLoading ? (
                <p>Loading history...</p>
              ) : history.length === 0 ? (
                <p>No predictions yet.</p>
              ) : (
                <ul className="history-list">
                  {history.map((item, index) => (
                    <li key={`${item.created_at}-${index}`}>
                      <strong>{item.prediction}</strong>
                      <p>{item.text}</p>
                      <small>{new Date(item.created_at).toLocaleString()}</small>
                    </li>
                  ))}
                </ul>
              )}
            </div>
          </section>
        </>
      )}
    </main>
  )
}

export default App
