import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../pages/css/Dashboard.css';

const BASE_URL = 'http://localhost:5000';

const Dashboard = () => {
  const [username, setUsername] = useState(''); 
  const [groups, setGroups] = useState([]);
  const navigate = useNavigate();

  //log out
  const handleLogout = () => {
    localStorage.removeItem("username"); 
    navigate("/"); 
  };

  useEffect(() => {
     const savedUsername = localStorage.getItem("username");
     if (savedUsername) {
      setUsername(savedUsername);
  }

    fetch(`${BASE_URL}/groups/`)
      .then(res => res.json())
      .then(data => setGroups(data))
      .catch(err => console.error('Error fetching groups:', err));
  }, []);

  return (
    <div className="dashboard">
      <aside className="sidebar">
        <h2 className="brand">Proxima Centauri</h2>
        <nav>
          <ul>
            <li className="active">Dashboard</li>
            <li>Groups</li>
            <li>Transactions</li>
            <li>Profile</li>
          </ul>
          <button className="logout-btn" onClick={handleLogout}>Logout</button>
        </nav>
      </aside>

      <main className="main-content">
        <h1>Karibu, {username}</h1>

        <div className="cards">
          <div className="card balance-card">
            <h3>Total Balance</h3>
            <p className="amount">Ksh 15,241.45</p>
          </div>

          <div className="card groups-card">
            <h3>Your Groups</h3>
            <ul>
              {groups.length > 0 ? (
                groups.map(group => (
                  <li key={group.group_id}>{group.group_name}</li>
                ))
              ) : (
                <li>No groups found</li>
              )}
            </ul>
          </div>
        </div>

        <div className="transactions">
          <h3>Recent Transactions</h3>
        </div>
      </main>
    </div>
  );
};

export default Dashboard;
