import { NavLink } from 'react-router-dom';

function Navigation() {
  return (
    <header className="site-header">
      <div>
        <h1>Smart Electricity Bill</h1>
        <p>Predict, analyze, extract meter readings, and save energy.</p>
      </div>
      <nav className="site-nav">
        <NavLink to="/" end>
          Dashboard
        </NavLink>
        <NavLink to="/upload">Upload Meter</NavLink>
        <NavLink to="/insights">Insights</NavLink>
        <NavLink to="/chat">Chat Assistant</NavLink>
      </nav>
    </header>
  );
}

export default Navigation;
