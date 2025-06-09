//Navigation bar component
import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import '../css/NavBar.css'; 

const NavBar = ({ onLogout }) => {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("username");
    if (onLogout) onLogout(); // optional callback
    navigate("/");
  };

  return (
    <aside className="sidebar">
      <h2 className="brand">Proxima Centauri</h2>
      <nav>
        <ul>
          <li><Link to="/dashboard">Dashboard</Link></li>
          <li><Link to="/groups">Groups</Link></li>
          <li><Link to="/transactions">Transactions</Link></li>
          <li><Link to="/profile">Profile</Link></li>
        </ul>
        <button className="logout-btn" onClick={handleLogout}>Logout</button>
      </nav>
    </aside>
  );
};

export default NavBar;
